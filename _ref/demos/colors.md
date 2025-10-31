<!-- ===========================================================================
@file _ref/demos/colors.md
@date 2025-10-28 01:03 PM CDT
@description
  Centralized visual reference of pastel color swatches used throughout the documentation library.
  Provides functional grouping by UI purpose (documentation, banners, highlights, and labels)
  to ensure styling consistency across all related repositories and projects.

  Serves as a supplemental companion to _ref/shape_lib/index.md, focusing specifically on color theming
  and the relationship between defined design tokens and implemented CSS class applications.
  
  Assumes required CSS is loaded via:
    - ../../_css/main.css for general components and color references

  Includes:
    - Rendered color samples with live previews
    - Associated class and element mappings
    - Optional HTML swatch table templates

  Recommended use:
    Reference within Markdown documentation or exported views (HTML/PDF)
    for maintaining visual consistency across team-shared notes and assets.
@author
  Eric L. Hepperle
=========================================================================== -->

<!-- Custom Stylesheet Reference -->
<link rel="stylesheet" href="../../_css/main.css">
<!-- <link rel="stylesheet" href="../../_css/status-messages.css"> -->

![Site Logo](/_pix/logos/logo-ehw-kb-h32.png)

# 📦 PASTEL COLORS REFERENCE for Boot.dev Course Notes

A structured visual catalog of pastel color swatches and associated UI class references, consolidating reusable styling examples from `main.css`.  Each entry includes rendered previews, class locations, and color associations for consistent design implementation.

## Usage Guidelines

- Use these tables to identify and apply pastel colors consistently across UI components.  
- Reference only defined CSS classes (avoid inline color definitions).  
- Keep examples synchronized with the version of `main.css` used in your project.  
- This document serves as both a visual reference and snippet library for documentation styling.

***

<details open>
  <summary><h2>Table of Contents</h2></summary>

