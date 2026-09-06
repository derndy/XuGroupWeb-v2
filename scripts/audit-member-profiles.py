#!/usr/bin/env python3
"""Audit generated member profiles using only the Python standard library.

Usage: python -B scripts/audit-member-profiles.py BUILD_DIR
This validates generated structure, progressive enhancement and local links. It
does not replace visual browser testing or editorial approval of member copy.
"""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Node:
    def __init__(self, tag="root", attrs=()):
        self.tag = tag
        self.attrs = dict(attrs)
        self.children = []

    def has_class(self, name):
        return name in self.attrs.get("class", "").split()

    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node):
                yield from child.walk()

    def find(self, predicate):
        return [node for node in self.walk() if predicate(node)]

    def text(self):
        return "".join(child.text() if isinstance(child, Node) else child for child in self.children)


class Document(HTMLParser):
    VOID = set("area base br col embed hr img input link meta param source track wbr".split())

    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]
        self.feed(path.read_text(encoding="utf-8"))
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs)
        self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                break

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def require(condition, message):
    if not condition:
        raise SystemExit(f"FAIL: {message}")


def normalized(node):
    return " ".join(node.text().split())


def class_nodes(node, name):
    return node.find(lambda candidate: candidate.has_class(name))


def local_file(build, href):
    path = urlsplit(href).path
    require(path.startswith("/"), f"Expected a root-relative local URL: {href}")
    target = build / unquote(path).lstrip("/")
    if path.endswith("/"):
        target /= "index.html"
    require(target.is_file(), f"Missing built destination: {href}")
    return target


def validate_landmarks_and_references(document, profile_path):
    profiles = document.find(lambda node: node.tag == "main" and node.has_class("person-profile"))
    require(len(profiles) == 1, f"Expected one member-profile main in {profile_path}")
    profile = profiles[0]
    headings = profile.find(lambda node: node.tag == "h1" and node.attrs.get("id") == "person-name")
    require(len(headings) == 1 and normalized(headings[0]), f"Expected one named H1 in {profile_path}")

    document_ids = [node.attrs["id"] for node in document.walk() if "id" in node.attrs]
    profile_ids = [node.attrs["id"] for node in profile.walk() if "id" in node.attrs]
    require(len(document_ids) == len(set(document_ids)), f"Duplicate document IDs in {profile_path}")
    for node in profile.walk():
        require("style" not in node.attrs, f"Unexpected inline style in {profile_path}")
        require(not any(key.startswith("on") for key in node.attrs),
                f"Unexpected inline event handler in {profile_path}")
        for key in ("aria-labelledby", "aria-describedby"):
            require(all(value in document_ids for value in node.attrs.get(key, "").split()),
                    f"Unresolved {key} in {profile_path}")
        if node.tag == "a":
            href = node.attrs.get("href", "")
            require(href, f"Empty link in {profile_path}")
            if href.startswith("#"):
                require(href[1:] in profile_ids, f"Broken profile anchor {href} in {profile_path}")
            elif href.startswith("/"):
                local_file(profile_path.parents[2], href)
    return profile


def validate_profile(build, profile_path):
    document = Document(profile_path).root
    profile = validate_landmarks_and_references(document, profile_path)
    slug = profile_path.parent.name

    portraits = class_nodes(profile, "person-profile__portrait")
    require(len(portraits) == 1, f"Expected one portrait in {slug}")
    images = portraits[0].find(lambda node: node.tag == "img")
    require(len(images) == 1, f"Expected one portrait image in {slug}")
    image = images[0]
    require(image.attrs.get("alt", "").startswith("Portrait of "), f"Missing portrait alt text in {slug}")
    require(image.attrs.get("width", "").isdigit() and int(image.attrs["width"]) > 0,
            f"Missing portrait width in {slug}")
    require(image.attrs.get("height", "").isdigit() and int(image.attrs["height"]) > 0,
            f"Missing portrait height in {slug}")

    back_links = profile.find(
        lambda node: node.tag == "a" and node.attrs.get("href", "").startswith("/people/#")
    )
    require(len(back_links) == 2, f"Expected two directory return links in {slug}")

    body = class_nodes(profile, "person-profile__body")
    require(len(body) == 1, f"Expected one profile body in {slug}")
    main_columns = class_nodes(profile, "person-profile__main")
    if main_columns:
        require(not body[0].has_class("person-profile__body--sidebar-only"),
                f"Content profile incorrectly marked sidebar-only in {slug}")
    else:
        require(body[0].has_class("person-profile__body--sidebar-only"),
                f"Sparse profile did not collapse its empty content column in {slug}")

    selected = class_nodes(profile, "person-profile__selected-work")
    for link in [node for group in selected for node in group.find(lambda item: item.tag == "a")]:
        local_file(build, link.attrs["href"])
    return profile


