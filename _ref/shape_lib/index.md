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

# 📦 SHAPE SNIPPET LIBRARY

A curated, well-documented collection of custom HTML span label and status banner snippets for consistent use in Markdown documentation.
All objects assume CSS classes are defined in `main.css` and/or section-specific stylesheets. Reference this file to copy/paste standardized UI snippets for consistent visuals throughout your documentation.

> **⚠️Caveat:** This document renders beautifully in VSCode’s Markdown Preview tab, where the linked CSS styles apply seamlessly. However, on GitHub’s native Markdown rendering, these custom styles will likely not be applied, resulting in unstyled snippets. 
> > 
> For durable presentation and consistent styling across platforms, consider exporting this documentation to PDF or HTML formats where stylesheets can be reliably included and rendered.

---

## Usage Guidelines

- **Copy** the desired shape/object snippet’s code block for Markdown placement.
- **Reference** this file to keep visual and UX standards consistent repo-wide.
- **Update** both the live object and description if you change any CSS classes.
- All snippets below are HTML only, no inline CSS required.

---

<details open>
  <summary><h2>Table of Contents</h2></summary>

<!-- no toc : applied to prevent Markdown All in One extension from auto-updating the TOC -->
- [📦 SHAPE SNIPPET LIBRARY](#-shape-snippet-library)
  - [Usage Guidelines](#usage-guidelines)
  - [Tags, Labels, Section Markers 🏷️](#tags-labels-section-markers-️)
    - [Boot.dev Meta Instruction Label](#bootdev-meta-instruction-label)
    - [Bookmark Anchor](#bookmark-anchor)
    - [Code Filename Label](#code-filename-label)
  - [Status Messages 📢](#status-messages-)
    - [Warning Banner ⚠️](#warning-banner-️)
    - [Info Banner ℹ️](#info-banner-ℹ️)
    - [Success Banner ✅](#success-banner-)
    - [Error Banner ⛔](#error-banner-)
  - [✅ Revision History](#-revision-history)
  
</details>


---


## Tags, Labels, Section Markers 🏷️

Reusable in-line elements for labeling operational instructions, anchors, code references, and more.  
Use these to clarify workflow steps, provide quick jump points in documentation, or call out filenames and input tags.

### Boot.dev Meta Instruction Label

- **Purpose**: Call attention to meta-instructions, “operation” steps, or workflow actions in tutorials and guides.
- **Appearance**: Inline block with purple background, gear icon (⚙️), black border (except left), and bold font.

<span class="boot-dev-op">Boot.dev Instructions:</span>

```
<span class="boot-dev-op">Boot.dev Instructions:</span>
```

### Bookmark Anchor

- **Purpose**: Visually indicate the last visited section or stopping point to quickly resume a course or study session.
- **Appearance**: Rounded cyan label with bookmark icon, used to highlight references, pointers, or quick-links.

<span id="bookmark">Bookmark this section</span>

```
<span id="bookmark">Bookmark this section</span>
```

### Code Filename Label

- **Purpose**: Mark filenames or code file references inline or alongside code blocks in technical notes.
- **Appearance**: Document icon and beige tag with black border, rounded right corners, for in-line clarity.

<span class="code-filename">example.py</span>

```
<span class="code-filename">example.py</span>
```

---

## Status Messages 📢

Reusable banners for highlighting status, tips, alerts, and feedback messages.  
Use these tags at the top of steps, inside callouts, or at key transitions to clearly signal important status or actionable notes.

### Warning Banner ⚠️

- **Purpose**: Present warnings, cautions, or potential hazards that require user attention before proceeding.
- **Appearance**: High-contrast yellow/orange tag, rounded corners with warning icon at the start.

<span class="warning-banner">Attention: Proceed with caution!</span>

```
<span class="warning-banner">Attention: Proceed with caution!</span>
```

### Info Banner ℹ️

- **Purpose**: Convey general tips, reminders, or supplemental information helpful to readers.
- **Appearance**: Blue label with information icon, white text, and rounded corners for high visibility.

<span class="info-banner">Tip: You can reset your password anytime.</span>

```
<span class="info-banner">Tip: You can reset your password anytime.</span>
```

### Success Banner ✅

- **Purpose**: Confirm completion, success, or affirmation. Use after positive save/submit actions or tutorial finish.
- **Appearance**: Light green tag with checkmark icon and bold, dark green text.

<span class="success-banner">Success! Your changes have been saved.</span>

```
<span class="success-banner">Success! Your changes have been saved.</span>
```

### Error Banner ⛔

- **Purpose**: Flag errors, rejected inputs, or failed actions that need correction or user review.
- **Appearance**: Pink/red box with stop icon at the start and clear error message labeling.

<span class="error-banner">Error: This action could not be completed.</span>

```
<span class="error-banner">Error: This action could not be completed.</span>
```



---

## ✅ Revision History

| Version | Date       | Author           | Changes Made           |
| ------- | ---------- | ---------------- | ---------------------- |
| 1.00    | 2025-09-26 | Eric L. Hepperle | Initial draft created. |

---