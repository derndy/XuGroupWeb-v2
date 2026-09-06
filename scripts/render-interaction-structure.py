#!/usr/bin/env python3
"""Render an exact toy comparison of node features and connected-pair products.

Run from any directory; outputs resolve relative to this script's repository.
Only the Python standard library is required. The numbers are illustrative,
not measurements, model scores, or evidence for a physical mechanism.
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/media/frameworks"
INK, MUTED, BLUE, TEAL = "#132d4c", "#40576e", "#245ca8", "#08736c"
FEATURES = (1, 2, 3, 4)
GRAPHS = (
    ("A", ((1, 2), (3, 4)), BLUE),
    ("B", ((1, 3), (2, 4)), TEAL),
)


def text(x, y, value, size=24, color=INK, weight=400, anchor="middle"):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
            f'font-family="Arial, sans-serif" font-size="{size}" '
            f'font-weight="{weight}" fill="{color}">{escape(str(value))}</text>')


def rect(x, y, w, h, fill="white", stroke="#cbd8e8", radius=14):
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
            f'rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>')


def start(w, h):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
        '<title id="title">Same units. Different relationships.</title>',
        '<desc id="desc">Two graphs have the same scalar features, 1, 2, 3 and 4, and the same feature mean, 2.5. Graph A connects 1 to 2 and 3 to 4. Graph B connects 1 to 3 and 2 to 4. The sum of connected-pair products is 14 for A and 11 for B. Illustrative calculation, not measured data.</desc>',
        rect(0, 0, w, h, "#f4f8fc", "#f4f8fc", 18),
    ]


def graph_card(x, y, w, h, name, pairs, color, mobile=False):
    cx = x + w / 2
    gap = 86 if mobile else 100
    top = y + (98 if mobile else 114)
    bottom = top + (106 if mobile else 122)
    coordinates = {1: (cx - gap, top), 2: (cx + gap, top),
                   3: (cx - gap, bottom), 4: (cx + gap, bottom)}
    s = [rect(x, y, w, h), text(cx, y + 42, f"Graph {name}", 27, color, 700)]
    # Lines encode undirected pair membership. No decorative arrowheads or
    # geometric distances are given scientific meaning.
    for a, b in pairs:
        ax, ay = coordinates[a]
        bx, by = coordinates[b]
        s.append(f'<line x1="{ax}" y1="{ay}" x2="{bx}" y2="{by}" stroke="{color}" stroke-width="5"/>')
    for value in FEATURES:
        nx, ny = coordinates[value]
        s.append(f'<circle cx="{nx}" cy="{ny}" r="29" fill="white" stroke="{color}" stroke-width="3"/>')
        s.append(text(nx, ny + 10, value, 30, color, 700))
    formula = " + ".join(f"({a} × {b})" for a, b in pairs)
    score = sum(a * b for a, b in pairs)
    label_y = y + (271 if mobile else 308)
    s.extend([
        text(cx, label_y, "Add connected-pair products", 22, MUTED),
        text(cx, label_y + 38, formula, 27, INK, 600),
        rect(cx - 87, label_y + 57, 174, 52, "#edf4fc" if name == "A" else "#e9f6f3", color, 26),
        text(cx, label_y + 93, f"Result: {score}", 28, color, 700),
    ])
    return s


def render(mobile=False):
    w, h = (440, 1120) if mobile else (960, 700)
    s = start(w, h)
    mean = sum(FEATURES) / len(FEATURES)
    if mobile:
        s.extend([
            rect(16, 16, 408, 144, "#eaf0f9", "#cbd8e8"),
            text(220, 52, "Same feature values", 24, INK, 700),
            text(220, 88, "1, 2, 3, 4", 28),
            text(220, 130, f"Mean in both graphs: {mean}", 24, MUTED),
        ])
        for i, (name, pairs, color) in enumerate(GRAPHS):
            s.extend(graph_card(16, 184 + i * 436, 408, 412, name, pairs, color, True))
        s.append(text(220, 1080, "Toy calculation · No measured data", 21, MUTED))
    else:
        s.extend([
            rect(24, 24, 912, 90, "#eaf0f9", "#cbd8e8"),
            text(480, 60, "Same feature values: 1, 2, 3, 4", 26, INK, 700),
            text(480, 94, f"Feature mean in both graphs: (1 + 2 + 3 + 4) / 4 = {mean}", 24, MUTED),
        ])
        for i, (name, pairs, color) in enumerate(GRAPHS):
            s.extend(graph_card(24 + i * 464, 140, 448, 450, name, pairs, color))
        s.extend([
            text(480, 635, "Connections change what is combined.", 26, INK, 700),
            text(480, 675, "Toy calculation · No measured data", 22, MUTED),
        ])
    s.append('</svg>')
    return "\n".join(s) + "\n"


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for mobile in (False, True):
        target = OUT / f"interaction-structure{'-mobile' if mobile else ''}.svg"
        target.write_text(render(mobile), encoding="utf-8")
        print(target.relative_to(ROOT))