def validate_prototype(profile):
    expected = {
        "person-profile__headline": 1,
        "person-profile__focus": 1,
        "person-profile__questions": 1,
        "person-profile__work-item": 2,
        "person-profile__capability-grid": 1,
        "person-profile__selected-work": 1,
        "person-profile__collaboration": 1,
    }
    for name, count in expected.items():
        require(len(class_nodes(profile, name)) == count,
                f"Prototype expected {count} {name} module(s)")
    require(len(class_nodes(profile, "person-profile__focus")[0].find(lambda node: node.tag == "li")) == 4,
            "Prototype expected four research focus tags")
    require(len(class_nodes(profile, "person-profile__questions")[0].find(lambda node: node.tag == "li")) == 3,
            "Prototype expected three research questions")
    require(len(class_nodes(profile, "person-profile__selected-work")[0].find(lambda node: node.tag == "li")) == 3,
            "Prototype expected three selected outputs")
    require(not class_nodes(profile, "person-profile__principles"),
            "Unconfirmed working principles must remain absent")
    require(not profile.find(lambda node: node.attrs.get("id") == "person-beyond-research"),
            "Unconfirmed beyond-research copy must remain absent")


def validate_sparse_profile(profile):
    optional = (
        "person-profile__questions", "person-profile__work-item", "person-profile__capability-grid",
        "person-profile__principles", "person-profile__selected-work", "person-profile__collaboration",
    )
    require(all(not class_nodes(profile, name) for name in optional),
            "Sparse profile rendered an empty optional module")
    require(len(class_nodes(profile, "person-profile__sidebar")) == 1,
            "Sparse profile must retain verified facts and contact details")


def validate_directory(build, profile_count):
    directory = Document(build / "people/index.html").root
    mains = directory.find(lambda node: node.tag == "main")
    require(len(mains) == 1, "Expected one main landmark in People directory")
    require(len(mains[0].find(lambda node: node.tag == "h1")) == 1,
            "Expected one H1 in People directory")
    cards = class_nodes(mains[0], "people-card")
    require(len(cards) == profile_count,
            f"People directory has {len(cards)} cards for {profile_count} built profiles")
    destinations = []
    for card in cards:
        links = card.find(lambda node: node.tag == "a" and node.attrs.get("href", "").startswith("/person/"))
        require(links, "People card is missing its member profile link")
        destinations.append(links[0].attrs["href"])
        local_file(build, links[0].attrs["href"])
    require(len(destinations) == len(set(destinations)), "Duplicate member cards in People directory")
    require("/person/pmt/" in destinations, "Prototype member is missing from People directory")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("build", type=Path)
    args = parser.parse_args()
    build = args.build.resolve()
    candidates = sorted((build / "person").glob("*/index.html"))
    profiles = [
        path for path in candidates
        if Document(path).root.find(lambda node: node.tag == "main" and node.has_class("person-profile"))
    ]
    require(profiles, "No generated member profiles found")

    audited = {path.parent.name: validate_profile(build, path) for path in profiles}
    require("pmt" in audited, "Missing Meitang Peng prototype")
    require("gf" in audited, "Missing sparse-profile regression fixture")
    validate_prototype(audited["pmt"])
    validate_sparse_profile(audited["gf"])
    validate_directory(build, len(profiles))
    print(f"PASS: {len(profiles)} member profiles and the People directory; prototype modules, sparse-profile fallback, landmarks, references, portraits, and local links")


if __name__ == "__main__":
    main()
