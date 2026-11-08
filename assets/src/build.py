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
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ASSETS = Path(__file__).resolve().parents[1]
CACHE = Path(__file__).parent / ".cache"

GREEN = "#084435"
YELLOW = "#f8f897"
CREAM = "#f7f8c9"
THEMES = {
    "light": {"ground": GREEN},
    "dark": {"ground": GREEN},
}

# A compact masthead; the six numbered stages express sequence, not metrics.
W = 1000

FACES = {
    "display": ("Barlow Condensed", 800),
    "text": ("Barlow Condensed", 600),
    "zh": ("Noto Sans TC", 700),
}

HERO = {
    "name": "JACOB HONG",
    "role_zh": "後端工程師",
    "role_en": "BACKEND ENGINEER",
    "stack": "C# / ASP.NET Core",
    "alt": "Jacob Hong. 後端工程師, backend engineer, C# / ASP.NET Core. "
    "Skills workflow: 01 Find direction, 02 Interview, 03 Choose, "
    "04 Implement, 05 Refactor, 06 Hand off.",
}

STAGES = ("Find direction", "Interview", "Choose", "Implement", "Refactor", "Hand off")


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

    def width(self, text, size):
        pen = BoundsPen(self.glyphs)
        scale = size / self.upem
        for name, x, y in self.shape(text, size, 0):
            self.glyphs[name].draw(TransformPen(pen, (scale, 0, 0, scale, x, y)))
        return pen.bounds[2] - pen.bounds[0]

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


def hero(f, theme, mobile=False):
    width, top, row_height = (600, 180, 72) if mobile else (W, 90, 46)
    columns = 3 if mobile else 6
    height = top + row_height * (2 if mobile else 1)
    cell = width / columns
    body = [
        f'<rect width="{width}" height="{top}" fill="{theme["ground"]}"/>',
        f'<rect y="{top}" width="{width}" height="{height - top}" fill="{YELLOW}"/>',
    ]

    def text(face, value, x, baseline, size, max_width, color):
        # Fit actual glyph bounds, so a font update cannot clip the masthead.
        size = min(size, size * max_width / f[face].width(value, size))
        body.append(p(f[face].path(value, x, baseline, size), color))

    if mobile:
        text("display", HERO["name"], 24, 111, 124, 552, YELLOW)
        text("zh", HERO["role_zh"], 24, 157, 30, 204, CREAM)
        text("text", HERO["stack"], 265, 157, 35, 311, CREAM)
    else:
        text("display", HERO["name"], 24, 81, 110, 506, YELLOW)
        body.append(f'<rect x="553" y="12" width="2" height="68" fill="{CREAM}"/>')
        text("zh", HERO["role_zh"], 579, 40, 31, 397, CREAM)
        text("text", HERO["stack"], 579, 80, 39, 397, CREAM)

    for i, label in enumerate(STAGES):
        column, row = i % columns, i // columns
        x, y = column * cell, top + row * row_height
        baseline = y + (43 if mobile else 32)
        text("text", f"{i + 1:02}", x + 16, baseline, 25 if mobile else 22, 24, GREEN)
        text("text", label, x + 48, baseline, 28 if mobile else 25, cell - 63, GREEN)
        if column < columns - 1:
            edge = x + cell - 6
            body.append(
                f'<path d="M{edge - 7} {y + 10}L{edge + 5} {y + row_height / 2}'
                f'L{edge - 7} {y + row_height - 10}" fill="none" stroke="{GREEN}" stroke-width="2"/>'
            )
    if mobile:
        body.append(f'<path d="M16 {top + row_height}H584" stroke="{GREEN}" stroke-width="1"/>')
    return svg(width, height, HERO["alt"], "".join(body))


def main():
    texts = {"display": "", "text": "", "zh": ""}
    texts["display"] += HERO["name"]
    texts["text"] += HERO["stack"] + "0123456" + "".join(STAGES)
    texts["zh"] += HERO["role_zh"]
    faces = {k: fetch_face(*FACES[k], texts[k]) for k in FACES}

    for mode, theme in THEMES.items():
        (ASSETS / f"hero-{mode}.svg").write_text(hero(faces, theme), encoding="utf-8")
        (ASSETS / f"hero-mobile-{mode}.svg").write_text(hero(faces, theme, mobile=True), encoding="utf-8")
    print("built", sorted(x.name for x in ASSETS.glob("*.svg")))


if __name__ == "__main__":
    main()
