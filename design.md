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

## Motion redesign
The current page must use code-rendered product UI instead of the original three promotional images. Hero composition follows the supplied XRadar reference with a purple palette, a floating X tile, pill actions, and a browser-framed live concept demo. The 12-second local MP4 is a silent animated concept walkthrough, not a recording of the released extension.

All continuous decorative motion must pause from the fixed motion control and must respect reduced-motion preferences. Video must provide native playback controls, pause outside the viewport, and include a text equivalent. Manual tone selection must stop automatic cycling. Copy must copy the complete selected reply, including during a typing animation. Activity data must be labeled illustrative.

Validation: local browser confirmed zero image elements, 12-second video duration, 1280-pixel video width, active video playback, and global pause behavior. Remaining unchecked accessibility criteria above remain release checks.

## Product-content revision
Removed the fictional post, generated sample replies, simulated activity metrics, and concept video. Replaced them with a tone overview, supported-language section, and descriptions of usage tracking, weekly activity, and reply history grounded in the supplied product materials. No customer counts, pricing, reviews, or usage figures are asserted. Prior demo/video QA notes describe superseded versions. Motion controls now apply to decorative CSS animations only.

## Language removal
Removed all language-support claims, the language feature card, the dedicated language section, and language references in navigation, metadata, and FAQs per the user's correction. Reflowed feature cards to fill the available space. Pricing requires confirmed plan names, amounts, billing periods, and reply limits; do not invent pricing.

## Video-reference redesign
Analyzed the complete 8.98-second 720x1080 supplied reference at half-second intervals (18 frames). Its cream canvas, fixed icon rail, bold compact headings, purple/orange/red/brown cards, overlapping scroll motion, and bottom pill inspired the new editorial layout. Replaced the prior dark page with a complete light website using code-rendered artwork and the confirmed product content. Kept Free at 7 lifetime replies and Pro at $9/month with 3,000 individual variations. No language claims or fabricated social proof. Navigation, FAQs, motion pause and mobile overflow were checked in the local browser; mobile overflow was fixed. Reduced-motion disables sticky card transitions and decorative animation. Current source of truth: dist/editorial.css and dist/app.js.
