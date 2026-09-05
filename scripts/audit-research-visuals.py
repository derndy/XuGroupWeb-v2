#!/usr/bin/env python3
"""Check the approved conceptual-image set in a Hugo output directory.

Usage: python -B scripts/audit-research-visuals.py BUILD_DIR [--before BASELINE]
Uses the standard library. This is a file/HTML audit, not a browser layout test.
"""

import argparse
import hashlib
import importlib.util
from pathlib import Path
import struct

spec = importlib.util.spec_from_file_location(
    "publication_audit", Path(__file__).with_name("audit-publications.py")
)
html = importlib.util.module_from_spec(spec)
spec.loader.exec_module(html)
require = html.require

BATCH = (
    ("research/", "CONCEPT-RES-001", "research-overview"),
    ("research/evidence-engineering/", "CONCEPT-RES-002", "pillar-ii-intro"),
    ("research/mathematical-frontiers/", "CONCEPT-RES-003", "pillar-iii-intro"),
    ("about/", "CONCEPT-RES-004", "about-vision"),
    ("", "CONCEPT-RES-005", "home-testbeds"),
    ("contact/", "CONCEPT-RES-006", "join-collaborate"),
)


def webp_dimensions(data):
    require(data[:4] == b"RIFF" and data[8:12] == b"WEBP", "Invalid WebP file")
    offset = 12
    while offset + 8 <= len(data):
        kind = data[offset:offset + 4]
        length = int.from_bytes(data[offset + 4:offset + 8], "little")
        chunk = data[offset + 8:offset + 8 + length]
        if kind == b"VP8 ":
            require(chunk[3:6] == b"\x9d\x01\x2a", "Invalid VP8 frame")
            width, height = struct.unpack("<HH", chunk[6:10])
            return width & 0x3fff, height & 0x3fff
        if kind == b"VP8L":
            require(chunk[0] == 0x2f, "Invalid VP8L frame")
            dimensions = int.from_bytes(chunk[1:5], "little")
            return (dimensions & 0x3fff) + 1, ((dimensions >> 14) & 0x3fff) + 1
        if kind == b"VP8X":
            return int.from_bytes(chunk[4:7], "little") + 1, int.from_bytes(chunk[7:10], "little") + 1
        offset += 8 + length + (length % 2)
    raise SystemExit("FAIL: WebP dimensions not found")


