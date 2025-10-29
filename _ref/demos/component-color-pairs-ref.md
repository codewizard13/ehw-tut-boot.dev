
# 🎨 COMPONENT–COLOR PAIR REFERENCE

A comprehensive mapping of all pastel color relationships found in `main.css`, grouped by feature to show which classes work together for consistent UI design.

***

<style>
.swatch-orig {
  padding: 0.5rem 2rem;
  border: 1px solid #ccc;
  display: inline-block;
}
</style>

***

## Boot.dev Operations Components

| Element | Selector | Color(s) Used | Sample |
|----------|-----------|---------------|--------|
| Meta Instruction Label | `.boot-dev-op` | `#cec2ff` (background), white (icon), black (border) | <span style="background:#cec2ff;" class="swatch-orig">Text</span> |
| Meta Instruction Section | `.boot-dev-op-sec` | `#f0edff` (background), mediumpurple (border) | <span style="background:#f0edff;" class="swatch-orig">Text</span> |

**Relationship:** `.boot-dev-op` and `.boot-dev-op-sec` work as a matched callout header and body segment commonly used in Boot.dev tutorials.

***

## Documentation and Tagging

| Element | Selector | Color(s) Used | Sample |
|----------|-----------|---------------|--------|
| Documentation Box | `.ehw-doc-descr` | `aliceblue` (background), gainsboro (border) | <span style="background:aliceblue;" class="swatch-orig">Text</span> |
| Tag Items | `#sec-tags ul li` | `#e6e6fa` (background), `#000080` (text) | <span style="background:#e6e6fa;" class="swatch-orig">Text</span> |

**Relationship:** Both enhance inline or block-level documentation clarity; `aliceblue` for info boxes, and lavender tones for tag lists.

***

## Status Banner Groups

| Banner Type | Selector | Color(s) Used | Sample |
|---------------|-----------|---------------|--------|
| Warning | `.warning-banner` | `#fff8e1` background, `#ff9800` border, `#b26a00` text | <span style="background:#fff8e1;" class="swatch-orig">Text</span> |
| Info | `.info-banner` | `#e3f2fd` background, `#2196f3` border, `#1769aa` text | <span style="background:#e3f2fd;" class="swatch-orig">Text</span> |
| Success | `.success-banner` | `#eafbea` background, `#43a047` border, `#20782b` text | <span style="background:#eafbea;" class="swatch-orig">Text</span> |
| Error | `.error-banner` | `#fde8e8` background, `#f44336` border, `#b71c1c` text | <span style="background:#fde8e8;" class="swatch-orig">Text</span> |

**Relationship:** These banners form a consistent color-coded notification set, ranging from neutral info (blue) to urgent warnings (yellow).

***

## Bookmark and Linking Components

| Element | Selector | Color(s) Used | Sample |
|----------|-----------|---------------|--------|
| Bookmark Indicator | `#bookmark` | `lightcyan` (background), cadetblue (border) | <span style="background:lightcyan;" class="swatch-orig">Text</span> |
| Bookmark Icon | `#bookmark::before` | white (icon) | <span style="background:cadetblue; color:white;" class="swatch-orig">🔖</span> |

**Relationship:** Visual pairing creates a consistent bookmark icon tag and highlighted box for “resume here” markers.

***

## Code and Verbatim Sections

| Element | Selector | Color(s) Used | Sample |
|----------|-----------|---------------|--------|
| Code Filename Label | `.code-filename` | `beige` (background), black (border), slategray (icon background) | <span style="background:beige;" class="swatch-orig">Text</span> |
| Verbatim Label | `.label-verbatim` | `#fef3c7` (background), brown (border) | <span style="background:#fef3c7;" class="swatch-orig">Text</span> |
| Callout Container | `.callout` | `#ffffe9` (background), `#92400e` (border) | <span style="background:#ffffe9;" class="swatch-orig">Text</span> |
| Callout Code Block | `.callout pre` | `#f0f4f8` (background), `#cbd5e1` (border) | <span style="background:#f0f4f8;" class="swatch-orig">Text</span> |

**Relationship:** These styles combine to form the “verbatim section” pattern used in lesson extracts and quoted instructional segments.

***

## Course Notes and Contextual Headers

| Element | Selector | Color(s) Used | Sample |
|----------|-----------|---------------|--------|
| Gotcha Heading | `.fat-heading[id^="gotcha"]` | `mistyrose` (background), brown (border, text) | <span style="background:mistyrose;" class="swatch-orig">Text</span> |
| Tip Heading | `.fat-heading[id^="tip"]` | `#eafbea` (background) | <span style="background:#eafbea;" class="swatch-orig">Text</span> |
| Time Stamp Heading | `.fat-heading[id*="---"]` | `bisque` (background) | <span style="background:bisque;" class="swatch-orig">Text</span> |
| General Note Heading | `h6` | `#ffffe3` (background), gray (border) | <span style="background:#ffffe3;" class="swatch-orig">Text</span> |

**Relationship:** Unified “course heading” aesthetic using soft pastels, distinguishing caution, tip, timing, and note categories.

***

### Summary of Key Component Pairings

| Feature Area | Label Class | Section / Block Class | Shared Theme Color | Swatch |
|---------------|-------------|------------------------|--------------------|--------|
| Boot.dev Operations | `.boot-dev-op` | `.boot-dev-op-sec` | Lavender–Purple | <span style="background:#cec2ff;" class="swatch-orig"></span> <span style="background:#f0edff;" class="swatch-orig"></span> |
| Documentation | `.ehw-doc-descr` | `#sec-tags ul li` | Blue–Lavender | <span style="background:aliceblue;" class="swatch-orig"></span> <span style="background:#e6e6fa;" class="swatch-orig"></span> |
| Status Banners | `.warning-banner` / `.info-banner` / `.success-banner` / `.error-banner` | Independent blocks | Yellow–Blue–Green–Red | <span style="background:#fff8e1;" class="swatch-orig"></span> <span style="background:#e3f2fd;" class="swatch-orig"></span> <span style="background:#eafbea;" class="swatch-orig"></span> <span style="background:#fde8e8;" class="swatch-orig"></span> |
| Bookmarks | `#bookmark` | `#bookmark::before` | Cyan–Teal | <span style="background:lightcyan;" class="swatch-orig"></span> <span style="background:cadetblue;" class="swatch-orig"></span> |
| Code + Verbatim | `.label-verbatim` / `.callout` / `.code-filename` | `.callout pre` | Ivory–Beige–Soft Gray | <span style="background:#fef3c7;" class="swatch-orig"></span> <span style="background:#ffffe9;" class="swatch-orig"></span> <span style="background:beige;" class="swatch-orig"></span> |
| Course Note Headers | `.fat-heading` variants / `h6` | N/A | Cream–Rose–Mint–Peach | <span style="background:#ffffe3;" class="swatch-orig"></span> <span style="background:mistyrose;" class="swatch-orig"></span> <span style="background:#eafbea;" class="swatch-orig"></span> <span style="background:bisque;" class="swatch-orig"></span> |

***

Would you like me to add a “Color Intent” column (e.g., calm, cautionary, confirmative) for visual design context in the next version?