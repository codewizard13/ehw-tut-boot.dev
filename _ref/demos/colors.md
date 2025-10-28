<!-- ===========================================================================
@file _shape-snippets.md
@date 2025-09-26 09:44 AM CDT
@description
  Centralized library of reusable span label, status banner, and shaped object snippets for Markdown documentation.
  Designed for consistent UI snippet reuse and easy copy-paste inclusion.
  Assumes required CSS is loaded via:
    - ../../_css/main.css for general tags and labels
    - ../../_css/status-messages.css for status banner styles
  Includes:
    - Section headings and rendered descriptions
    - Live rendered HTML snippets ("in the wild")
    - Copy-paste HTML code blocks
  Note: This renders well in VSCode Markdown Preview but styling may be lost in GitHub Markdown.
    Export to PDF or HTML for durable styled outputs.
@author Eric L. Hepperle
========================================================================== -->

<!-- Custom Stylesheet Reference -->
<link rel="stylesheet" href="../../_css/main.css">
<!-- <link rel="stylesheet" href="../../_css/status-messages.css"> -->

![Site Logo](/_pix/logos/logo-ehw-kb-h32.png)

# 📦 PASTEL COLORS REFERENCE

A structured visual catalog of pastel color swatches and associated UI class references, consolidating reusable styling examples from `main.css`.  
Each entry includes rendered previews, class locations, and color associations for consistent design implementation.

***

## Usage Guidelines

- Use these tables to identify and apply pastel colors consistently across UI components.  
- Reference only defined CSS classes (avoid inline color definitions).  
- Keep examples synchronized with the version of `main.css` used in your project.  
- This document serves as both a visual reference and snippet library for documentation styling.

***

<details open>
  <summary><h2>Table of Contents</h2></summary>

- [📦 SHAPE SNIPPET DOCUMENT](#-shape-snippet-document)  
  - [Usage Guidelines](#usage-guidelines)  
  - [CONTENT](#content)  
  - [Revision History](#revision-history)

</details>

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