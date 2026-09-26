---
name: GUOJIE-HONG
description: Swiss International Typographic Style for a bilingual GitHub profile README, with one International Orange field reserved for skills.
colors:
  international-orange: "#ff4f00"
  on-orange: "#111111"
  ink: "#111111"
  ink-secondary: "#595959"
  ink-dark: "#ffffff"
  ink-secondary-dark: "#9ba4ad"
typography:
  display:
    fontFamily: "Archivo"
    fontSize: "262px"
    fontWeight: 800
    lineHeight: 0.84
    letterSpacing: "-0.035em"
  product:
    fontFamily: "Archivo"
    fontSize: "124px"
    fontWeight: 800
    letterSpacing: "-0.02em"
  headline-hero:
    fontFamily: "Noto Sans TC"
    fontSize: "76px"
    fontWeight: 700
    letterSpacing: "0.02em"
  headline:
    fontFamily: "Noto Sans TC"
    fontSize: "64px"
    fontWeight: 700
    letterSpacing: "0.02em"
  title:
    fontFamily: "Archivo"
    fontSize: "44px"
    fontWeight: 500
    lineHeight: "52px"
    letterSpacing: "0em"
  label:
    fontFamily: "Archivo"
    fontSize: "36px"
    fontWeight: 500
    letterSpacing: "0.14em"
rounded:
  none: "0px"
spacing:
  gutter: "24px"
  column: "146.67px"
  field-inset: "40px"
  heading-rule-gap: "30px"
  heading-label-gap: "22px"
  heading-foot: "14px"
components:
  hero-field:
    backgroundColor: "{colors.international-orange}"
    textColor: "{colors.on-orange}"
    rounded: "{rounded.none}"
    padding: "0 0 0 40px"
    width: "488px"
    height: "522px"
  hero-name:
    textColor: "{colors.ink}"
    typography: "{typography.display}"
  hero-role:
    textColor: "{colors.ink}"
    typography: "{typography.headline-hero}"
  hero-stack-line:
    textColor: "{colors.ink-secondary}"
    typography: "{typography.title}"
  hero-product:
    textColor: "{colors.on-orange}"
    typography: "{typography.product}"
  hero-statement:
    textColor: "{colors.on-orange}"
    typography: "{typography.title}"
  section-rule:
    backgroundColor: "{colors.ink}"
    rounded: "{rounded.none}"
    width: "1000px"
    height: "10px"
  section-rule-skills:
    backgroundColor: "{colors.international-orange}"
    rounded: "{rounded.none}"
    width: "1000px"
    height: "10px"
  section-headline:
    textColor: "{colors.ink}"
    typography: "{typography.headline}"
  english-label:
    textColor: "{colors.ink-secondary}"
    typography: "{typography.label}"
---

# Design System: GUOJIE-HONG

All dimensions are SVG user units on the 1000-unit canvas that `assets/src/build.py` draws. Each SVG declares `width="1000"`, so one unit is one px at its intrinsic size, and README.md scales it to the text column with `width="100%"`. One unit renders at about 0.85px in the 846px desktop column and about 0.33px in the 326px phone column. `build.py` holds the source of truth for every value here. Change it there, rebuild, and update this file.

## Overview

**Creative North Star: "The Information Is the Design"**

The profile is a Swiss International Typographic poster. It uses only the facts about Jacob Hong as material: name, role, stack, the one project, and how to reach him. They sit on a six-column grid in extreme scale contrast. Size, weight and position carry the hierarchy, along with one field of International Orange that marks `skills` as the thing to act on. Nothing else decorates the page.

GitHub's Markdown renderer strips CSS and JavaScript, so the display type, the section headings and the single moment of motion live in generated SVG images. Their text is outlined to paths, and each image ships in a light and a dark variant. Anything a reader should copy, click or search stays native Markdown in GitHub's own type: prose, commands, tables and links. The images have a transparent ground, so GitHub's white or near-black page shows through.

The page is sparse: one poster, then four bilingual section headings, each a thick rule, a Chinese headline and its English translation. This world replaced an earlier pixel-RPG profile and rejects that look outright: no game metaphors, badges, stats cards or typing banners.

**Key Characteristics:**
- Six-column grid on a 1000-unit canvas, flush with the README text column.
- Archivo ExtraBold at poster scale against Archivo Medium in spaced caps; Noto Sans TC Bold for Chinese.
- One orange field, reserved for `skills`.
- Thick rules, square corners, no shadows, no ornament.
- Bilingual: every Chinese headline has its English translation beneath it.
- One moment of motion: the field opens once, and then everything is still.

## Colors

The palette is two inks on the page's own ground plus one spot color, and the spot color carries a single meaning.

