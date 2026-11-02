# ReplyVibe design guidance

## Context and goals
Showcase the ReplyVibe Chrome extension with a restrained neon-purple identity, clear product previews, and an interactive tone demo. XRadar is a layout reference; ReplyVibe is the product. The extension is in Chrome Web Store review. The page must not claim it is available to install.

## Design tokens and foundations
The implementation source of truth is `dist/style.css` at `:root`. Components must use semantic color variables: `--bg`, `--surface`, `--raised`, `--text`, `--muted`, `--purple`, `--pink`, `--line`, and `--accent`. Typography should use Inter with the supplied system fallback. Spacing should follow the eight-pixel foundation with compact optical adjustments. Major sections must use consistent page gutters. Main headings should scale responsively. Purple glows should frame product content without reducing legibility.

## Component rules
- Navigation must use real anchors with descriptive labels. Small screens must retain primary feature and demo navigation. Links must show visible hover, focus-visible, and active feedback. Disabled, loading, and error states are not applicable to static anchors.
- Buttons must have visible default, hover, focus-visible, and active states. Disabled actions must use the native disabled attribute. The launch button must remain disabled during store review. Async copy completion must be confirmed in its label; failure must select the reply for manual copying. Copy does not need a loading state because its operation completes immediately; any future network operation must expose loading, prevent duplicate submissions, and show a recoverable error.
- Tone and screenshot controls must use native buttons and `aria-pressed`. Pointer, touch, Enter, and Space must select the same state. The selected tone must update the live reply region. Reply content must wrap and the card must grow for long text. Missing demo data must retain a readable explanatory message rather than a blank panel.
- Feature cards are noninteractive. They must not show pointer cursors or simulated hover affordances. Default presentation must remain readable without animation; focus, active, disabled, loading, and error states are not applicable.
- Screenshot previews must preserve aspect ratio, provide descriptive alt text, and remain within the viewport. Loading must not collapse the image space. If an image cannot load, its descriptive alternative must remain available.
- FAQ disclosures must use native details/summary. Enter and Space must toggle the focused disclosure. Long answers must wrap without clipping. Open and closed states must be visually distinct. Disabled, loading, and error states are not applicable to local static content.

## Accessibility acceptance criteria
- All controls must be reachable and operable by keyboard; focus must remain visible. Pass: Tab through the page and operate tone buttons, preview tabs, and FAQs without a pointer.
- Text must meet WCAG AA contrast: 4.5:1 for normal text and 3:1 for large text; essential control boundaries must meet 3:1. Verify with a contrast checker before public release.
- Layout must avoid horizontal overflow at 320 CSS pixels and at 200% zoom. Text must not be clipped.
- Touch controls must provide at least 24 by 24 CSS pixels, with 40-pixel targets preferred.
- Reduced-motion preferences must suppress smooth scrolling and transitions.
- Demo tone changes must be announced through the polite live region. Decorative symbols must not be used as the sole control labels.

## Content and tone
Copy should be concise, warm, and specific. Use “Your words. Your vibe.” and “Try the demo.” The sample post and generated text must remain labeled as illustrative. Claims must be grounded in the supplied product material. Fake reviews, user counts, pricing, and endorsements must not be added.

## Anti-patterns and migration
Components must not copy XRadar branding or its blue palette. Background glows must not overpower content. Install links must not point to unrelated listings. When approved, replace coming-soon messaging and the disabled button with the verified Chrome Web Store URL, and update the FAQ. Do not imply this static demo connects to AI.

## QA checklist
- [ ] Desktop and mobile visual inspection completed.
- [ ] Keyboard navigation and focus indicators verified.
- [ ] Contrast measured against AA requirements.
- [ ] No overflow at 320px or 200% zoom.
- [ ] All four tones and both product previews tested.
- [ ] Clipboard success and fallback reviewed.
- [ ] FAQ disclosure behavior checked.
- [x] JavaScript syntax checked.
- [x] Review-in-progress state reflected throughout.
- [x] Supplied product screenshots included locally.

Browser QA is pending if the execution environment cannot route the local preview.
