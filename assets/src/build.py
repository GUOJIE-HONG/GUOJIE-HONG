"""Build the README's SVG assets.

GitHub loads SVG through <img>, which cannot fetch web fonts, so every line of
text is shaped with HarfBuzz and outlined to paths. Each image ships in a light
and a dark variant; README.md picks one with <picture>.

    pip install fonttools brotli uharfbuzz
    python assets/src/build.py
"""

import hashlib
import io
import re
import urllib.parse
import urllib.request
from pathlib import Path

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ASSETS = Path(__file__).resolve().parents[1]
CACHE = Path(__file__).parent / ".cache"

ORANGE = "#ff4f00"
ON_ORANGE = "#111111"
THEMES = {
    "light": {"ink": "#111111", "sub": "#595959"},
    "dark": {"ink": "#ffffff", "sub": "#9ba4ad"},
}

# Six-column grid on a 1000-unit canvas, flush with the README's text column.
W = 1000
GUTTER = 24
COL = (W - 5 * GUTTER) / 6


def col(i):
    """Left edge of column i (0-based)."""
    return i * (COL + GUTTER)


# The English line under every Chinese headline: spaced caps, one treatment.
LABEL_SIZE = 36
LABEL_TRACKING = 0.14

FACES = {
    "display": ("Archivo", 800),
    "text": ("Archivo", 500),
    "zh": ("Noto Sans TC", 700),
}

HERO = {
    "name": ("Jacob", "Hong"),
    "role_zh": "後端工程師",
    "role_en": "BACKEND ENGINEER",
    "stack": "C# / ASP.NET Core",
    "product": "skills",
    "rule": ("Evidence,", "never guesswork."),
    "alt": "Jacob Hong. 後端工程師, backend engineer, C# / ASP.NET Core. "
    "skills: evidence, never guesswork.",
}

HEADINGS = {
    "skills": ("開發流程工具", "SKILLS FOR CODING AGENTS", True),
    "stack": ("技術", "STACK", False),
    "studying": ("正在研究", "CURRENTLY STUDYING", False),
    "contact": ("聯絡", "CONTACT", False),
}


def fetch_face(family, weight, text):
    """Download a Google Fonts subset holding exactly the glyphs in `text`."""
    chars = "".join(sorted(set(text)))
    key = hashlib.sha1(f"{family}|{weight}|{chars}".encode()).hexdigest()[:16]
    path = CACHE / f"{key}.ttf"
    if not path.exists():
        query = urllib.parse.urlencode(
            {"family": f"{family}:wght@{weight}", "text": chars}
        )
        css = urllib.request.urlopen(
            f"https://fonts.googleapis.com/css2?{query}"
        ).read().decode()
        url = re.search(r"url\((https://[^)]+)\)", css).group(1)
        CACHE.mkdir(exist_ok=True)
        path.write_bytes(urllib.request.urlopen(url).read())
    return Face(path.read_bytes())


class Face:
    def __init__(self, data):
        self.tt = TTFont(io.BytesIO(data))
        self.upem = self.tt["head"].unitsPerEm
        self.hb = hb.Font(hb.Face(data))
        self.glyphs = self.tt.getGlyphSet()
        self.order = self.tt.getGlyphOrder()

    def shape(self, text, size, tracking):
        buf = hb.Buffer()
        buf.add_str(text)
        buf.guess_segment_properties()
        hb.shape(self.hb, buf, {"kern": True, "liga": True})
        s = size / self.upem
        placed, x = [], 0.0
        for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
            placed.append((self.order[info.codepoint], x + pos.x_offset * s, pos.y_offset * s))
            x += pos.x_advance * s + tracking * size
        return placed

    def path(self, text, x, y, size, tracking=0.0):
        """Outline `text` with its baseline at y and its first ink at x."""
        placed = self.shape(text, size, tracking)
        s = size / self.upem
        x -= self.tt["hmtx"][placed[0][0]][1] * s  # flush the ink, not the side bearing
        pen = SVGPathPen(self.glyphs, ntos=lambda v: f"{v:.1f}".rstrip("0").rstrip("."))
        for name, gx, gy in placed:
            self.glyphs[name].draw(TransformPen(pen, (s, 0, 0, -s, x + gx, y - gy)))
        return pen.getCommands()

    def cap(self, size):
        return self.tt["OS/2"].sCapHeight * size / self.upem

    def top(self, text, size):
        """Height of the tallest ink in `text` above the baseline."""
        glyf = self.tt["glyf"]
        names = [name for name, _, _ in self.shape(text, size, 0)]
        return max(glyf[n].yMax for n in names) * size / self.upem


