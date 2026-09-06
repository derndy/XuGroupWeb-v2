#!/usr/bin/env python3
"""Render a conceptual evidence-choice diagram; no measured data or results."""
from pathlib import Path
from html import escape

OUT = Path('assets/media/frameworks')
OUT.mkdir(parents=True, exist_ok=True)


def render(mobile):
    width, height = (440, 1130) if mobile else (960, 850)
    cx = width / 2
    teal, ink, muted = '#08736c', '#132d4c', '#40576e'
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             '<title id="title">Choose evidence that separates explanations</title>',
             '<desc id="desc">Two explanations fit current observations. Choose a feasible perturbation with differing predictions, measure with controls, and assess the difference against uncertainty. Update the explanations or choose another test if the result remains ambiguous. Conceptual example, not experimental data.</desc>',
             f'<defs><marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10Z" fill="{teal}"/></marker></defs>',
             f'<rect width="{width}" height="{height}" rx="18" fill="#f4f8fc"/>']

    def arrow(path, dashed=False, head=True):
        parts.append(f'<path d="{path}" fill="none" stroke="{teal}" stroke-width="2.5"'+(' marker-end="url(#arrow)"' if head else '')+(' stroke-dasharray="7 5"' if dashed else '')+'/>')

    def node(x, y, w, h, rows, color=teal):
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="white" stroke="{color}" stroke-width="1.6"/>')
        gap=28
        top=y+h/2-(len(rows)-1)*gap/2+7
        for i, row in enumerate(rows):
            parts.append(f'<text x="{x+w/2}" y="{top+i*gap}" text-anchor="middle" font-family="Arial, sans-serif" font-size="{24 if mobile else 22}" font-weight="{650 if i==0 else 400}" fill="{ink if i==0 else muted}">{escape(row)}</text>')

    if mobile:
        # Two alternatives stay side by side while the decision spine is vertical.
        node(55,24,330,80,['Current observations'])
        arrow('M220 104 V124 H112 V145');arrow('M220 124 H328 V145')
        node(17,153,190,108,['Explanation A','Fits what','we know'])
        node(233,153,190,108,['Explanation B','Fits what','we know'])
        arrow('M112 261 V288 H220 V315');arrow('M328 261 V288 H220', head=False)
        node(55,323,330,108,['Choose a perturbation','Feasible test with','different predictions'])
        arrow('M220 431 V453 H112 V480');arrow('M220 453 H328 V480')
        node(17,488,190,108,['Prediction A','Expected','response A'])
        node(233,488,190,108,['Prediction B','Expected','response B'])
        arrow('M112 596 V622 H220 V649');arrow('M328 596 V622 H220', head=False)
        node(55,657,330,108,['Measure with controls','Compare differences','against uncertainty'])
        arrow('M220 765 V796 H112 V827');arrow('M220 796 H328 V827')
        node(17,835,190,135,['Informative','Reweight','the competing','explanations'])
        node(233,835,190,135,['Ambiguous','Revise or','choose the','next test'], '#7142a5')
        parts.append(f'<text x="220" y="1030" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" fill="{muted}">Either outcome informs the next choice.</text>')
        parts.append(f'<text x="220" y="1070" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" fill="{muted}">Conceptual example · No measured data</text>')
    else:
        node(300,20,360,64,['Current observations'])
        arrow('M480 84 V100 H210 V116');arrow('M480 100 H750 V116')
        node(60,124,300,84,['Explanation A','Fits what we know'])
        node(600,124,300,84,['Explanation B','Fits what we know'])
        arrow('M210 208 V231 H480 V252');arrow('M750 208 V231 H480', head=False)
        node(230,260,500,88,['Choose a feasible perturbation','Predictions differ between explanations'])
        arrow('M480 348 V370 H210 V391');arrow('M480 370 H750 V391')
        node(60,399,300,84,['Prediction A','Expected response A'])
        node(600,399,300,84,['Prediction B','Expected response B'])
        arrow('M210 483 V505 H480 V526');arrow('M750 483 V505 H480', head=False)
        node(230,534,500,88,['Measure with controls','Compare differences against uncertainty'])
        arrow('M480 622 V645 H210 V666');arrow('M480 645 H750 V666')
        node(35,674,350,100,['Informative','Reweight competing','explanations'])
        node(575,674,350,100,['Still ambiguous','Revise or choose','the next test'], '#7142a5')
        parts.append(f'<text x="480" y="799" text-anchor="middle" font-family="Arial, sans-serif" font-size="22" fill="{muted}">Either outcome informs the next choice.</text>')
        parts.append(f'<text x="480" y="832" text-anchor="middle" font-family="Arial, sans-serif" font-size="18" fill="{muted}">Conceptual example · No measured data</text>')
    parts.append('</svg>')
    (OUT / ('evidence-choice-mobile.svg' if mobile else 'evidence-choice.svg')).write_text('\n'.join(parts)+'\n')


if __name__ == '__main__':
    render(False)
    render(True)
