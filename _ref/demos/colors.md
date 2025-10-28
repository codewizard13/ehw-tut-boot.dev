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

A structured visual catalog of pastel color swatches and their corresponding UI class references, consolidating all reusable styling examples from `main.css`.  
Each entry includes live render previews, mapped CSS class locations, and associated design roles for cohesive visual implementation.

***

## Usage Guidelines

- Use these tables to identify and apply pastel color classes consistently across interface elements.  
- Reference only defined CSS classes (avoid direct inline styling).  
- Maintain version alignment with active `main.css` builds.  
- Utilize this document as both a visual lookup and a reusable snippet companion for course documentation.

***

<details open>
  <summary><h2>Table of Contents</h2></summary>

- [📦 Pastel Colors Reference](#-pastel-colors-reference-for-bootdev-course-notes)  
  - [Usage Guidelines](#usage-guidelines)  
  - [Content](#content)  
  - [Revision History](#revision-history)

</details>

***

## CONTENT

A grouped and descriptive palette of pastel colors from `main.css`, organized by their functional role in documentation design—covering informational banners, content highlights, UI tags, and other themed label styles.



<!-- Custom Stylesheet Reference -->
<link rel="stylesheet" href="../../_css/main.css">
<!-- <link rel="stylesheet" href="../../_css/status-messages.css"> -->

![Site Logo](/_pix/logos/logo-ehw-kb-h32.png)

# 📦 PASTEL COLORS REFERENCE for Boot.dev Course Notes

A structured visual catalog of pastel color swatches and associated UI class references, consolidating reusable styling examples from `main.css`.  
Each entry includes rendered previews, class locations, and color associations for consistent design implementation.

***

## Usage Guidelines

- Use these tables to identify and apply pastel colors consistently across UI components.  
- Reference only defined CSS classes (avoid inline color definitions).  
- Keep examples synchronized with the version of `main.css` used in your project.  
- This document serves as both a visual reference and snippet library for documentation styling.

***

- [📦 PASTEL COLORS REFERENCE for Boot.dev Course Notes](#-pastel-colors-reference-for-bootdev-course-notes)
  - [Usage Guidelines](#usage-guidelines)
  - [CONTENT](#content)
- [📦 PASTEL COLORS REFERENCE for Boot.dev Course Notes](#-pastel-colors-reference-for-bootdev-course-notes-1)
  - [Usage Guidelines](#usage-guidelines-1)
  - [CONTENT](#content-1)
    - [Documentation and Tagging](#documentation-and-tagging)
    - [Alerts and Status Banners](#alerts-and-status-banners)
    - [Notes, Callouts, and Highlights](#notes-callouts-and-highlights)
    - [UI Elements and Labels](#ui-elements-and-labels)
- [HTML Color Swatch Template](#html-color-swatch-template)
  - [✅ Revision History](#-revision-history)


***

## CONTENT

A grouped palette of pastel colors from `main.css`, organized by their functional use across documentation, status banners, highlights, and UI element classes.

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

Would you like the next version to include light-to-dark or hue-based sorting within each group?



# HTML Color Swatch Template



| Background | Text    | Style Vibe              | Swatch                                                                           |
| ---------- | ------- | ----------------------- | -------------------------------------------------------------------------------- |
| #FFFACD    | #003366 | Cheerful & professional | <span style="background-color:#FFFACD;color:#003366;" class="swatch">Text</span> |
| #D0F0F0    | #333333 | Calm & modern           | <span style="background-color:#D0F0F0;color:#333333;" class="swatch">Text</span> |
| #FFE5B4    | #4B2E2E | Warm & inviting         | <span style="background-color:#FFE5B4;color:#4B2E2E;" class="swatch">Text</span> |
| #E6E6FA    | #000080 | Elegant & clean         | <span style="background-color:#E6E6FA;color:#000080;" class="swatch">Text</span> |
| #CCFFCC    | #006400 | Fresh & natural         | <span style="background-color:#CCFFCC;color:#006400;" class="swatch">Text</span> |
| #F0F0F0    | #000000 | Minimalist & sharp      | <span style="background-color:#F0F0F0;color:#000000;" class="swatch">Text</span> |
| #D0EFFF    | #191970 | Crisp & techy           | <span style="background-color:#D0EFFF;color:#191970;" class="swatch">Text</span> |

***

## ✅ Revision History


| Version | Date       | Author           | Notes                                                           |
| ------- | ---------- | ---------------- | --------------------------------------------------------------- |
| 1.00    | 2025-10-28 | Eric L. Hepperle | Initial draft created with grouped color palette documentation. |
| 1.01    | 2025-10-28 | Eric L. Hepperle | Update file docblock and TOC.                                   |