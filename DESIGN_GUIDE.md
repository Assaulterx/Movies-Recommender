# 🎨 StreamVault - Design Guide

Complete design specification and customization guide

---

## Design Philosophy

StreamVault combines modern UI/UX principles with professional OTT aesthetics:

- **Dark Mode**: Reduces eye strain, looks premium
- **Glassmorphism**: Modern glass effect with backdrop blur
- **Gradient Accents**: Eye-catching pink/purple colors
- **Smooth Animations**: Delightful user interactions
- **Responsive**: Works seamlessly across devices
- **Accessible**: WCAG AA compliant

---

## Color System

### Core Color Palette

#### Primary Colors
```
Pink/Magenta Start:    #E94560 (rgb(233, 69, 96))
Neon Magenta:          #FF006E (rgb(255, 0, 110))
```
Used for: Headlines, accents, hover states, CTAs

#### Background Colors
```
Background Primary:    #0F3460 (rgb(15, 52, 96))
Background Secondary:  #1A1A2E (rgb(26, 26, 46))
Background Tertiary:   #16213E (rgb(22, 33, 62))
```
Used for: Page backgrounds, sidebar, surfaces

#### Text Colors
```
Text Primary:          #EAEAEA (rgb(234, 234, 234))
Text Secondary:        #CBD5E1 (rgb(203, 213, 225))
Text Muted:            #94A3B8 (rgb(148, 163, 184))
```
Used for: Body text, labels, metadata

#### Accent Colors
```
Purple Secondary:      #667EEA (rgb(102, 126, 234))
Violet:                #764BA2 (rgb(118, 75, 162))
```
Used for: Secondary accents, alternative states

### Color Usage Guidelines

| Element | Color | Why |
|---------|-------|-----|
| Page Background | #0F3460 + gradient | Professional, deep |
| Headers (H1) | #FF006E gradient | Attention-grabbing |
| Section Headers (H2) | #FF006E | Clear hierarchy |
| Primary Buttons | Linear gradient | Eye-catching |
| Cards Background | rgba(255,255,255,0.05) | Subtle, clean |
| Card Borders | rgba(233,69,96,0.3) | Soft emphasis |
| Text | #EAEAEA | High contrast |
| Secondary Text | #CBD5E1 | Readable, softer |

---

## Typography System

### Font Stack
```css
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
```
Rationale: System fonts, fast loading, excellent rendering

### Type Scale

```
Display Large    40px  700  Line Height: 1.2  Margin: 30px 0
Display Medium   30px  700  Line Height: 1.2  Margin: 25px 0
Display Small    24px  700  Line Height: 1.2  Margin: 20px 0

Heading 1        28px  600  Line Height: 1.3  Margin: 20px 0
Heading 2        24px  600  Line Height: 1.3  Margin: 15px 0
Heading 3        20px  600  Line Height: 1.3  Margin: 12px 0

Body Large       18px  400  Line Height: 1.5  Margin: 12px 0
Body Medium      16px  400  Line Height: 1.5  Margin: 10px 0
Body Small       14px  400  Line Height: 1.5  Margin: 8px 0

Caption          12px  500  Line Height: 1.4  Margin: 4px 0
Small            11px  400  Line Height: 1.4  Margin: 2px 0
```

### Typography Examples

**Page Title**
```html
<h1>🎬 StreamVault</h1>
<!-- Display Large: 40px, bold, gradient color, with text-shadow -->
```

**Section Header**
```html
<h2>🔍 Recommendations</h2>
<!-- Heading 1: 28px, semibold, #FF006E -->
```

**Subsection**
```html
<h3>Popular on Netflix</h3>
<!-- Heading 2: 24px, semibold, #FF006E -->
```

**Body Text**
```html
<p>This is body text...</p>
<!-- Body Medium: 16px, regular, #EAEAEA -->
```

**Metadata**
```html
<small>📺 MOVIE • Netflix</small>
<!-- Caption: 12px, semibold, #94A3B8 -->
```

---

## Spacing System

### Spacing Scale
```
4px   = space-1   (minimal spacing)
8px   = space-2   (tight spacing)
12px  = space-3   (small spacing)
16px  = space-4   (standard spacing) ← DEFAULT
20px  = space-5   (comfortable)
24px  = space-6   (generous)
32px  = space-8   (large spacing)
40px  = space-10  (extra large)
```

### Padding Guidelines
```
Buttons:      12px vertical, 20px horizontal
Cards:        16-20px all sides
Sections:     20-30px all sides
Sidebar:      16px padding
Page:         20px minimum
```

### Margin Guidelines
```
Between sections:    20px
Between elements:    12px
After headings:      12px
Before lists:        8px
```

---

## Component Design

### Cards (Poster Display)

