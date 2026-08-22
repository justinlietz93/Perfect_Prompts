"""Build native Perfect Prompts application icon assets from the supplied logo.

The user-supplied source artwork is preserved unchanged under
``Application/assets/source/``.  The derived app icon removes only the exterior
black canvas connected to the image boundary, preserves the artwork itself,
adds transparent breathing room, and emits platform-ready PNG/ICO assets.
"""

from __future__ import annotations

from pathlib import Path
import shutil

from PIL import Image, ImageChops, ImageDraw, ImageFilter

APPLICATION_DIR = Path(__file__).resolve().parents[1]
SOURCE = APPLICATION_DIR / "assets" / "source" / "perfect-prompts-logo-source.png"
PUBLIC_ASSETS = APPLICATION_DIR / "assets"
PACKAGE_ASSETS = APPLICATION_DIR / "src" / "perfect_prompts" / "assets"

MASTER_SIZE = 1024
ARTWORK_SIZE = 900
DARK_THRESHOLD = 22
ICO_SIZES = (16, 20, 24, 32, 40, 48, 64, 96, 128, 256)
PNG_SIZES = (16, 24, 32, 48, 64, 128, 256, 512)


def _foreground_mask(image: Image.Image) -> Image.Image:
    """Remove only dark background connected to the outer canvas.

    A simple chroma/color key would punch holes through the icon because the
    artwork itself intentionally uses very dark navy/black tones.  Flood-filling
    from the canvas edge instead lets the luminous rounded frame protect the
    dark interior while the exterior square background becomes transparent.
    """

    red, green, blue, _alpha = image.convert("RGBA").split()
    brightest = ImageChops.lighter(ImageChops.lighter(red, green), blue)
    traversable_dark = brightest.point(
        lambda value: 255 if value <= DARK_THRESHOLD else 0,
        mode="L",
    )

    flooded = traversable_dark.copy()
    ImageDraw.floodfill(flooded, (0, 0), 128, thresh=0)
    foreground = flooded.point(lambda value: 0 if value == 128 else 255, mode="L")
    return foreground.filter(ImageFilter.GaussianBlur(1.2))


def build_master(source: Path = SOURCE) -> Image.Image:
    image = Image.open(source).convert("RGBA")
    mask = _foreground_mask(image)
    image.putalpha(mask)

    bbox = mask.getbbox()
    if bbox is None:
        raise RuntimeError("Could not locate Perfect Prompts icon artwork")

    x0, y0, x1, y1 = bbox
    cx = (x0 + x1) / 2
    cy = (y0 + y1) / 2
    side = max(x1 - x0, y1 - y0) * 1.015
    box = (
        int(round(cx - side / 2)),
        int(round(cy - side / 2)),
        int(round(cx + side / 2)),
        int(round(cy + side / 2)),
    )
    artwork = image.crop(box)
    artwork.thumbnail((ARTWORK_SIZE, ARTWORK_SIZE), Image.Resampling.LANCZOS)

    master = Image.new("RGBA", (MASTER_SIZE, MASTER_SIZE), (0, 0, 0, 0))
    offset = ((MASTER_SIZE - artwork.width) // 2, (MASTER_SIZE - artwork.height) // 2)
    master.alpha_composite(artwork, offset)
    return master


def _save_png_set(master: Image.Image, root: Path) -> None:
    icon_root = root / "icons" / "hicolor"
    for size in PNG_SIZES:
        target = icon_root / f"{size}x{size}" / "apps" / "perfect-prompts.png"
        target.parent.mkdir(parents=True, exist_ok=True)
        master.resize((size, size), Image.Resampling.LANCZOS).save(target, optimize=True)


def main() -> int:
    PUBLIC_ASSETS.mkdir(parents=True, exist_ok=True)
    PACKAGE_ASSETS.mkdir(parents=True, exist_ok=True)

    master = build_master()
    public_master = PUBLIC_ASSETS / "perfect-prompts-icon.png"
    public_256 = PUBLIC_ASSETS / "perfect-prompts-icon-256.png"
    public_ico = PUBLIC_ASSETS / "perfect-prompts.ico"

    master.save(public_master, optimize=True)
    master.resize((256, 256), Image.Resampling.LANCZOS).save(public_256, optimize=True)
    master.save(public_ico, format="ICO", sizes=[(size, size) for size in ICO_SIZES])
    _save_png_set(master, PUBLIC_ASSETS)

    shutil.copy2(public_master, PACKAGE_ASSETS / public_master.name)
    shutil.copy2(public_ico, PACKAGE_ASSETS / public_ico.name)
    for size in (16, 24, 32, 48, 64, 256):
        source = PUBLIC_ASSETS / "icons" / "hicolor" / f"{size}x{size}" / "apps" / "perfect-prompts.png"
        shutil.copy2(source, PACKAGE_ASSETS / f"perfect-prompts-icon-{size}.png")

    print(f"Built transparent master: {public_master}")
    print(f"Built Linux PNG: {public_256}")
    print(f"Built Windows ICO: {public_ico}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