- [📦 PASTEL COLORS REFERENCE for Boot.dev Course Notes](#-pastel-colors-reference-for-bootdev-course-notes)
  - [Usage Guidelines](#usage-guidelines)
    - [Documentation and Tagging](#documentation-and-tagging)
    - [Alerts and Status Banners](#alerts-and-status-banners)
    - [Notes, Callouts, and Highlights](#notes-callouts-and-highlights)
    - [UI Elements and Labels](#ui-elements-and-labels)
      - [Key:](#key)
    - [Section Colors with Names](#section-colors-with-names)
    - [Pastel Section Color Sets](#pastel-section-color-sets)
  - [✅ Revision History](#-revision-history)

</details>

***

<style>
.swatch {
  padding: 4px 16px;
  display: inline-block;
  border: 1px solid #333;
}

.swatch-orig {
  padding: 0.5rem 2rem;
  border: 1px solid #ccc;
  display: inline-block;

}
</style>

### Documentation and Tagging
| Color     | Sample                                                              | Classes / Elements |
| --------- | ------------------------------------------------------------------- | ------------------ |
| aliceblue | <span style="background:aliceblue;" class="swatch-orig">Text</span> | `.ehw-doc-descr`   |
| #e6e6fa   | <span style="background:#e6e6fa;" class="swatch-orig">Text</span>   | `#sec-tags ul li`  |
| #f0edff   | <span style="background:#f0edff;" class="swatch-orig">Text</span>   | `.boot-dev-op-sec` |

***

### Alerts and Status Banners
| Color   | Sample                                                            | Classes / Elements                           |
| ------- | ----------------------------------------------------------------- | -------------------------------------------- |
| #fff8e1 | <span style="background:#fff8e1;" class="swatch-orig">Text</span> | `.warning-banner`                            |
| #e3f2fd | <span style="background:#e3f2fd;" class="swatch-orig">Text</span> | `.info-banner`                               |
| #eafbea | <span style="background:#eafbea;" class="swatch-orig">Text</span> | `.success-banner`, `.fat-heading[id^="tip"]` |
| #fde8e8 | <span style="background:#fde8e8;" class="swatch-orig">Text</span> | `.error-banner`                              |
| pink    | <span style="background:pink;" class="swatch-orig">Text</span>    | `.error` background                          |

***

### Notes, Callouts, and Highlights
| Color     | Sample                                                              | Classes / Elements                           |
| --------- | ------------------------------------------------------------------- | -------------------------------------------- |
| #ffffe3   | <span style="background:#ffffe3;" class="swatch-orig">Text</span>   | `h6` notes                                   |
| mistyrose | <span style="background:mistyrose;" class="swatch-orig">Text</span> | `.fat-heading[id^="gotcha"]`                 |
| #ffffe9   | <span style="background:#ffffe9;" class="swatch-orig">Text</span>   | `.callout`                                   |
| #f0f4f8   | <span style="background:#f0f4f8;" class="swatch-orig">Text</span>   | `.callout pre`                               |
| #fef3c7   | <span style="background:#fef3c7;" class="swatch-orig">Text</span>   | `.label-verbatim`                            |
| bisque    | <span style="background:bisque;" class="swatch-orig">Text</span>    | `.fat-heading[id*="---"]` (video timestamps) |

***

### UI Elements and Labels
| Color     | Sample                                                              | Classes / Elements |
| --------- | ------------------------------------------------------------------- | ------------------ |
| beige     | <span style="background:beige;" class="swatch-orig">Text</span>     | `.code-filename`   |
| #cec2ff   | <span style="background:#cec2ff;" class="swatch-orig">Text</span>   | `.boot-dev-op`     |
| lightcyan | <span style="background:lightcyan;" class="swatch-orig">Text</span> | `#bookmark`        |

***

#### Key:

> ✅ = Official standard HTML color name; all other names are informal


### Section Colors with Names

| IDX  | HEX CODE | ORIGINAL COLOR NAME | OFFICIAL COLOR NAME ✅ | MATCHES OTHER STANDARD COLOR | COLOR SWATCH                                                               |
| :--- | :------- | :------------------ | :-------------------- | :--------------------------- | :------------------------------------------------------------------------- |
| 1    | \#FFEDF3 | Lavender Blush      |                       |                              | <span style="background:#FFEDF3" class="swatch-orig">Lavender Blush</span> |
| 2    | \#DB7082 | Blush               |                       |                              | <span style="background:#DB7082" class="swatch-orig">Blush</span>          |
| 3    | \#FFC2D5 | Orchid Pink         |                       |                              | <span style="background:#FFC2D5" class="swatch-orig">Orchid Pink</span>    |
| 4    | \#FFF7ED | Floral White        |                       |                              | <span style="background:#FFF7ED" class="swatch-orig">Floral White</span>   |
| 5    | \#DBBE70 | Ecru                |                       |                              | <span style="background:#DBBE70" class="swatch-orig">Ecru</span>           |
| 6    | \#FFE6C2 | Wheat               | `wheat`               |                              | <span style="background:#FFE6C2" class="swatch-orig">`wheat`</span>        |
| 7    | \#F2FFED | Honeydew            | `honeydew`            |                              | <span style="background:#F2FFED" class="swatch-orig">`honeydew`</span>     |
| 8    | \#7BDB70 | Light Green         |                       | `lightgreen` \#90EE90        | <span style="background:#7BDB70" class="swatch-orig">***???***</span>      |
| 9    | \#D0FFC2 | Tea Green           |                       |                              | <span style="background:#D0FFC2" class="swatch-orig">Tea Green</span>      |
| 10   | \#EDFFFB | Azure (web)         |                       | `azure` \#F0FFFF             | <span style="background:#EDFFFB" class="swatch-orig">***???***</span>      |
| 11   | \#70DBD5 | Tiffany Blue        |                       |                              | <span style="background:#70DBD5" class="swatch-orig">Tiffany Blue</span>   |
| 12   | \#C2FFF4 | Celeste             |                       |                              | <span style="background:#C2FFF4" class="swatch-orig">Celeste</span>        |
| 13   | \#F0EDFF | Lavender (web)      |                       | `lavender` \#E6E6FA          | <span style="background:#F0EDFF" class="swatch-orig">***???***</span>      |
| 14   | \#9370DB | Amethyst            | `mediumpurple`        |                              | <span style="background:#9370DB" class="swatch-orig">`mediumpurple`</span> |
| 15   | \#CEC2FF | Periwinkle          |                       |                              | <span style="background:#CEC2FF" class="swatch-orig">Periwinkle</span>     |
| 16   | \#FFF2ED | Seashell            | `seashell`            |                              | <span style="background:#FFF2ED" class="swatch-orig">`seashell`</span>     |
| 17   | \#DB9E70 | Buff                |                       |                              | <span style="background:#DB9E70" class="swatch-orig">Buff</span>           |
| 18   | \#FFD4C2 | Pale Dogwood        |                       |                              | <span style="background:#FFD4C2" class="swatch-orig">Pale Dogwood</span>   |
| 19   | \#FDEDFF | Pale Purple         |                       |                              | <span style="background:#FDEDFF" class="swatch-orig">Pale Purple</span>    |
| 20   | \#DB70D3 | Orchid              | `orchid`              |                              | <span style="background:#DB70D3" class="swatch-orig">`orchid`</span>       |
| 21   | \#FCC2FF | Mauve               |                       | `mauve` \#E0B0FF             | <span style="background:#FCC2FF" class="swatch-orig">***???***</span>      |

### Pastel Section Color Sets

| Index | Section Background                                                   | Section Border                                                       | Label Background                                                     | Color Names                                      |
| ----- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | ------------------------------------------------ |
| 1     | <span style="background:#FFEDF3;" class="swatch-orig">#FFEDF3</span> | <span style="background:#DB7082;" class="swatch-orig">#DB7082</span> | <span style="background:#FFC2D5;" class="swatch-orig">#FFC2D5</span> | `Lavender Blush`, `Blush`, `Orchid Pink`         |
| 2     | <span style="background:#FFF7ED;" class="swatch-orig">#FFF7ED</span> | <span style="background:#DBBE70;" class="swatch-orig">#DBBE70</span> | <span style="background:#FFE6C2;" class="swatch-orig">#FFE6C2</span> | `Floral White`, `Ecru`, `✅_wheat`                |
| 3     | <span style="background:#F2FFED;" class="swatch-orig">#F2FFED</span> | <span style="background:#7BDB70;" class="swatch-orig">#7BDB70</span> | <span style="background:#D0FFC2;" class="swatch-orig">#D0FFC2</span> | `✅_honeydew`, `Light Green`, `Tea Green`         |
| 4     | <span style="background:#EDFFFB;" class="swatch-orig">#EDFFFB</span> | <span style="background:#70DBD5;" class="swatch-orig">#70DBD5</span> | <span style="background:#C2FFF4;" class="swatch-orig">#C2FFF4</span> | `Azure (web)`, `Tiffany Blue`, `Celeste`         |
| 5     | <span style="background:#F0EDFF;" class="swatch-orig">#F0EDFF</span> | <span style="background:#9370DB;" class="swatch-orig">#9370DB</span> | <span style="background:#CEC2FF;" class="swatch-orig">#CEC2FF</span> | `Lavender (web)`, `✅_mediumpurple`, `Periwinkle` |
| 6     | <span style="background:#FFF2ED;" class="swatch-orig">#FFF2ED</span> | <span style="background:#DB9E70;" class="swatch-orig">#DB9E70</span> | <span style="background:#FFD4C2;" class="swatch-orig">#FFD4C2</span> | `✅_seashell`, `Buff`, `Pale Dogwood`             |
| 7     | <span style="background:#EDFAFF;" class="swatch-orig">#EDFAFF</span> | <span style="background:#70ADDB;" class="swatch-orig">#70ADDB</span> | <span style="background:#C2EDFF;" class="swatch-orig">#C2EDFF</span> | `✅_aliceblue`, `Carolina Blue`, `Uranian Blue`   |
| 8     | <span style="background:#FDEDFF;" class="swatch-orig">#FDEDFF</span> | <span style="background:#DB70D3;" class="swatch-orig">#DB70D3</span> | <span style="background:#FCC2FF;" class="swatch-orig">#FCC2FF</span> |               `Pale Purple`, `✅_orchid`, `Mauve`                                   |


***

## ✅ Revision History


| Version | Date       | Author           | Notes                                                           |
| ------- | ---------- | ---------------- | --------------------------------------------------------------- |
| 1.00    | 2025-10-28 | Eric L. Hepperle | Initial draft created with grouped color palette documentation. |
| 1.01    | 2025-10-28 | Eric L. Hepperle | Update file docblock and TOC.                                   |
| 1.02    | 2025-10-30 | Eric L. Hepperle | Add pastel section variations, deduplicate intro content.       |
| 1.03    | 2025-10-31 | Eric L. Hepperle | Add color names table.                                          |