def svg(width, height, title, body, style=""):
    style = f"<style>{style}</style>" if style else ""
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}" role="img" aria-labelledby="t">'
        f'<title id="t">{title}</title>{style}{body}</svg>\n'
    )


def p(d, fill, cls=""):
    cls = f' class="{cls}"' if cls else ""
    return f'<path{cls} fill="{fill}" d="{d}"/>'


# The field opens once from a column-wide rule; it is never invisible, so a
# renderer that skips or freezes the animation still shows the composition.
MOTION = (
    ".field{transform-box:fill-box;transform-origin:0 0;"
    "animation:open 1.2s cubic-bezier(.16,1,.3,1) both}"
    "@keyframes open{from{transform:scaleX(.06)}}"
    "@media (prefers-reduced-motion:reduce){.field{animation:none}}"
)


def hero(f, theme):
    ink, sub = theme["ink"], theme["sub"]
    name_size = 262
    lead = name_size * 0.84
    y_jacob = round(f["display"].top(HERO["name"][0], name_size)) + 4
    y_hong = round(y_jacob + lead)
    field_top = y_jacob + 44
    height = 760

    # Inside the orange field: columns 4-6.
    fx = col(3) + 40
    y_product = 596
    product_size = 124
    rule_size = 44
    y_rule = (y_product + 62, y_product + 62 + 52)

    # Bottom left: columns 1-3, baselines shared with the field's lines.
    zh_size = 76

    body = [
        f'<rect class="field" x="{col(3):.1f}" y="{field_top}" '
        f'width="{W - col(3):.1f}" height="{height - field_top}" fill="{ORANGE}"/>',
        p(f["display"].path(HERO["name"][0], 0, y_jacob, name_size, -0.035), ink),
        p(f["display"].path(HERO["name"][1], 0, y_hong, name_size, -0.035), ink),
        p(f["zh"].path(HERO["role_zh"], 0, y_product, zh_size, 0.02), ink),
        p(f["text"].path(HERO["role_en"], 0, y_rule[0], LABEL_SIZE, LABEL_TRACKING), sub),
        p(f["text"].path(HERO["stack"], 0, y_rule[1], rule_size), sub),
        p(f["display"].path(HERO["product"], fx, y_product, product_size, -0.02), ON_ORANGE),
        p(f["text"].path(HERO["rule"][0], fx, y_rule[0], rule_size), ON_ORANGE),
        p(f["text"].path(HERO["rule"][1], fx, y_rule[1], rule_size), ON_ORANGE),
    ]
    return svg(W, height, HERO["alt"], "".join(body), MOTION)


def heading(f, theme, zh, en, accent):
    ink, sub = theme["ink"], theme["sub"]
    rule = ORANGE if accent else ink
    zh_size = 64
    y_zh = 10 + 30 + round(zh_size * 0.88)
    y_en = y_zh + 22 + round(f["text"].cap(LABEL_SIZE))
    height = y_en + 14
    body = (
        f'<rect width="{W}" height="10" fill="{rule}"/>'
        + p(f["zh"].path(zh, 0, y_zh, zh_size, 0.02), ink)
        + p(f["text"].path(en, 0, y_en, LABEL_SIZE, LABEL_TRACKING), sub)
    )
    return svg(W, height, f"{zh} {en.capitalize()}", body)


def main():
    texts = {"display": "", "text": "", "zh": ""}
    texts["display"] += "".join(HERO["name"]) + HERO["product"]
    texts["text"] += HERO["role_en"] + HERO["stack"] + "".join(HERO["rule"])
    texts["zh"] += HERO["role_zh"]
    for zh, en, _ in HEADINGS.values():
        texts["zh"] += zh
        texts["text"] += en
    faces = {k: fetch_face(*FACES[k], texts[k]) for k in FACES}

    for mode, theme in THEMES.items():
        (ASSETS / f"hero-{mode}.svg").write_text(hero(faces, theme), encoding="utf-8")
        for slug, (zh, en, accent) in HEADINGS.items():
            out = ASSETS / f"heading-{slug}-{mode}.svg"
            out.write_text(heading(faces, theme, zh, en, accent), encoding="utf-8")
    print("built", sorted(x.name for x in ASSETS.glob("*.svg")))


if __name__ == "__main__":
    main()
