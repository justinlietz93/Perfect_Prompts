from hashlib import sha256
from pathlib import Path

from PIL import Image


APPLICATION = Path(__file__).resolve().parents[1]
SOURCE_HASH = "e655cb15971ed1e035183dba432db12e944342907d461d68eaa0f94c2d94bf18"


def test_original_logo_source_is_preserved_byte_for_byte():
    source = APPLICATION / "assets" / "source" / "perfect-prompts-logo-source.png"
    assert sha256(source.read_bytes()).hexdigest() == SOURCE_HASH


def test_master_icon_is_transparent_and_padded():
    icon = Image.open(APPLICATION / "assets" / "perfect-prompts-icon.png").convert("RGBA")
    assert icon.size == (1024, 1024)
    assert icon.getpixel((0, 0))[3] == 0
    assert icon.getpixel((1023, 1023))[3] == 0
    assert icon.getpixel((512, 512))[3] == 255
    bbox = icon.getchannel("A").getbbox()
    assert bbox is not None
    assert bbox[0] >= 40 and bbox[1] >= 40
    assert bbox[2] <= 984 and bbox[3] <= 984


def test_windows_icon_is_true_multiresolution_container():
    icon = Image.open(APPLICATION / "assets" / "perfect-prompts.ico")
    sizes = icon.ico.sizes()
    for size in {(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)}:
        assert size in sizes
    assert icon.convert("RGBA").getpixel((0, 0))[3] == 0


def test_linux_icon_is_transparent_png():
    icon = Image.open(APPLICATION / "assets" / "perfect-prompts-icon-256.png").convert("RGBA")
    assert icon.size == (256, 256)
    assert icon.getpixel((0, 0))[3] == 0
