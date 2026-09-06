# People photographs — 6 September 2026

Base: main `80f49e4295639d90216583a234d11b89912e4708`, after PR #21 merged.

## Scope

A shared People photo partial adds proportional q85 WebP sources for the three existing group photographs and 18 member portraits. The welcome photograph is reused on Home and People: 21 originals, 22 placements, 36 unique derivatives. All original files remain byte-for-byte intact and remain the fallback image sources. Captions, alternative text, member ordering and profiles are unchanged.

Group photographs offer 480, 800 and original width; portraits offer 270, 480, 800 where smaller than the original, plus original width. Small original portraits are not upscaled. Each image now reports its actual intrinsic dimensions, replacing the hard-coded 320 × 320 portrait attributes. Existing square portrait framing and group-photo aspect ratios are preserved. Only the People hero retains high fetch priority; the other placements retain lazy loading.

The 2025 welcome original is 1,914,729 bytes. Generated versions are 38,582 bytes at 480 pixels, 89,752 at 800, and 179,006 at 1200. This is an asset-size comparison, not a browser speed measurement. Sources are existing repository photos; no identities, captions or new photographic claims were inferred.

## Validation

Production Hugo build passes (895 pages). Scanned 536 generated index pages: all 250 populated local image references resolve. Checked 22 picture placements and 36 unique WebP files for actual width, aspect ratio, no upscaling and unchanged fallback bytes. Main-element visible text matches the prior output throughout the site. The 91-publication and seven conceptual-image / 28-WebP baseline audits pass.

Browser viewport testing remains pending. No production merge or configuration change. Remaining paper-figure sourcing priorities are PyraE2E and the selected JACS paper; legacy image descriptions still need bounded review.
