#!/usr/bin/env python3
"""Check local image and picture/srcset references in a built Hugo website.

Usage: python -B scripts/audit-site-images.py BUILD_DIR [--json]
This checks files and HTML, not browser rendering or external availability.
Empty alt text is reported for contextual review, not treated as proof of error.
"""

import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Images(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.pictures = 0
        self.elements = []

    def handle_starttag(self, tag, attrs):
        if tag == "picture":
            self.pictures += 1
        if tag == "img" or (tag == "source" and self.pictures):
            self.elements.append((tag, dict(attrs)))

    def handle_endtag(self, tag):
        if tag == "picture":
            self.pictures = max(0, self.pictures - 1)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build", type=Path)
    parser.add_argument("--json", action="store_true", help="Print the full review queue as JSON")
    args = parser.parse_args()
    root = args.build.resolve()
    pages = sorted(root.rglob("*.html"))
    if not (root / "index.html").is_file():
        raise SystemExit("FAIL: build directory must contain index.html")
    report = {"html_pages": len(pages), "image_elements": 0,
              "local_image_references": 0, "missing_local_files": [],
              "empty_image_sources": [], "empty_alt_review": [],
              "external_image_urls": []}
    external = set()
    for page in pages:
        parsed = Images()
        parsed.feed(page.read_text(encoding="utf-8"))
        rel = page.relative_to(root).as_posix()
        for tag, attrs in parsed.elements:
            source = attrs.get("src") or ""
            if tag == "img":
                report["image_elements"] += 1
                if not source:
                    report["empty_image_sources"].append({"page": rel, "id": attrs.get("id", "")})
                if not (attrs.get("alt") or "").strip():
                    report["empty_alt_review"].append({"page": rel, "src": source})
            urls = [source] if source else []
            srcset = attrs.get("srcset") or ""
            # Inline data URLs can contain commas and have no local file to check.
            if srcset and not srcset.lstrip().startswith("data:"):
                urls.extend(item.strip().split()[0] for item in srcset.split(",") if item.strip())
            for url in urls:
                parsed_url = urlsplit(url)
                if parsed_url.scheme == "data":
                    continue
                if parsed_url.netloc or parsed_url.scheme:
                    external.add(url)
                    continue
                report["local_image_references"] += 1
                local = (root / unquote(parsed_url.path.lstrip("/"))
                         if parsed_url.path.startswith("/") else page.parent / unquote(parsed_url.path))
                local = local.resolve()
                if not local.is_relative_to(root) or not local.is_file():
                    report["missing_local_files"].append({"page": rel, "url": url})
    report["external_image_urls"] = sorted(external)
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        status = "FAIL" if report["missing_local_files"] else "PASS"
        print(f"{status}: {len(pages)} HTML pages, {report['image_elements']} image elements, "
              f"{report['local_image_references']} local image/picture/srcset references; "
              f"{len(report['missing_local_files'])} missing files")
        print(f"REVIEW: {len(report['empty_alt_review'])} empty alt descriptions; "
              f"{len(report['empty_image_sources'])} empty image sources; "
              f"{len(external)} external URLs (not fetched)")
        for item in report["missing_local_files"]:
            print(f"  {item['page']}: {item['url']}")
    if report["missing_local_files"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
