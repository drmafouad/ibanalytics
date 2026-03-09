# 🐰 Investor Bunny Design System

This document outlines the visual identity of the **Investor Bunny Strategic Intelligence** platform. It ensures consistency across all research reports, dashboards, and portals.

## 🎨 Color Palette
The brand uses a warm, earthy "Academic Financial" palette designed for deep reading and intellectual clarity.

| Variable Name | Hex Code | Purpose |
| :--- | :--- | :--- |
| `bg-base` | `#FDFAF6` | **Warm Cream**: Primary application background. |
| `bg-card` | `#FFFFFF` | **Pure White**: Card and content area backgrounds. |
| `bg-sidebar` | `#1A1918` | **Charcoal Coffee**: Sidebar, Footer, and high-impact strategy modules. |
| `border-soft` | `#E9E2D9` | **Soft Beige**: Subtle separators and card borders. |
| `text-primary` | `#2D2A26` | **Deep Coffee**: High-contrast body text and headings. |
| `text-secondary` | `#7A746C` | **Warm Muted Gray**: Secondary descriptions, captions, and citations. |
| `accent-warm` | `#D97706` | **Amber**: Primary accent, technical indicator status, and high-importance highlights. |
| `accent-terracotta`| `#C2410C` | **Terracotta**: Brand identity color, logo accents, and bearish/alert indicators. |
| `accent-sage` | `#65A30D` | **Sage Green**: Bullish indicators, growth scores, and success metrics. |
| `accent-plum` | `#9D174D` | **Deep Plum**: Bearish indicators or "Risk-Off" notifications. |

---

## 🖋️ Typography
A sophisticated blend of high-end serifs and modern geometric sans-serifs.

### 1. **Fraunces** (Serif)
*   **Weights**: 300, 400, 600, 700
*   **Usage**: All primary Headings (`h1`, `h2`), Large Data Values (e.g., Stock Price), and Logo text.
*   **Personality**: Authoritative, high-contrast, premium "wall street journal" aesthetic.

### 2. **Instrument Serif** (Serif - Italic Focused)
*   **Weights**: Italic (0, 1)
*   **Usage**: Subtitles, Citations, Analytical Insights, and "The Bunny Thesis" sections.
*   **Personality**: Scholarly, sophisticated, adds a layer of intellectual personality.

### 3. **Plus Jakarta Sans** (Sans-Serif)
*   **Weights**: 400, 500, 600, 700, 800
*   **Usage**: UI elements, labels (caps), tables, body text, and calculator inputs.
*   **Personality**: High legibility, modern, clean, and data-friendly.

---

## 📐 General Design Rules

### 1. The "Breathable" Grid
*   **Padding**: Cards must use `2.5rem` (`40px`) internal padding to ensure data doesn't feel cramped.
*   **Gaps**: The grid system uses a `2.5rem` (`40px`) gap between modules.
*   **Main Container**: Use `5%` horizontal padding for the main content area to frame the report like a focused document.

### 2. Visual Hierarchy
*   **Labels**: Use `Plus Jakarta Sans`, font-size `0.7rem`, font-weight `800`, and `uppercase` with `0.1em` letter spacing for section headers and data labels.
*   **Stat Values**: Use `Fraunces` Bold/Semibold at larger sizes (`1.5rem` to `3.25rem`) to make data points "speak" louder than the labels.
*   **Borders**: Keep borders subtle (`1px solid #E9E2D9`). Avoid heavy shadows; use a very light, soft coffee-tinted shadow for depth.

### 3. Modularity & Theming
*   **The "Shadow" Section**: Use a charcoal background (`#1A1918`) for "Actionable" sections like Trading Strategies or Spec Sheets to visually separate "analysis" from "execution."
*   **Badges**: Status labels (Bullish, Bearish, Neutral) use low-saturation background colors derived from the accent palette (e.g., `#ECFCCB` for Bullish).

### 4. Semantic UI Icons
*   **Stroke Width**: Icons should use a `thin-to-medium` weight (`2px` to `3px` stroke) to match the elegance of the serif fonts.
*   **Colors**: Icons should inherit the text color or the semantic accent color (e.g., Sage for Up-arrows).