### Primary
- **International Orange** (#ff4f00): Used only for `skills`: the hero field behind `skills` and its statement, and the 10-unit rule above the `skills` section heading. It stays the same in both themes. Against GitHub's grounds it measures 3.3:1 (light) and 5.7:1 (dark), so it clears 3:1 for graphical objects in both.
- **Field Ink** (#111111): All text set on orange, in both themes (5.7:1 on the orange).

### Neutral
- **Poster Black** (#111111): Primary ink in the light theme: the name, the Chinese headlines, and the section rules other than `skills` (18.9:1 on GitHub's white).
- **Graphite** (#595959): Secondary ink in the light theme: English labels and the stack line (7.0:1).
- **Paper White** (#ffffff): Primary ink in the dark theme, in the same roles as Poster Black (18.9:1 on GitHub's dark ground).
- **Slate** (#9ba4ad): Secondary ink in the dark theme, in the same roles as Graphite (7.5:1).
- **Ground** (not a token): transparent. GitHub supplies #ffffff in light mode and #0d1117 in dark mode (sampled from the renders). No SVG paints a background.

### Named Rules
**The One Field Rule.** International Orange appears on `skills` and nowhere else. The test: if `skills` were deleted, no orange would be left on the page.

**The Fixed Field Ink Rule.** Text set inside the field is always #111111 and never swaps with the theme. The one crossing is the name's display-scale overprint (see Elevation & Depth), a hero device that does not permit any other text in theme ink on orange.

**The Two-Ink Swap Rule.** The light and dark variants of an SVG differ only in ink: Poster Black becomes Paper White and Graphite becomes Slate. The orange, the Field Ink and the geometry are identical in both.

## Typography

**Display Font:** Archivo ExtraBold (800). No fallback, because it is outlined to paths.
**Text and Label Font:** Archivo Medium (500).
**Chinese Font:** Noto Sans TC Bold (700).
**README prose:** GitHub's own Markdown type, left as GitHub renders it.

**Character:** Archivo is a plain grotesque that suits the Swiss manner. ExtraBold is set tight, so the name reads as one block, and Medium is opened up into spaced caps for the English labels. Noto Sans TC Bold gives Chinese the same weight on the page without imitating the Latin.

### Hierarchy
- **Display** (Archivo 800, 262, line-height 0.84, -0.035em): The name, on two lines. Used in the hero only.
- **Product** (Archivo 800, 124, -0.02em): `skills` inside the field.
- **Headline, hero** (Noto Sans TC 700, 76, +0.02em): The role line 後端工程師.
- **Headline** (Noto Sans TC 700, 64, +0.02em): Every section heading.
- **Title** (Archivo 500, 44, 52 leading, no tracking): The field statement "Evidence, / never guesswork." and, in secondary ink, "C# / ASP.NET Core".
- **Label** (Archivo 500, 36, +0.14em, uppercase): The English line beneath each Chinese headline, BACKEND ENGINEER included. The caps are written into the strings, not produced by a transform.

The ramp runs 262 / 124 / 76 / 64 / 44 / 36, so the name is more than seven times the size of the smallest label. That contrast is intentional.

### Named Rules
**The Outlined Type Rule.** `build.py` shapes every glyph in every SVG with HarfBuzz and outlines it to paths. An image loaded through `<img>` cannot fetch fonts, so no SVG may contain `<text>` or a font reference.

**The Headline-and-Translation Rule.** Every Chinese headline has its English translation directly beneath it in the Label style. The label is always a translation of the headline, never a category tag or a kicker.

**The 36-Unit Floor Rule.** No SVG text is smaller than 36 units. That renders at about 11.7px in a 326px phone column and about 30px on desktop. Anything that would need to be smaller belongs in Markdown text.

## Layout

**Canvas and column.** Every SVG is 1000 units wide and placed with `width="100%"`, so it fills the README text column exactly with no side margin. `build.py` offsets each line's left side bearing so that the ink, not the glyph box, starts at x=0.

**Grid.** There are six columns of 146.67 units with 24-unit gutters. Column left edges fall at 0, 170.67, 341.33, 512, 682.67 and 853.33.

**Vertical measures.** The hero is 760 units tall. Each section heading is 157 units tall: rule from 0 to 10, headline baseline at 96, label baseline at 143, and 14 units below it.

**README rhythm.** The hero is followed by `<br><br>`, and a single `<br>` precedes every section heading. GitHub adds its own `h2` margin and hairline.

**Responsive behavior.** The system has no breakpoints. Each SVG scales uniformly with the column, which is why the 36-unit floor exists. Markdown tables and code blocks reflow or scroll the way GitHub makes them.

**Name span.** The name spans columns 1 to 5: "Jacob" reaches about x=765, and "Hong" ends at about x=653 inside column 4, where its "g" overprints the field.

### Named Rules
**The Flush Column Rule.** Images are exactly as wide as the text column, and their first ink sits at x=0. There is no inner margin to align anything against except the grid.

**The Shared Baseline Rule.** In the hero, the block at bottom left and the lines in the field share baselines at 596, 658 and 710. A new line on either side takes a baseline from that set.

## Elevation & Depth

The system is flat, like print. It has no shadows, gradients, blur or transparency. The only depth is overprint: the field is drawn first and the name is printed over it, so the "g" of "Hong" sits on the orange. Overprint works only at display scale. In the dark theme, the overprinted glyph is Paper White on orange at 3.3:1, which clears 3:1 only because the glyph is display-sized, so no smaller type may cross the field.

### Named Rules
**The Flat Print Rule.** Surfaces are solid ink or solid orange on the page's own ground. If something needs to stand out, change its size, weight or position, not its elevation.

## Shapes

Every shape is a rectangle with square corners (0 radius). Section rules are full-width bars 10 units thick. The field is a rectangle that starts at column 4's left edge and bleeds off the canvas's right and bottom edges. The system has no circles, pills, icons, dividers or frames.

## Components

### Hero Poster
The signature piece is a type poster that states who he is and marks `skills` as the thing to act on (`assets/hero-light.svg`, `assets/hero-dark.svg`, 1000 × 760).
- **Name:** Display type, two lines, flush left, with baselines at 194 and 414.
- **Field:** An orange rectangle from x=512 (column 4), y=238, to the right and bottom edges (488 × 522). Text inside starts 40 units in (x=552).
- **Inside the field:** `skills` in Product type at baseline 596, then "Evidence," and "never guesswork." in Title type at 658 and 710, all in Field Ink.
- **Bottom left, columns 1 to 3:** 後端工程師 in the hero headline style at 596, BACKEND ENGINEER as a Label at 658, and "C# / ASP.NET Core" as a Title in secondary ink at 710.
- **Motion:** The field opens from its left edge, animating from `scaleX(.06)` to full width over 1.2s with `cubic-bezier(.16,1,.3,1)` and fill-mode `both` (`transform-box: fill-box`, `transform-origin: 0 0`). It runs once when the image loads, and it is off under `prefers-reduced-motion: reduce`. The field is never invisible, so a renderer that skips or freezes the animation still shows the composition.
- **Alt text:** One sentence that carries every word in the image.

**The One Moment Rule.** Only the hero field moves, and only once. Nothing loops, and no other asset animates.

### Section Heading
This is a thick rule with a bilingual headline, and it is the page's only way to navigate (`assets/heading-{skills,stack,studying,contact}-{light,dark}.svg`, 1000 × 157).
- **Rule:** A full-width bar 10 units thick, in primary ink. The `skills` heading uses International Orange instead.
- **Headline:** The Chinese title in Headline type, primary ink.
- **Label:** The English translation in Label type, secondary ink.
- **Markup:** `<h2>` wrapping a themed `<picture>`, so the document keeps its outline. On the `skills` heading, the `<a>` to the repo sits inside the `<h2>`.
- **Alt text:** The Chinese headline followed by the English label in sentence case, for example "開發流程工具 Skills for coding agents".
- **States:** None of the system's own, because GitHub strips CSS. Links get GitHub's default focus and hover.

### Themed Picture
This is the mechanism behind every image.
- `<picture>` holds `<source media="(prefers-color-scheme: dark)" srcset="…-dark.svg">` plus `<img src="…-light.svg" width="100%" alt="…">`. GitHub wraps it in `<themed-picture>`.
- The HTML block must begin with a block-level tag, either `<picture>` itself or `<h2>`. A leading inline `<a>` tears the `<source>` out.

### Native Markdown
The system does not style these elements; GitHub renders its defaults.
- Prose, links, tables (the six-stage `skills` pipeline, the stack, current study) and fenced code blocks.

**The Copyable Stays Text Rule.** Anything a reader copies, such as install commands, stays in a fenced Markdown code block and is never drawn into an SVG.

## Do's and Don'ts

### Do:
- **Do** generate every SVG through `assets/src/build.py`. Add strings to `HERO` or `HEADINGS`, then rebuild both themes together.
- **Do** start every new SVG element at a column's left edge (0, 170.67, 341.33, 512, 682.67, 853.33), or at a fixed inset from one, as the field text does (512 + 40).
- **Do** give every new section a heading strip: a 10-unit rule, a Chinese headline, and the English translation in spaced caps beneath it.
- **Do** keep all ink inside the canvas; no glyph may cross the viewBox edge.
- **Do** write alt text that carries every word drawn in the image.
- **Do** keep the ordinal stage numbers in the `skills` table; they are sequence, not metrics.

### Don't:
- **Don't** use International Orange anywhere but `skills`.
- **Don't** set text inside the orange field in theme ink; field text is always #111111, and the name's overprint is the only crossing.
- **Don't** add badges, stats cards, typing banners, or game metaphors (levels, HP bars, quests).
- **Don't** present invented numbers: no percentages, skill levels, counts or progress bars.
- **Don't** add ornament: no icons, emoji, gradients, shadows, rounded corners or decorative dividers. The 10-unit rule is the only line the system draws.
- **Don't** set SVG text smaller than 36 units.
- **Don't** animate anything but the hero field, and don't make it loop.
- **Don't** start an HTML block with an inline `<a>` in front of a `<picture>`; put the link inside the `<h2>`.
- **Don't** paint a background into an SVG; the ground belongs to GitHub.
