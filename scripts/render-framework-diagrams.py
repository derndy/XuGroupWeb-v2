#!/usr/bin/env python3
"""Render editable conceptual diagrams from the canonical Pillar node labels.

Run from the repository root; requires PyYAML. No external images or results.
"""
from pathlib import Path
from html import escape
import textwrap
import yaml

OUT = Path('assets/media/frameworks')
OUT.mkdir(parents=True, exist_ok=True)
PILLARS = yaml.safe_load(Path('data/research_system.yml').read_text())['pillars']
COLORS = ['#165db5', '#08736c', '#7142a5']
NOTES = [
    'Representation, interactions and learning are co-designed.',
    'Results inform the next evidence choice.',
    'Stress tests can lead us to revisit assumptions.',
]


def render(pillar, index, mobile):
    color = COLORS[index]
    width, height = (400, 900) if mobile else (900, 460)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             f'<title id="title">{escape(pillar["detail"]["architecture"]["title"])}</title>',
             f'<desc id="desc">{escape(NOTES[index])} Conceptual framework, not an experimental result.</desc>',
             f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M 0 0 L 10 5 L 0 10 z" fill="{color}"/></marker></defs>',
             f'<rect width="{width}" height="{height}" rx="20" fill="#f4f8fc"/>']

    def line(path, both=False, dashed=False):
        parts.append(f'<path d="{path}" fill="none" stroke="{color}" stroke-width="2.5" marker-end="url(#arrow)"' + (' marker-start="url(#arrow)"' if both else '') + (' stroke-dasharray="7 5"' if dashed else '') + '/>')

    def text(x, y, value, size=20, fill='#132d4c', weight=600, wrap=22):
        rows = textwrap.wrap(value, wrap)
        parts.append(f'<text x="{x}" y="{y}" text-anchor="middle" fill="{fill}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}">')
        for n, row in enumerate(rows):
            parts.append(f'<tspan x="{x}" dy="{0 if n == 0 else 25}">{escape(row)}</tspan>')
        parts.append('</text>')

    def node(x, y, n, w=220):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="96" rx="12" fill="white" stroke="{color}" stroke-width="1.5"/>')
        parts.append(f'<circle cx="{x+22}" cy="{y+22}" r="12" fill="{color}"/>')
        text(x+22, y+27, str(n+1), 14, 'white', 700)
        label = pillar['detail']['architecture']['nodes'][n]['label']
        text(x+w/2, y+49, label, wrap=16 if w == 220 else 18)

    if mobile:
        ys = [40, 200, 360, 520, 680]
        if index == 0:
            parts.append('<rect x="42" y="182" width="316" height="450" rx="18" fill="#e8f0fc"/>')
        for n in range(4):
            line(f'M 200 {ys[n]+96} V {ys[n+1]-8}', both=index == 0 and n in (1, 2))
        if index == 1:
            line('M 330 728 H 373 V 88 H 338', dashed=True)
        if index == 2:
            line('M 330 568 H 373 V 248 H 338', dashed=True)
        for n, y in enumerate(ys):
            node(70, y, n, 260)
        text(200, 827, NOTES[index], 20, wrap=30)
    elif index == 0:
        parts.append('<rect x="36" y="162" width="828" height="146" rx="18" fill="#e8f0fc"/>')
        for x in (170, 450, 730):
            line(f'M 450 124 V 144 H {x} V 180')
            line(f'M {x} 286 V 328 H 450 V 348')
        line('M 289 238 H 331', both=True)
        line('M 569 238 H 611', both=True)
        node(340, 28, 0)
        for n, x in enumerate((60, 340, 620), 1):
            node(x, 190, n)
        node(340, 356, 4)
        text(735, 69, 'Joint design', 23, color)
    else:
        positions = [(40, 36), (340, 36), (640, 36), (640, 316), (40, 316)]
        line('M 260 84 H 332')
        line('M 560 84 H 632')
        line('M 750 132 V 308')
        line('M 640 364 H 268')
        if index == 1:
            line('M 150 316 V 140', dashed=True)
        else:
            line('M 640 342 H 450 V 140', dashed=True)
        for n, (x, y) in enumerate(positions):
            node(x, y, n)
        text(450 if index == 1 else 260, 212, 'Evidence informs the next choice' if index == 1 else 'Revisit assumptions', 23, color, wrap=25)
        if index == 2:
            text(260, 267, 'Dashed path: feedback from stress tests', 18, '#40576e', 400, wrap=30)
    parts.append('</svg>')
    suffix = '-mobile' if mobile else ''
    (OUT / f'{pillar["id"]}{suffix}.svg').write_text('\n'.join(parts) + '\n')


for i, pillar in enumerate(PILLARS):
    for mobile in (False, True):
        render(pillar, i, mobile)
