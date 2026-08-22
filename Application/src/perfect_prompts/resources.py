from importlib.resources import files
from pathlib import Path


def icon_png_path() -> Path:
    """High-resolution transparent application icon for Qt/window surfaces."""
    return Path(str(files("perfect_prompts.assets").joinpath("perfect-prompts-icon.png")))


def icon_png_256_path() -> Path:
    """256 px transparent icon for native Linux icon-theme installation."""
    return Path(str(files("perfect_prompts.assets").joinpath("perfect-prompts-icon-256.png")))


def icon_ico_path() -> Path:
    """Multi-resolution Windows icon container."""
    return Path(str(files("perfect_prompts.assets").joinpath("perfect-prompts.ico")))
