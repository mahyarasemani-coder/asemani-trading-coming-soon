#!/usr/bin/env python3
"""Generate the display logo and favicons from the official A/T monogram.

Input  : assets/logo/at-logo-transparent.png  (official mark, black on transparent)
Outputs: assets/logo/at-logo-copper.png, favicon.ico, favicon.png, apple-touch-icon.png

The mark's geometry is never altered: every output pixel keeps the source
alpha (shape) value; only its colour is replaced by a copper gradient.
Favicons are plain downscaled copies of that result.

Requires Pillow and NumPy. Only needed if the logo files must be regenerated;
the website itself has no build step.

Usage (from the repository root):  python3 tools/build-logo.py
"""
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "assets/logo/at-logo-transparent.png"

# Dark copper, restrained highlight. (position 0..1 along the diagonal, RGB)
COPPER_STOPS = [
    (0.00, (0x5E, 0x32, 0x1A)),
    (0.30, (0x7F, 0x49, 0x27)),
    (0.48, (0x9E, 0x65, 0x3B)),  # soft highlight band
    (0.66, (0x76, 0x41, 0x21)),
    (1.00, (0x48, 0x25, 0x12)),
]
PAGE_BACKGROUND = (0xEC, 0xE2, 0xC6)  # champagne, matches --champagne in styles.css


def copper_gradient(width: int, height: int) -> np.ndarray:
    """RGB array with a top-left to bottom-right copper gradient."""
    ys, xs = np.mgrid[0:height, 0:width]
    t = (xs / (width - 1) * 0.45 + ys / (height - 1) * 0.55).clip(0, 1)
    positions = [p for p, _ in COPPER_STOPS]
    channels = [
        np.interp(t, positions, [c[i] for _, c in COPPER_STOPS]) for i in range(3)
    ]
    return np.stack(channels, axis=-1).round().astype("uint8")


def tile(logo: Image.Image, size: int, margin: float, radius: float) -> Image.Image:
    """Logo centred on a champagne tile (keeps the mark legible on dark tabs)."""
    scale = 4  # supersample for clean rounded corners
    big = size * scale
    canvas = Image.new("RGBA", (big, big), (0, 0, 0, 0))
    mask = Image.new("L", (big, big), 0)
    from PIL import ImageDraw

    ImageDraw.Draw(mask).rounded_rectangle(
        (0, 0, big - 1, big - 1), radius=int(big * radius), fill=255
    )
    canvas.paste(Image.new("RGBA", (big, big), PAGE_BACKGROUND + (255,)), (0, 0), mask)
    box = int(big * (1 - 2 * margin))
    ratio = min(box / logo.width, box / logo.height)
    resized = logo.resize(
        (round(logo.width * ratio), round(logo.height * ratio)), Image.LANCZOS
    )
    canvas.alpha_composite(
        resized, ((big - resized.width) // 2, (big - resized.height) // 2)
    )
    return canvas.resize((size, size), Image.LANCZOS)


def main() -> None:
    source = Image.open(SOURCE).convert("RGBA")
    alpha = np.asarray(source)[..., 3]

    rgba = np.dstack([copper_gradient(source.width, source.height), alpha])
    copper = Image.fromarray(rgba, "RGBA")
    copper.save(ROOT / "assets/logo/at-logo-copper.png", optimize=True)

    tile(copper, 48, margin=0.10, radius=0.18).save(
        ROOT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)]
    )
    tile(copper, 96, margin=0.10, radius=0.18).save(ROOT / "favicon.png", optimize=True)
    tile(copper, 180, margin=0.16, radius=0.0).convert("RGB").save(
        ROOT / "apple-touch-icon.png", optimize=True
    )


if __name__ == "__main__":
    main()
