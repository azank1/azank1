#!/usr/bin/env python3
"""Draw the profile README's work cards as SVG, in a light and a dark version.

An SVG shown through <img> cannot load web fonts, so each file embeds a subset of the
fonts holding only the characters it uses. Geist and Geist Mono are SIL OFL 1.1; take the
latin woff2 of each from Google Fonts and pass their folder:

    python tools/build_assets.py --fonts DIR    # DIR holds geist.woff2 and geistmono.woff2

Needs fonttools and brotli. Writes assets/cards/<id>-{dark,light}.svg. Card copy lives in
CARDS below; keep it in step with the portfolio (src/data/projects.ts in azank1/portfolio).
"""

import argparse
import base64
import io
from pathlib import Path
from xml.sax.saxutils import escape

from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

THEMES = {
    'dark': dict(bg='#181818', edge='#ffffff', edge_a=0.09, ink='#e4e4e4', accent='#ff5f1f', accent_text='#ff8a50', ok='#4ade80'),
    'light': dict(bg='#fbfbfa', edge='#171717', edge_a=0.10, ink='#171717', accent='#ff5f1f', accent_text='#c2410c', ok='#15803d'),
}


class Face:
    """One static weight of a font: measures text and hands out per-file subsets."""

    def __init__(self, path: Path, family: str, wght: int):
        font = TTFont(path, recalcTimestamp=False)  # same input, same bytes: no build time in the font
        if 'fvar' in font:
            font = instantiateVariableFont(font, {'wght': wght}, updateFontNames=False)
        buf = io.BytesIO()
        font.save(buf)
        self.data = buf.getvalue()
        self.cmap = font.getBestCmap()
        self.hmtx = font['hmtx']
        self.upm = font['head'].unitsPerEm
        self.family, self.weight = family, wght

    def width(self, text: str, size: float, tracking: float = 0.0) -> float:
        units = 0
        for ch in text:
            glyph = self.cmap.get(ord(ch))
            if glyph is None:
                raise ValueError(f'{self.family} {self.weight} has no glyph for {ch!r}')
            units += self.hmtx[glyph][0]
        return units * size / self.upm + tracking * size * len(text)

    def woff2(self, chars: set[str]) -> str:
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


class Doc:
    """An SVG under construction that remembers which characters each face draws."""

    def __init__(self, faces: dict[str, Face], theme: dict):
        self.faces, self.t = faces, theme
        self.used: dict[str, set[str]] = {k: set() for k in faces}

    def text(self, x, y, s, face='sans', size=14, fill=None, alpha=1.0, anchor='start', tracking=0.0):
        self.used[face].update(s)
        f = self.faces[face]
        fam = 'G' if face.startswith('sans') else 'GM'
        attrs = [f'x="{x:g}"', f'y="{y:g}"', f'font-family="{fam}"', f'font-weight="{f.weight}"', f'font-size="{size:g}"']
        attrs.append(f'fill="{fill or self.t["ink"]}"')
        if alpha < 1:
            attrs.append(f'fill-opacity="{alpha:g}"')
        if anchor != 'start':
            attrs.append(f'text-anchor="{anchor}"')
        if tracking:
            attrs.append(f'letter-spacing="{tracking * size:.2f}"')
        return f'<text {" ".join(attrs)}>{escape(s)}</text>'

    def fonts_css(self) -> str:
        rules = []
        for key, face in self.faces.items():
            if not self.used[key]:
                continue
            fam = 'G' if key.startswith('sans') else 'GM'
            rules.append(
                f"@font-face{{font-family:{fam};font-weight:{face.weight};"
                f"src:url(data:font/woff2;base64,{face.woff2(self.used[key])}) format('woff2')}}"
            )
        return '\n'.join(rules)


def wrap(face: Face, text: str, size: float, max_width: float) -> list[str]:
    lines, line = [], ''
    for word in text.split():
        trial = f'{line} {word}'.strip()
        # 3% headroom for kerning the measurement does not see
        if face.width(trial, size) * 1.03 <= max_width or not line:
            line = trial
        else:
            lines.append(line)
            line = word
    lines.append(line)
    return lines


def arrow(x, y, color, alpha=1.0, size=7):
    """A small north east arrow whose top right corner sits at (x, y)."""
    a = f' stroke-opacity="{alpha:g}"' if alpha < 1 else ''
    return (
        f'<path d="M{x - size:g} {y + size:g} L{x:g} {y:g} M{x - size + 1.5:g} {y:g} H{x:g} V{y + size - 1.5:g}" '
        f'fill="none" stroke="{color}"{a} stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/>'
    )


