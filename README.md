# ASEMANI TRADING — Coming Soon

A static, dependency-free Coming Soon page for ASEMANI TRADING (AT), planned for `asemanitrading.com`.

## Files

| File          | Purpose                                                        |
| ------------- | -------------------------------------------------------------- |
| `index.html`  | Page markup, SEO / Open Graph metadata, JSON-LD organization   |
| `styles.css`  | All styling, background, responsive rules and motion           |
| `script.js`   | Updates the footer year (optional; the page works without JS)  |
| `favicon.svg` | Vector "AT" favicon                                            |
| `robots.txt`  | Allows crawling                                                |

No build step, no frameworks, no external fonts, scripts, images or analytics.

## Local preview

Open `index.html` directly in a browser, or serve the folder:

```sh
python3 -m http.server 8080
# then visit http://localhost:8080
```

## Editing

- Colours and font stacks are CSS custom properties at the top of `styles.css`.
- All copy lives in `index.html`.
- Animations are disabled automatically for visitors who prefer reduced motion.
