# -*- coding: utf-8 -*-
"""Compress site images to WebP for production."""

from pathlib import Path
from PIL import Image

ROOT = Path(r"H:\SkardSoft\StationOneCafe")
PUBLIC = ROOT / "public"

# Keep alpha for these name fragments
ALPHA_KEYS = ("logo", "flourish", "yandex", "just-eat", "icon")

TARGETS = [
    ("assets/hero.png", 1920, 78),
    ("assets/hero-flourish.png", 960, 82),
    ("assets/hookah-square-enhanced.png", 1200, 78),
    ("assets/kitchen-breakfast.png", 1000, 78),
    ("assets/kitchen-lunch.png", 1000, 78),
    ("assets/kitchen-dinner.png", 1000, 78),
    ("assets/reviews-bg.png", 1600, 72),
    ("assets/review-elizaveta.png", 256, 80),
    ("assets/review-andrey.png", 256, 80),
    ("assets/review-tori.png", 256, 80),
    ("assets/621465960_18067678844550093_6426370961459551137_n.jpg", 1400, 76),
    ("assets/621994545_18067362602216362_5964215558239244974_n.jpg", 900, 76),
    ("assets/624634555_18096249614303539_8693718930694080913_n.jpg", 900, 76),
    ("assets/624772640_17985520190946305_7945716152227430879_n.jpg", 900, 76),
    ("assets/627337651_18350106856231994_3719591899379123701_n.jpg", 900, 76),
    ("assets/gallery-wine.jpg", 900, 76),
    ("assets/cafe-interior-without-people.png", 1400, 76),
    ("assets/622891114_18069939233428118_1565601425155871556_n.jpg", 900, 76),
    ("assets/626760662_18165613687364405_4345666885574126020_n.jpg", 900, 76),
    ("assets/623556418_18110118085646510_7634547381258020052_n.jpg", 900, 76),
    ("logo.png", 512, 85),
    ("logo-mini.png", 256, 85),
    ("icons/yandex-eda.png", 256, 85),
    ("icons/just-eat.png", 256, 85),
]


def needs_alpha(path: Path) -> bool:
    name = path.name.lower()
    return any(k in name for k in ALPHA_KEYS)


def to_webp(rel: str, max_edge: int, quality: int) -> None:
    src = PUBLIC / rel
    if not src.exists():
        print(f"skip missing: {rel}")
        return

    out = src.with_suffix(".webp")
    base = Image.open(src)

    if needs_alpha(src):
        im = base.convert("RGBA")
    else:
        if base.mode in ("RGBA", "LA") or (base.mode == "P" and "transparency" in base.info):
            rgba = base.convert("RGBA")
            bg = Image.new("RGB", rgba.size, (33, 34, 38))
            bg.paste(rgba, mask=rgba.split()[-1])
            im = bg
        else:
            im = base.convert("RGB")

    w, h = im.size
    scale = min(1.0, max_edge / max(w, h))
    if scale < 1:
        im = im.resize((max(1, int(w * scale)), max(1, int(h * scale))), Image.Resampling.LANCZOS)

    im.save(out, "WEBP", quality=quality, method=6)
    print(f"{rel} -> {out.name}: {src.stat().st_size // 1024}KB -> {out.stat().st_size // 1024}KB")


def main():
    for rel, edge, q in TARGETS:
        to_webp(rel, edge, q)


if __name__ == "__main__":
    main()
