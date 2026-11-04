#!/usr/bin/env python3
"""Draw the profile README's repo bands as SVG: one slim black band per repo, name and link.

An SVG shown through <img> cannot load web fonts, so each file embeds a subset of the
fonts holding only the characters it uses. Geist and Geist Mono are SIL OFL 1.1; pass a
folder holding Geist-SemiBold.ttf and GeistMono-Medium.ttf (static weights, from the
`geist` npm package or Google Fonts):

    python tools/build_assets.py --fonts DIR

Needs fonttools and brotli. Writes assets/repos/<id>.svg. A black band with a hairline edge
and blue accents reads on both GitHub themes, so there is one file per repo.
"""

import argparse
import base64
import io
from pathlib import Path
from xml.sax.saxutils import escape

from fontTools import subset
from fontTools.ttLib import TTFont

BAND = '#161b22'
EDGE = '#30363d'
INK = '#e6edf3'
BLUE = '#58a6ff'
BAR = '#2f81f7'

REPOS = [
    dict(id='metaorcha', name='metaorcha', dest='solvent-labs-org/metaorcha'),
    dict(id='seamkit', name='seamkit', dest='azank1/seamkit'),
    dict(id='agent-check', name='agent-check', dest='azank1/agent-exposure'),
    dict(id='guardrails-kit', name='guardrails-kit', dest='azank1/guardrails-kit'),
    dict(id='cdv', name='conservative-dual-verify', dest='azank1/cdv'),
]


class Face:
    """One static font weight: measures text and hands out per-file subsets."""

    def __init__(self, path: Path, family: str, weight: int):
        self.data = path.read_bytes()
        font = TTFont(io.BytesIO(self.data), recalcTimestamp=False)
        self.cmap, self.hmtx, self.upm = font.getBestCmap(), font['hmtx'], font['head'].unitsPerEm
        self.family, self.weight = family, weight

    def width(self, text: str, size: float) -> float:
        units = 0
        for ch in text:
            glyph = self.cmap.get(ord(ch))
            if glyph is None:
                raise ValueError(f'{self.family} has no glyph for {ch!r}')
            units += self.hmtx[glyph][0]
        return units * size / self.upm

    def woff2(self, chars: str) -> str:
        font = TTFont(io.BytesIO(self.data), recalcTimestamp=False)
        options = subset.Options()
        options.flavor = 'woff2'
        options.layout_features = ['kern']
        options.name_IDs = ['*']  # keeps the copyright and the OFL notice
        options.hinting = False
        options.notdef_outline = True
        sub = subset.Subsetter(options)
        sub.populate(unicodes=sorted({ord(c) for c in chars} | {0x20}))
        sub.subset(font)
        font.flavor = 'woff2'
        out = io.BytesIO()
        font.save(out)
        return base64.b64encode(out.getvalue()).decode()


def band(sans: Face, mono: Face, n: int, r: dict) -> str:
    W, H, pad = 840, 44, 20
    num, name, dest = f'{n:02d}', r['name'], r['dest']
    name_x = pad + mono.width(num, 12) + 14
    ax = W - pad  # the arrow's top right corner
    if name_x + sans.width(name, 16) + 40 > ax - 14 - mono.width(dest, 12):
        raise ValueError(f'{r["id"]}: the name and the link collide')
    css = (
        f"@font-face{{font-family:G;font-weight:600;src:url(data:font/woff2;base64,{sans.woff2(name)}) format('woff2')}}\n"
        f"@font-face{{font-family:GM;font-weight:500;src:url(data:font/woff2;base64,{mono.woff2(num + dest)}) format('woff2')}}"
    )
    y = 27.5
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="t">
<title id="t">{escape(f"{name}, github.com/{dest}")}</title>
<!-- Type: Geist and Geist Mono, SIL Open Font License 1.1, embedded as subsets. Drawn by tools/build_assets.py. -->
<style>
{css}
</style>
<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="8" fill="{BAND}" stroke="{EDGE}"/>
<rect x="0.5" y="10" width="3" height="{H - 20}" rx="1.5" fill="{BAR}"/>
<text x="{pad}" y="{y}" font-family="GM" font-weight="500" font-size="12" fill="{BLUE}">{num}</text>
<text x="{name_x:g}" y="{y}" font-family="G" font-weight="600" font-size="16" fill="{INK}" letter-spacing="-0.2">{escape(name)}</text>
<text x="{ax - 14}" y="{y}" font-family="GM" font-weight="500" font-size="12" fill="{BLUE}" text-anchor="end">{escape(dest)}</text>
<path d="M{ax - 7} {y - 1.5} L{ax} {y - 8.5} M{ax - 5.5} {y - 8.5} H{ax} V{y - 3}" fill="none" stroke="{BLUE}" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>
</svg>
'''


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--fonts', type=Path, required=True)
    ap.add_argument('--out', type=Path, default=Path(__file__).resolve().parent.parent / 'assets' / 'repos')
    args = ap.parse_args()
    sans = Face(args.fonts / 'Geist-SemiBold.ttf', 'Geist', 600)
    mono = Face(args.fonts / 'GeistMono-Medium.ttf', 'Geist Mono', 500)
    args.out.mkdir(parents=True, exist_ok=True)
    for n, r in enumerate(REPOS, 1):
        p = args.out / f'{r["id"]}.svg'
        p.write_text(band(sans, mono, n, r))
        print(f'{p.name}  {p.stat().st_size / 1024:.1f} KB')


if __name__ == '__main__':
    main()