def by_class(root, name):
    return root.find(lambda node: node.has_class(name))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build", type=Path)
    parser.add_argument("--before", type=Path)
    args = parser.parse_args()
    variant_count = 0
    for route, asset_id, placement in BATCH:
        doc = html.Document(args.build / route / "index.html").root
        require(len(doc.find(lambda node: node.tag == "main")) == 1, f"Main landmark: {route}")
        require(len(doc.find(lambda node: node.tag == "h1")) == 1, f"H1: {route}")
        ids = [node.attrs["id"] for node in doc.walk() if "id" in node.attrs]
        require(len(ids) == len(set(ids)), f"Duplicate IDs: {route}")
        figures = doc.find(lambda node: "data-scientific-visual" in node.attrs)
        require(len(figures) == 1, f"Expected one approved illustration: {route}")
        figure = figures[0]
        require(figure.attrs["data-scientific-visual"] == asset_id, f"Wrong asset: {route}")
        require(figure.attrs["data-visual-placement"] == placement, f"Wrong placement: {route}")
        require(not by_class(doc, "governed-figure"), f"Concept must not be presented as result evidence: {route}")
        captions = figure.find(lambda node: node.tag == "figcaption")
        require(len(captions) == 1 and captions[0].attrs["id"] == figure.attrs.get("aria-describedby"), f"Caption association: {route}")
        require("Conceptual illustration · AI-generated" in captions[0].text(), f"Missing conceptual label: {route}")
        for node in figure.walk():
            require("style" not in node.attrs and not any(key.startswith("on") for key in node.attrs), f"Inline style/handler: {route}")
        pictures = figure.find(lambda node: node.tag == "picture")
        images = figure.find(lambda node: node.tag == "img")
        require(len(pictures) == len(images) == 1, f"Picture fallback: {route}")
        image = images[0]
        require(bool(image.attrs.get("alt", "").strip()), f"Missing alt text: {route}")
        require(image.attrs.get("loading") == ("eager" if placement.endswith("-hero") else "lazy"), f"Loading priority: {route}")
        original = html.local_file(args.build, image.attrs["src"])
        data = original.read_bytes()
        require(data[:8] == b"\x89PNG\r\n\x1a\n", f"Missing PNG fallback: {route}")
        width, height = struct.unpack(">II", data[16:24])
        require((int(image.attrs["width"]), int(image.attrs["height"])) == (width, height), f"Intrinsic dimensions: {route}")
        require(hashlib.sha256(data).hexdigest() == figure.attrs["data-approved-sha256"], f"Original differs from approval: {route}")
        downloads = figure.find(lambda node: "data-original-image" in node.attrs)
        require(len(downloads) == 1 and "download" in downloads[0].attrs, f"Direct download missing: {route}")
        require(html.local_file(args.build, downloads[0].attrs["href"]) == original, f"Download target mismatch: {route}")
        sources = pictures[0].find(lambda node: node.tag == "source")
        require(len(sources) == 1 and sources[0].attrs.get("type") == "image/webp" and sources[0].attrs.get("sizes"), f"Responsive source: {route}")
        widths = []
        for candidate in sources[0].attrs["srcset"].split(","):
            href, descriptor = candidate.strip().split()
            require(descriptor.endswith("w"), f"Invalid width descriptor: {route}")
            variant = html.local_file(args.build, href).read_bytes()
            vw, vh = webp_dimensions(variant)
            widths.append(vw)
            require(vw == int(descriptor[:-1]) and vw <= width, f"Unexpected derivative width: {route}")
            require(abs(vh - height * vw / width) <= 1, f"Cropped/stretched derivative: {route}")
            require(len(variant) < len(data), f"Derivative is larger than original: {route}")
            variant_count += 1
        require(widths == [640, 960, 1440, width], f"Missing responsive widths: {route}")

        if args.before and (args.before / route / "index.html").exists():
            old = html.Document(args.before / route / "index.html").root
            require([html.normalized(node) for node in old.find(lambda node: node.tag == "h1")]
                    == [html.normalized(node) for node in doc.find(lambda node: node.tag == "h1")], f"Original title changed: {route}")
            for section in old.find(lambda node: node.tag == "section"):
                section_id = section.attrs.get("id")
                matches = doc.find(lambda node: node.attrs.get("id") == section_id) if section_id else []
                if section_id and section_id != "research-routes-title":
                    require(len(matches) == 1 and html.normalized(matches[0]) == html.normalized(section), f"Original section changed: {route}#{section_id}")
            for name in ("pillar-detail-hero__intro", "pillar-detail-brief", "pillar-architecture"):
                require([html.normalized(node) for node in by_class(old, name)]
                        == [html.normalized(node) for node in by_class(doc, name)], f"Original {name} changed: {route}")

    for route in (
        "research/learning-system-design/",
    ):
        pillar = html.Document(args.build / route / "index.html").root
        require(
            not pillar.find(lambda node: "data-scientific-visual" in node.attrs),
            f"Unapproved conceptual visual on {route}",
        )
    for name in ("research/2.png", "research/4.png", "audit/legacy-research-assets/2.png", "audit/legacy-research-assets/4.png"):
        require(not (args.build / name).exists(), f"Blocked legacy image published: {name}")
    print(f"PASS: {len(BATCH)} approved placements, exact PNG downloads, {variant_count} uncropped WebP variants, labels, landmarks, and legacy exclusion")
    if args.before:
        print("PASS: baseline headings, section content, Pillar introductions/briefs, and semantic architecture maps preserved")


if __name__ == "__main__":
    main()