**Structure**
```
┌─────────────────────────────┐
│    Poster Image (300x450)   │
├─────────────────────────────┤
│ Title (max 30 chars)        │
│ Type: MOVIE                 │
│ Platform: Netflix           │
│ Genre: Drama, Crime         │
│ ⭐ Match: 92.5%            │
│ [███████░░] Progress Bar    │
└─────────────────────────────┘
```

**Styling**
```css
background: linear-gradient(135deg, rgba(233,69,96,0.1), rgba(255,0,110,0.1));
border: 2px solid rgba(233, 69, 96, 0.3);
border-radius: 15px;
padding: 10px;
backdrop-filter: blur(10px);
transition: all 0.3s ease;
```

**Hover State**
```css
transform: translateY(-8px);
box-shadow: 0 8px 25px rgba(255,0,110,0.6);
border-color: rgba(255,0,110,0.5);
```

### Buttons

**Primary Button**
```css
background: linear-gradient(90deg, #E94560, #FF006E);
color: white;
border: none;
border-radius: 10px;
padding: 12px 25px;
font-weight: 600;
cursor: pointer;
box-shadow: 0 5px 15px rgba(233,69,96,0.4);
transition: all 0.3s ease;
```

**Hover State**
```css
transform: translateY(-3px);
box-shadow: 0 8px 25px rgba(255,0,110,0.6);
```

**Active State**
```css
transform: translateY(-1px);
box-shadow: 0 5px 15px rgba(233,69,96,0.4);
```

### Input Fields

**Styling**
```css
background-color: rgba(255,255,255,0.1);
border: 2px solid rgba(233,69,96,0.5);
color: #EAEAEA;
border-radius: 10px;
padding: 12px;
font-size: 14px;
transition: all 0.3s ease;
```

**Focus State**
```css
background-color: rgba(255,0,110,0.1);
border-color: #FF006E;
box-shadow: 0 0 20px rgba(255,0,110,0.3);
outline: none;
```

### Tab Component

**Active Tab**
```css
color: #FF006E;
border-bottom: 3px solid #FF006E;
font-weight: 600;
```

**Inactive Tab**
```css
color: #94A3B8;
border-bottom: 2px solid transparent;
font-weight: 500;
```

---

## Layout System

### Grid Structure

#### Desktop (1920px+)
- Poster Grid: 5 columns
- Sidebar: 300px fixed width
- Main Content: Remaining space
- Column Gap: 20px
- Row Gap: 20px

#### Tablet (768-1919px)
- Poster Grid: 3-4 columns
- Sidebar: Collapsible or side-positioned
- Column Gap: 15px
- Row Gap: 15px

#### Mobile (<768px)
- Poster Grid: 2 columns
- Sidebar: Stacked or hidden
- Column Gap: 10px
- Row Gap: 10px
- Full width with padding

### Section Layout

```
Page (100vw)
├── Header (full width)
├── Divider
├── Main Content
│   ├── Sidebar (300px)
│   └── Content Area
│       ├── Tabs/Navigation
│       └── Content Grid
└── Footer (full width)
```

---

## Effects & Animations

### Glass Morphism Effect

**Card Glass Effect**
```css
background: rgba(255, 255, 255, 0.05);
backdrop-filter: blur(10px);
border: 1px solid rgba(255, 255, 255, 0.1);
border-radius: 15px;
```

### Hover Animations

**Card Lift**
```css
transform: translateY(-8px);
transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
```

**Glow Effect**
```css
box-shadow: 0 8px 25px rgba(255, 0, 110, 0.6);
transition: box-shadow 0.3s ease;
```

### Button Interactions

**Ripple-like Effect**
```css
/* On click */
animation: pulse 0.6s cubic-bezier(0.4, 0, 0.6, 1);
```

### Gradient Animations

**Text Gradient**
```css
background: linear-gradient(90deg, #E94560, #FF006E);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
background-clip: text;
```

### Transition Easing

**Standard**
```css
transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
```

**Ease-in-out**
```css
transition: all 0.3s ease-in-out;
```

**Linear** (for rotations)
```css
transition: transform 0.2s linear;
```

---

## Shadows & Depth

### Shadow System

```css
/* Small shadows (cards, buttons) */
box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);

/* Medium shadows (modals, elevated) */
box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);

/* Large shadows (prominent elements) */
box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);

/* Glow shadows (hover states) */
box-shadow: 0 8px 25px rgba(255, 0, 110, 0.6);

/* Inset shadows (glass effect) */
box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
```

---

## Border System

### Border Radius

```
Sharp:     0px
Subtle:    4px
Standard:  8px
Rounded:   12px
Pill:      9999px
```

### Border Colors

**Primary**
```css
border: 2px solid rgba(233, 69, 96, 0.3);
```

