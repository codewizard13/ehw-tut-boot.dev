<!-- ===========================================================================
@file _shape-snippets.md
@date 2025-09-26 09:44 AM CDT
@description
  Centralized library of reusable span label, status banner, and shaped object snippets for Markdown documentation.
  Designed for consistent UI snippet reuse and easy copy-paste inclusion.
  Assumes required CSS is loaded via:
    - ../../_css/main.css for general tags and labels
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
    - [Markdown-Only Note / Tip](#markdown-only-note--tip)
    - [Output-Results Section](#output-results-section)
    - [Boot.dev Meta Instruction Label](#bootdev-meta-instruction-label)
    - [Bookmark Anchor](#bookmark-anchor)
    - [Code Filename Label](#code-filename-label)
    - [Lesson Heading Title](#lesson-heading-title)
    - [▶️ L6: Where to Declare Functions](#️-l6-where-to-declare-functions)
  - [Status Messages 📢](#status-messages-)
    - [Warning Banner ⚠️](#warning-banner-️)
    - [Info Banner ℹ️](#info-banner-ℹ️)
    - [Success Banner ✅](#success-banner-)
    - [Error Banner ⛔](#error-banner-)
  - [Banners with Matched Sections](#banners-with-matched-sections)
    - [Info Section with Internal Heading](#info-section-with-internal-heading)
    - [Boot.dev Meta Instruction Label + Section](#bootdev-meta-instruction-label--section)
    - [Error Section](#error-section)
    - [Verbatim Copy Section](#verbatim-copy-section)
    - [Verbatim Copy-Assignment-Answer Section](#verbatim-copy-assignment-answer-section)
      - [**Snippet:**](#snippet)
    - [Challenge Section](#challenge-section)
    - [Boots' Feedback Section](#boots-feedback-section)
  - [CORRECT! 🏆](#correct-)
  - [✅ Revision History](#-revision-history)
  
</details>


---


## Tags, Labels, Section Markers 🏷️

Reusable in-line elements for labeling operational instructions, anchors, code references, and more.  
Use these to clarify workflow steps, provide quick jump points in documentation, or call out filenames and input tags.


### Markdown-Only Note / Tip

**Basic**

> 💡 *Placeholder content here in italics.

```md
> 💡 *Placeholder content here in italics.
```

or the tip

**With Text**

> 💡 **TIP**: *Placeholder content here in italics.*

```md
> 💡 **TIP**: *Placeholder content here in italics.*
```

### Output-Results Section


**📈 OUTPUT RESULTS**

```sh
Inputs: 0, 0, 0
Expected: (0, 0, 0)
Actual:   (0, 0, 0)
Pass
---------------------------------
Inputs: 1111, 1111, 1111
Expected: (15, 15, 15)
Actual:   (15, 15, 15)
Pass
---------------------------------
Inputs: 101010, 110011, 101010
Expected: (42, 51, 42)
Actual:   (42, 51, 42)
Pass
============= PASS ==============
6 passed, 0 failed
```

````sh

**📈 OUTPUT RESULTS**

```sh
// RESULTS_PLACEHOLDER
```
````


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

### Lesson Heading Title

### ▶️ L6: Where to Declare Functions

```md
### ▶️ L6: Where to Declare Functions
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

## Banners with Matched Sections


### Info Section with Internal Heading

<section class="info-banner"><span>💡 Printing to Debug Your Code </span>

Printing values and running your code is a great way to debug your code. You can see what values are stored in various variables, find your mistakes, and fix them. Add print statements and run your code as you go! It's a great habit to get into to make sure that each line you write is doing what you expect it to do.

</section>

```
<section class="info-banner"><span>💡 [Title_in_Title_Case] </span>

// Content Here

</section>
```

<section class="info-banner"><span>💡 PRO TIP: </span>
In Python, functions must be defined before they are called
</section>

```
<section class="info-banner"><span>💡 PRO TIP: </span>

// Content Here

</section>
```


### Boot.dev Meta Instruction Label + Section

<span class="boot-dev-op">Boot.dev Instructions:</span>

<section class="boot-dev-op-sec">

In the real world it's rare to leave `print()` statements in your code when you're done debugging. Similarly, you need to remember to remove any `print()` statements from your code before submitting your work here on Boot.dev because it will interfere with the tests!


</section>

```
<span class="boot-dev-op">Boot.dev Instructions:</span>

<section class="boot-dev-op-sec">

// Content Here

</section>
```

### Error Section

<section class="error-banner">Error:

```sh
PythonError: Traceback (most recent call last):
  File "<exec>", line 16, in <module>
  File "<string>", line 1, in <module>
NameError: name 'main' is not defined
```

</section>

````
<section class="error-banner">Error:

```sh
// Error Code Here
```

</section>
````

### Verbatim Copy Section

<section class="callout"><span class="label-verbatim">Copied verbatim from the course 👇🏽</span>

Let's break down this function line by line so you can understand every nook and cranny of it.

```py
def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result

radius = 5
area = area_of_circle(radius)
print(area)
# 78.5
```

Here's a chronological explanation of what happens when the above code is executed:

1. `def area_of_circle(r)`

The `area_of_circle` function is defined for later use, but not called. It accepts a single input, the arbitrarily named `r`. The body of the function (`pi = 3.14.`.. etc) is ignored for now.

2. `radius = 5`
A new variable called `radius` is created and set to the value `5`.

... etc.

</section>

<br>

```
<section class="callout"><span class="label-verbatim">Copied verbatim from the course 👇🏽</span>

// Content Here

... etc.

</section>
```

---

### Verbatim Copy-Assignment-Answer Section

<section class="callout"><span class="label-verbatim">COPIED VERBATIM:  👇🏽</span>

// VERBATIM_CONTENT

</section>

<section class="callout"><span class="label-verbatim">Assignment:  👇🏽</span>

// ASSIGNMENT CONTENT

</section>

<br>

<section class="assignment-answer-sec">

**✍️ ASSIGNMENT STARTING CODE:**

<span class="code-filename">main.py</span>

```py
// answer starting code here
```

**✍️ MY ANSWER:**

```py
// answer code here
```

</section><!-- END .assignment-answer-sec -->

#### **Snippet:**

````sh

<section class="callout"><span class="label-verbatim">COPIED VERBATIM:  👇🏽</span>

// VERBATIM_CONTENT

</section>

<section class="callout"><span class="label-verbatim">Assignment:  👇🏽</span>

// ASSIGNMENT CONTENT

</section>

<br>

<section class="assignment-answer-sec">

**✍️ ASSIGNMENT STARTING CODE:**

<span class="code-filename">main.py</span>

```py
// answer starting code here
```

**✍️ MY ANSWER:**

```py
// answer code here
```

</section><!-- END .assignment-answer-sec -->

````

### Challenge Section

<section class="challenge callout"><span class="label-challenge">CHALLENGE:  [Challenge Name] 👇🏽</span>

// CHALLENGE_CONTENT

</section>

<br>

<section class="assignment-answer-sec">

**✍️ ASSIGNMENT STARTING CODE:**

<span class="code-filename">main.py</span>

```py
// answer starting code here
```

**✍️ MY ANSWER:**

```py
// answer code here
```

</section><!-- END .assignment-answer-sec -->

<br>

````md
<section class="challenge callout"><span class="label-challenge">CHALLENGE:  [Challenge Name] 👇🏽</span>

// CHALLENGE_CONTENT

</section>

<br>

<section class="assignment-answer-sec">

**✍️ ASSIGNMENT STARTING CODE:**

<span class="code-filename">main.py</span>

```py
// answer starting code here
```

**✍️ MY ANSWER:**

```py
// answer code here
```

</section><!-- END .assignment-answer-sec -->
````


### Boots' Feedback Section

<section class="boots-feeback callout"><span class="label-boots-feeback">BOOTS' FEEDBACK 👇🏽</span>

**✍️ BOOTS' FEEDBACK:**

## CORRECT! 🏆

// CONTENT_PLACEHOLDER

</section>

<br>

```md
<section class="boots-feeback callout"><span class="label-boots-feeback">BOOTS' FEEDBACK 👇🏽</span>

**✍️ BOOTS' FEEDBACK:**

## CORRECT! 🏆

// CONTENT_PLACEHOLDER

</section>
```

---

## ✅ Revision History

| Version | Date       | Author           | Changes Made                                                                            |
| ------- | ---------- | ---------------- | --------------------------------------------------------------------------------------- |
| 1.00    | 2025-09-26 | Eric L. Hepperle | Initial draft created.                                                                  |
| 1.02    | 2025-10-01 | Eric L. Hepperle | Add example sections (info, Boot.dev operation, error, verbatim copy) and lesson title. |

---