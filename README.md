# ASEMANI TRADING — Coming Soon

A static, dependency-free Coming Soon page for ASEMANI TRADING, intended for `https://asemanitrading.com/`.

## Files

| File | Purpose |
| --- | --- |
| `index.html` | Page markup, SEO / Open Graph metadata, Organization structured data |
| `styles.css` | All styling: palette, layout, responsive, print and forced-colours rules |
| `script.js` | Adds `noindex` on any host other than the production domain (preview protection) |
| `robots.txt` | Allows crawling |
| `favicon.ico`, `favicon.png`, `apple-touch-icon.png` | Icons generated from the official logo |
| `assets/logo/at-logo-source.jpg` | **Provenance.** Official A/T monogram exactly as embedded in the company Business Plan. Do not edit. |
| `assets/logo/at-logo-transparent.png` | The same mark, black on transparent. Basis for all derived files. Do not edit. |
| `assets/logo/at-logo-copper.png` | Display logo: the mark with the dark copper gradient applied |
| `tools/build-logo.py` | Regenerates the copper logo and icons from the transparent PNG |

No build step, frameworks, external fonts, remote assets, analytics, forms or backend.

## Local preview

Open `index.html` directly in a browser, or serve the folder on this machine only:

```sh
python3 -m http.server 8080 --bind 127.0.0.1
# then visit http://127.0.0.1:8080
```

## Logo

The logo is the official mark; its shape must not be redrawn or altered.
`tools/build-logo.py` only recolours it: every pixel keeps the transparency
(shape) of `at-logo-transparent.png` and receives a colour from a copper gradient.
The icons are downscaled copies on a champagne tile.

To regenerate after changing the gradient (requires Python with Pillow and NumPy):

```sh
python3 tools/build-logo.py
```

The source is 297 × 290 px, so the logo is displayed at no more than about 124 CSS px.
A vector original, if one is found, should replace these files.

## Search indexing

- Production (`asemanitrading.com`) is indexable; the canonical URL points there.
- On any other host, `script.js` adds `<meta name="robots" content="noindex">`.
  If the hosting platform can send an `X-Robots-Tag: noindex` header on preview
  deployments, enable that too; it is the more reliable safeguard.

## Editing

- Colours and font stacks are CSS custom properties at the top of `styles.css`.
- All copy lives in `index.html`.
- The page has no animation.