def shell(doc: Doc, w: int, h: int, title: str, desc: str, style: str, body: str, rx: int) -> str:
    t = doc.t
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">
<title id="t">{escape(title)}</title>
<desc id="d">{escape(desc)}</desc>
<!-- Type: Geist and Geist Mono, SIL Open Font License 1.1, embedded as subsets. Drawn by tools/build_assets.py. -->
<style>
{doc.fonts_css()}
{style}
</style>
<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="{rx}" fill="{t["bg"]}" stroke="{t["edge"]}" stroke-opacity="{t["edge_a"]}"/>
{body}
</svg>
'''


# ---------------------------------------------------------------- cards

CARDS = [
    dict(
        id='metaorcha', name='Metaorcha', status='OPEN SOURCE · APACHE 2.0', live='LIVE',
        line='One goal in, a verified multi-agent run out, across MCP, A2A and computer use. Every run leaves a signed receipt that verifies offline.',
        tags='Python · MCP · A2A', dest='metaorcha.ai', url='https://metaorcha.ai/',
    ),
    dict(
        id='production', name='Production harness', status='PRIVATE', live='IN PRODUCTION',
        line='Around three live production CRMs: every change classified by what it can break, rehearsed off production, done only when production shows it.',
        tags='Supabase · Postgres · CI/CD', dest='the method', url='https://azanhyder-port.vercel.app/research/#production',
    ),
    dict(
        id='cdv', name='CDV', status='OPEN SOURCE · RESEARCH PREVIEW',
        line='An agent never grades its own work: a deterministic floor and an LLM critic score each step, the stricter wins, and a Bayesian loop decides when to stop.',
        tags='Python · MCP · Bayesian', dest='azank1/cdv', url='https://github.com/azank1/cdv',
    ),
    dict(
        id='code-desks', name='Code Desks', status='OPEN SOURCE · MIT',
        line='Run an office of AI coding sessions from your terminal: named desks, gated handoffs, and a meter that reads what each desk really used.',
        tags='Python · CLI · telemetry', dest='azank1/code-desk-cli', url='https://github.com/azank1/code-desk-cli',
    ),
    dict(
        id='bizopsmap', name='bizopsmap', status='OPEN SOURCE · LOCAL FIRST', live='LIVE',
        line='Layers, lanes, relations and stats for a codebase or a business operation, drawn as one local page with OpenTelemetry on the same map.',
        tags='Node · OpenTelemetry', dest='live preview', url='https://bizopsmap-preview-nu.vercel.app/',
    ),
    dict(
        id='commit-city', name='commit.city', status='OPEN SOURCE · MIT', live='LIVE',
        line='Swap github.com for commit.city: any user, org or repo becomes a 3D city and a year of commits replays as a time lapse. Press A for the agents.',
        tags='three.js · Vercel · Python', dest='commit.city', url='https://commit.city',
    ),
]


def card_glyph(card_id: str, t: dict) -> str:
    """A small mark per project, drawn in a 44 by 44 box; the accent marks what matters."""
    ink, hot = t['ink'], t['accent']
    line = f'fill="none" stroke="{ink}" stroke-opacity=".42" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"'
    acc = f'fill="none" stroke="{hot}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
    if card_id == 'metaorcha':  # many agents, one verified run
        return (
            f'<path d="M5 8 C18 8 18 22 27 22 M5 22 H27 M5 36 C18 36 18 22 27 22" {line}/>'
            f'<g {line}><circle cx="5" cy="8" r="2.6"/><circle cx="5" cy="22" r="2.6"/><circle cx="5" cy="36" r="2.6"/></g>'
            f'<circle cx="35" cy="22" r="8" {acc}/><path d="M31.4 22.3 L34 24.9 L38.8 19.6" {acc}/>'
        )
    if card_id == 'production':  # the lane
        return (
            f'<path d="M1 22 H43" {line}/>'
            + ''.join(f'<circle cx="{x}" cy="22" r="3.6" fill="{t["bg"]}" stroke="{ink}" stroke-opacity=".42" stroke-width="1.6"/>' for x in (6, 17, 28, 39))
            + f'<rect x="19.5" y="18.5" width="7" height="7" rx="1.8" fill="{hot}"/>'
        )
    if card_id == 'cdv':  # two judges, the stricter score wins
        return (
            f'<rect x="9" y="6" width="10" height="32" rx="2" {line}/><rect x="25" y="17" width="10" height="21" rx="2" {line}/>'
            f'<path d="M3 17 H41" {acc} stroke-dasharray="3 3"/>'
        )
    if card_id == 'code-desks':  # the meter
        bar = 'fill="none" stroke-width="4" stroke-linecap="round"'
        return (
            f'<path d="M4 10 H40" {bar} stroke="{hot}"/>'
            f'<path d="M4 22 H28" {bar} stroke="{ink}" stroke-opacity=".42"/>'
            f'<path d="M4 34 H16" {bar} stroke="{ink}" stroke-opacity=".42"/>'
        )
    if card_id == 'bizopsmap':  # a map with one inferred link
        nodes = [(6, 9), (24, 5), (39, 15), (14, 33), (35, 37)]
        return (
            f'<path d="M6 9 L24 5 L39 15 M6 9 L14 33 L35 37 M24 5 L14 33" {line}/>'
            f'<path d="M39 15 L35 37" {acc} stroke-dasharray="2.5 3"/>'
            + ''.join(f'<circle cx="{x}" cy="{y}" r="3" fill="{t["bg"]}" stroke="{ink}" stroke-opacity=".5" stroke-width="1.6"/>' for x, y in nodes)
        )
    # commit-city: a skyline
    bars = [(3, 16), (11, 27), (19, 19), (27, 36), (35, 11)]
    return ''.join(
        f'<rect x="{x}" y="{40 - h}" width="6" height="{h}" rx="1.2" '
        + (f'fill="{hot}"/>' if h == 36 else f'fill="{ink}" fill-opacity=".22"/>')
        for x, h in bars
    ) + f'<path d="M0 40.5 H44" {line}/>'


def card(faces: dict[str, Face], theme: dict, n: int, c: dict) -> str:
    W, H, pad = 420, 214, 24
    doc = Doc(faces, theme)
    t = theme
    lines = wrap(faces['sans'], c['line'], 14, W - 2 * pad)
    if len(lines) > 3:
        raise ValueError(f'{c["id"]}: the line wraps to {len(lines)} lines; three fit')

    parts = [doc.text(pad, 40, f'{n:02d}', 'mono5', 12, fill=t['accent_text'])]
    x = pad + 28
    if c.get('live'):
        parts.append(f'<circle cx="{x + 3.5}" cy="35.6" r="3.5" fill="{t["ok"]}"/>')
        parts.append(doc.text(x + 13, 40, c['live'], 'mono5', 11, fill=t['ok'], tracking=0.1))
        x += 13 + faces['mono5'].width(c['live'], 11, 0.1) + 10
        parts.append(doc.text(x, 40, '·', 'mono', 11, alpha=0.35))
        x += 14
    parts.append(doc.text(x, 40, c['status'], 'mono', 11, alpha=0.5, tracking=0.1))
    if x + faces['mono'].width(c['status'], 11, 0.1) > W - pad - 54:
        raise ValueError(f'{c["id"]}: the status line runs into the mark')

    parts.append(f'<g transform="translate({W - pad - 44} 22)">{card_glyph(c["id"], t)}</g>')
    parts.append(doc.text(pad - 1, 84, c['name'], 'sans6', 26, tracking=-0.025))
    for i, ln in enumerate(lines):
        parts.append(doc.text(pad, 112 + i * 20, ln, 'sans', 14, alpha=0.68))

    foot = H - 24
    parts.append(f'<path d="M{pad} {foot - 20} H{W - pad}" stroke="{t["ink"]}" stroke-opacity=".08"/>')
    parts.append(doc.text(pad, foot, c['tags'], 'mono', 11, alpha=0.45))
    parts.append(doc.text(W - pad - 14, foot, c['dest'], 'mono5', 11, fill=t['accent_text'], anchor='end'))
    parts.append(arrow(W - pad, foot - 8.5, t['accent_text']))
    if faces['mono'].width(c['tags'], 11) + faces['mono5'].width(c['dest'], 11) + 40 > W - 2 * pad:
        raise ValueError(f'{c["id"]}: the tags and the link collide')

    desc = f'{c["name"]}. {c.get("live", "").title()} {c["status"].title()}. {c["line"]} {c["tags"]}.'
    return shell(doc, W, H, f'{n:02d} {c["name"]}', ' '.join(desc.split()), '', '\n'.join(parts), 16)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--fonts', type=Path, required=True)
    ap.add_argument('--out', type=Path, default=Path(__file__).resolve().parent.parent / 'assets')
    args = ap.parse_args()

    faces = {
        'sans': Face(args.fonts / 'geist.woff2', 'Geist', 400),
        'sans6': Face(args.fonts / 'geist.woff2', 'Geist', 600),
        'mono': Face(args.fonts / 'geistmono.woff2', 'Geist Mono', 400),
        'mono5': Face(args.fonts / 'geistmono.woff2', 'Geist Mono', 500),
    }
    (args.out / 'cards').mkdir(parents=True, exist_ok=True)
    for name, theme in THEMES.items():
        for n, c in enumerate(CARDS, 1):
            (args.out / 'cards' / f'{c["id"]}-{name}.svg').write_text(card(faces, theme, n, c))
    for p in sorted(args.out.rglob('*.svg')):
        print(f'{p.relative_to(args.out)}  {p.stat().st_size / 1024:.1f} KB')


if __name__ == '__main__':
    main()
