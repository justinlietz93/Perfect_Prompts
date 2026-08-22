from importlib.resources import files
from pathlib import Path


GUI_ICON_SIZES = (16, 24, 32, 48, 64, 256)


def icon_png_path(size: int | None = None) -> Path:
    """Return the transparent application icon, optionally at a native raster size."""
    name = "perfect-prompts-icon.png" if size is None else f"perfect-prompts-icon-{size}.png"
    return Path(str(files("perfect_prompts.assets").joinpath(name)))


def icon_png_256_path() -> Path:
    """256 px transparent icon for native Linux icon-theme installation."""
    return icon_png_path(256)


def icon_ico_path() -> Path:
    """Multi-resolution Windows icon container."""
    return Path(str(files("perfect_prompts.assets").joinpath("perfect-prompts.ico")))


def application_icon():
    """Build a Qt icon with native raster sizes instead of downscaling the 1024 px master."""
    from PySide6.QtCore import QSize
    from PySide6.QtGui import QIcon

    icon = QIcon()
    for size in GUI_ICON_SIZES:
        path = icon_png_path(size)
        if path.is_file():
            icon.addFile(str(path), QSize(size, size))
    if icon.isNull():
        icon.addFile(str(icon_png_path()))
    return icon
