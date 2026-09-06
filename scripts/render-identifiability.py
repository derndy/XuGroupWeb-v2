#!/usr/bin/env python3
"""Render an exact linear example; these are not experimental observations."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INK, BLUE, TEAL = '#132d4c', '#245ca8', '#08736c'

def text(x, y, label, size=22, color=INK, weight=400):
    return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{size}" font-weight="{weight}" text-anchor="middle" fill="{color}">{escape(str(label))}</text>'

def line(x1, y1, x2, y2, color, width=2, dash=''):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-dasharray="{dash}"/>'

def panel(x, y, w, second=False):
    s = [f'<rect x="{x}" y="{y}" width="{w}" height="470" rx="14" fill="white" stroke="#cbd8e8"/>']
    cx = x + w/2
    s.append(text(cx,y+38,'Two measurements' if second else 'One measurement',24,INK,700))
    s.append(text(cx,y+72,'a + b = 4; a − b = 2' if second else 'a + b = 4',24,BLUE,600))
    left, bottom, unit = x+66, y+360, 62
    def xy(a,b): return left+a*unit,bottom-b*unit
    for k in range(5):
        s.extend([line(*xy(k,0),*xy(k,4),'#e0e7f0',1),line(*xy(0,k),*xy(4,k),'#e0e7f0',1)])
        s.extend([text(left+k*unit,bottom+26,k,19),text(left-18,bottom-k*unit+6,k,19)])
    s.extend([line(*xy(0,0),*xy(4.25,0),INK),line(*xy(0,0),*xy(0,4.25),INK)])
    s.extend([text(left+4.5*unit,bottom+7,'a',24),text(left-22,bottom-4.22*unit,'b',24)])
    s.append(line(*xy(0,4),*xy(4,0),BLUE,4))
    if second:
        s.append(line(*xy(2,0),*xy(4,2),TEAL,4,'9 6'))
        px,py=xy(3,1)
        s.append(f'<circle cx="{px}" cy="{py}" r="8" fill="{INK}" stroke="white" stroke-width="2"/>')
        s.append(text(px+58,py+7,'(3, 1)',22,INK,700))
        s.append(text(cx,y+427,'One intersection: (3, 1)',23,TEAL,700))
    else:
        for a,b in [(1,3),(2,2),(3,1)]:
            px,py=xy(a,b)
            s.append(f'<circle cx="{px}" cy="{py}" r="7" fill="white" stroke="{BLUE}" stroke-width="3"/>')
        s.append(text(cx,y+418,'Every point on the blue line fits.',21,INK,600))
        s.append(text(cx,y+451,'Three example pairs are marked.',20))
    return s

def render(mobile=False):
    w,h=(440,1120) if mobile else (960,700)
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
       '<title id="title">A good fit need not identify a unique explanation.</title>',
       '<desc id="desc">For a and b between zero and four, the exact measurement a plus b equals four leaves a line of possible pairs. Adding the independent exact measurement a minus b equals two leaves the unique intersection (3,1). Illustrative linear model with exact measurements, not experimental evidence.</desc>',
       f'<rect width="{w}" height="{h}" rx="18" fill="#f4f8fc"/>']
    if mobile:
        s.append(text(220,36,'What can the data identify?',25,INK,700))
        s.extend(panel(16,58,408)); s.extend(panel(16,548,408,True))
        s.extend([text(220,1060,'Exact linear example',22),text(220,1094,'Not measured data',21)])
    else:
        s.extend([text(480,52,'A good fit is not always a unique answer.',30,INK,700),text(480,91,'The second measurement adds a different constraint.',24)])
        s.extend(panel(24,120,448)); s.extend(panel(488,120,448,True))
        s.extend([text(480,638,'Blue solid: sum constraint · Green dashed: difference constraint',23),text(480,677,'Exact linear example · Not measured data',22)])
    return '\n'.join(s+['</svg>'])+'\n'

if __name__ == '__main__':
    out=ROOT/'assets/media/frameworks'
    for mobile in (False,True):
        p=out/f"identifiability{'-mobile' if mobile else ''}.svg"
        p.write_text(render(mobile),encoding='utf-8')
        print(p.relative_to(ROOT))