**Hover**
```css
border: 2px solid rgba(255, 0, 110, 0.5);
```

**Focus**
```css
border: 2px solid #FF006E;
```

---

## Responsive Design Breakpoints

### Mobile First Approach

```css
/* Mobile (default) */
@media (min-width: 0px) {
    cols_per_row = 2
    padding = 10px
    font-size = 14px
}

/* Tablet */
@media (min-width: 768px) {
    cols_per_row = 3-4
    padding = 15px
    font-size = 14px
}

/* Desktop */
@media (min-width: 1920px) {
    cols_per_row = 5
    padding = 20px
    font-size = 16px
}
```

---

## Accessibility Guidelines

### Color Contrast
- **Text on Background**: 4.5:1 minimum (WCAG AA)
- **UI Components**: 3:1 minimum
- **Focus Indicators**: Visible, clear

### Focus States
```css
:focus-visible {
    outline: 2px solid #FF006E;
    outline-offset: 2px;
}
```

### Keyboard Navigation
- Tab order follows visual flow
- Focus ring clearly visible
- No keyboard traps

### Text Alternatives
- Images have alt text
- Icons have aria-labels
- Metadata described

---

## Customization Examples

### Changing Primary Color

1. **Find CSS Section** (around line 40)
2. **Replace Colors**:
   ```python
   OLD: #E94560 and #FF006E
   NEW: Your colors
   ```

### Changing Grid Columns

1. **Find Grid Display** (around line 350)
2. **Update Value**:
   ```python
   cols_per_row = 5  # Change to desired number
   ```

### Changing Font Size

1. **Find Typography Section** (around line 80)
2. **Update Font Size**:
   ```python
   font-size: 16px;  # Change to desired size
   ```

### Adding Custom Theme

1. **Create CSS Variables**:
   ```css
   :root {
       --primary: #E94560;
       --secondary: #FF006E;
   }
   ```

2. **Use Variables**:
   ```css
   color: var(--primary);
   ```

---

## Dark Mode Considerations

### Current Implementation
- Always dark mode (no toggle)
- Optimized for dark backgrounds
- Good contrast ratios maintained

### Future: Light Mode Support

```css
/* Light theme variant */
[data-theme="light"] {
    --bg: #FFFFFF;
    --text: #0F3460;
    --border: rgba(0, 0, 0, 0.1);
}
```

---

## Animation Guidelines

### When to Animate
✅ **DO animate**:
- Hover states
- Button clicks
- Page transitions
- Loading states
- Hover over cards

❌ **DON'T animate**:
- Page load (can feel slow)
- Form submissions (seems stuck)
- Errors (feels jarring)
- Text changes (distracting)

### Animation Duration
- Quick: 150ms (button hover)
- Standard: 300ms (transitions)
- Slow: 500ms+ (important changes)

---

## Component States

### Button States

| State | Styling |
|-------|---------|
| Default | Gradient bg, normal shadow |
| Hover | Lifted position, glow shadow |
| Active | Slight depression |
| Disabled | Reduced opacity |
| Focus | Focus ring outline |

### Card States

| State | Styling |
|-------|---------|
| Default | Glass effect, border |
| Hover | Lifted, glow, border highlight |
| Focus | Focus ring |
| Error | Red border, warning color |

### Input States

| State | Styling |
|-------|---------|
| Default | Subtle border |
| Hover | Darker border |
| Focus | Magenta border, glow |
| Filled | Active state styling |
| Error | Red border, error message |
| Disabled | Reduced opacity |

---

## Best Practices

1. **Consistency**: Use the color palette consistently
2. **Spacing**: Follow spacing scale, don't invent gaps
3. **Typography**: Use defined sizes from scale
4. **Shadows**: Use shadow system, don't custom shadow
5. **Borders**: Use border radius system
6. **Animations**: Keep transitions smooth (0.3s default)
7. **Accessibility**: Maintain contrast ratios
8. **Responsive**: Test on all breakpoints

---

## Performance Considerations

- Use CSS over JavaScript for animations
- Minimize shadow blur radius (performance)
- Debounce scroll events
- Cache image resources
- Lazy load components
- Use will-change sparingly

---

## Testing Checklist

- [ ] Colors have sufficient contrast
- [ ] Animations are smooth (60fps)
- [ ] Responsive on mobile/tablet
- [ ] Focus states are visible
- [ ] Keyboard navigation works
- [ ] Images load correctly
- [ ] Forms are accessible
- [ ] Performance is acceptable

---

## Resources

- **Color Palette**: See "Color System" section
- **Typography**: See "Typography System" section
- **Spacing**: See "Spacing System" section
- **Components**: See "Component Design" section

---

**For questions about design customization, refer to specific sections above!**
