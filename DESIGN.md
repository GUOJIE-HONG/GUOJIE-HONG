---
name: GUOJIE-HONG
description: Compact works liner notes for Jacob Hong's GitHub profile.
colors:
  deep-green: "#084435"
  pale-yellow: "#f8f897"
  cream: "#f7f8c9"
typography:
  display:
    fontFamily: "Barlow Condensed"
    fontSize: "110px"
    fontWeight: 800
  role:
    fontFamily: "Noto Sans TC"
    fontSize: "31px"
    fontWeight: 700
  stack:
    fontFamily: "Barlow Condensed"
    fontSize: "39px"
    fontWeight: 600
  stage:
    fontFamily: "Barlow Condensed"
    fontSize: "25px"
    fontWeight: 600
rounded:
  none: "0px"
spacing:
  masthead-inset: "24px"
  stage-inset: "16px"
components:
  masthead:
    backgroundColor: "{colors.deep-green}"
    textColor: "{colors.pale-yellow}"
    rounded: "{rounded.none}"
    width: "1000px"
    height: "136px"
  masthead-mobile:
    backgroundColor: "{colors.deep-green}"
    textColor: "{colors.pale-yellow}"
    rounded: "{rounded.none}"
    width: "600px"
    height: "324px"
  stage-strip:
    backgroundColor: "{colors.pale-yellow}"
    textColor: "{colors.deep-green}"
    height: "46px"
---

# Design System: GUOJIE-HONG

## Overview

**Creative North Star: "Works Liner Notes"**

The profile introduces the author and his method together: a compact green name panel sits above six ordered workflow stages on yellow. The name, role and sequence provide the identity. The liner-notes reference describes the layout, not a musical interest or professional claim.

Only the masthead is custom artwork. All introductions, headings, links, commands and tables remain native GitHub Markdown. Existing factual content is preserved. GitHub owns body typography, theme, spacing and link behavior; this repository ships no page CSS or JavaScript.

**Key Characteristics:**

- Deep green and pale yellow fields with cream role text.
- Condensed Latin lettering paired with clear Chinese type.
- A compact desktop masthead and a separate phone composition.
- Six numbered steps convey sequence, not proficiency or metrics.
- Static artwork followed by readable, copyable native content.

## Colors

### Primary

- **Deep Green**: name-panel ground, stage labels and chevrons.
- **Pale Yellow**: name lettering and stage-strip ground.

### Neutral

- **Cream**: role, stack and the desktop separator.

The masthead retains these colors in both light and dark themes. Its surfaces are opaque; the document outside it follows GitHub's theme. Light/dark asset pairs currently have identical artwork. Sidecar tonal ramps are panel-only swatch metadata, not additional colors for the shipped artwork.

## Typography

Barlow Condensed 800 sets JACOB HONG. Barlow Condensed 600 sets the stack and stages; Noto Sans TC 700 sets 後端工程師. `assets/src/build.py` downloads and caches font subsets, shapes them with HarfBuzz, and outlines them with fontTools. SVGs never fetch fonts when displayed.

**The Outlined Type Rule.** Generate visible lettering as SVG paths; keep the complete text equivalent in the image title and README alt text.

Frontmatter sizes are maximum SVG user-unit sizes on the desktop 1000-unit canvas, not browser CSS sizes. The generator fits actual glyph widths to their allotted space. Desktop sizes: name 110, role 31, stack 39, stage label 25, number 22. Phone sizes on a 600-unit canvas: name 124, role 30, stack 35, stage label 28, number 25. Body and heading fonts are supplied by GitHub.

## Layout

Desktop artwork is 1000 × 136: the green panel is 90 units tall, and the six-column yellow strip is 46 units tall. Name begins at x=24; the role and stack begin at x=579, after a separator at x=553.

At viewport widths up to 600px, `<picture>` selects 600 × 324 phone artwork. The name occupies the first row; role and stack share the next. The green panel is 180 units tall. The yellow strip has three columns and two 72-unit rows, read left to right, top to bottom.

Both compositions fill the README content width. Native headings replace the old full-width heading images; artificial `<br>` spacing is removed. Tables and code blocks retain GitHub's native overflow behavior.

## Elevation & Depth

The masthead is flat: no shadows, gradients, textures, or animation. Color fields and type create hierarchy. GitHub may supply its own borders and rounded code blocks in the body.

## Shapes

The masthead uses square rectangles, one desktop separator, and small chevrons between stages. On phones, a thin rule separates the two stage rows. Chevrons express sequence; they are not buttons.

## Components

### Responsive masthead

`assets/hero-{light,dark}.svg` and `assets/hero-mobile-{light,dark}.svg` are built together. Phone-dark and phone-light sources precede the desktop-dark source and desktop-light fallback. All variants carry the same complete description in `<title>`; README image alt text repeats the name, role, stack and all six stages.

### Native content

Four bilingual level-two headings retain the document outline. The skills heading links to the project. Both installation methods remain fenced text blocks. The skill listing, stack table, study table, email and About links stay editable Markdown. The masthead illustrates the development workflow; the listing includes only the stages with featured skills and need not cover all six stages.

**The Copyable Stays Text Rule.** Installation commands remain fenced Markdown text so readers can select and copy them.

## Do's and Don'ts

- **Do** edit `assets/src/build.py` and rebuild all four SVGs together.
- **Do** keep the name, role, sequence and alt text synchronized.
- **Do** check both phone and desktop compositions in light and dark previews.
- **Do** preserve native copyable commands and factual content.
- **Don't** reintroduce the orange poster, oversized section images or artificial blank rows.
- **Don't** turn the workflow strip into fake controls or a proficiency meter.
- **Don't** embed external fonts, scripts or image dependencies in the SVGs.
- **Don't** treat local GitHub-like preview CSS as a shipping design asset or proof of live GitHub rendering.
