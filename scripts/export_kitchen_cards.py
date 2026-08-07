# -*- coding: utf-8 -*-
"""Crop/export kitchen category card images as square WebP."""

from pathlib import Path
from PIL import Image
import numpy as np

ROOT = Path(r"H:\SkardSoft\StationOneCafe")
SRC = Path(r"C:\Users\Jeck\.cursor\projects\h-SkardSoft-StationOneCafe\assets")
OUT = ROOT / "public" / "assets"
OUT.mkdir(parents=True, exist_ok=True)

SIZE = 900
QUALITY = 78

SOURCES = {
    "kitchen-kompaniya.webp": "c__Users_Jeck_AppData_Roaming_Cursor_User_workspaceStorage_88dd81690097186c6c3247159f166bb3_images_624643788_18085853573141749_638337670858511965_n-5f9b68ba-9185-4461-9932-48b545b23d47.png",
    "kitchen-zakuski.webp": "c__Users_Jeck_AppData_Roaming_Cursor_User_workspaceStorage_88dd81690097186c6c3247159f166bb3_images_623514843_18057673661655568_1299293980754078358_n-d9ce70bd-f242-4e5d-acff-4bb8564c6803.png",
    "kitchen-recommend.webp": "c__Users_Jeck_AppData_Roaming_Cursor_User_workspaceStorage_88dd81690097186c6c3247159f166bb3_images_558974965_18025563809741762_6274901206733803498_n-0d291260-9731-4c59-8533-6df5ea9694a7.png",
    "kitchen-salaty.webp": "c__Users_Jeck_AppData_Roaming_Cursor_User_workspaceStorage_88dd81690097186c6c3247159f166bb3_images_626277543_18083215433240129_5069482095334536922_n-15fc9dbc-1c41-4513-94a8-469067d47263.png",
    "kitchen-desserty.webp": "c__Users_Jeck_AppData_Roaming_Cursor_User_workspaceStorage_88dd81690097186c6c3247159f166bb3_images_626271976_18097431529934256_255768507969049092_n-8cdab772-f72a-4385-9c62-1b37d301e899.png",
    "kitchen-pizza.webp": "c__Users_Jeck_AppData_Roaming_Cursor_User_workspaceStorage_88dd81690097186c6c3247159f166bb3_images_621612033_17960108832030636_6285785154045567292_n-07ffcc12-2c21-4d66-89c7-88104e284fe3.png",
    "kitchen-uglyakh.webp": "c__Users_Jeck_AppData_Roaming_Cursor_User_workspaceStorage_88dd81690097186c6c3247159f166bb3_images_619910846_17992260662747212_1228672192607842079_n-847159fe-5f00-42e0-a19b-800e8f16f82e.png",
    "kitchen-pasta.webp": "c__Users_Jeck_AppData_Roaming_Cursor_User_workspaceStorage_88dd81690097186c6c3247159f166bb3_images_image-f9a91bbd-518c-4e47-8668-6639e5356673.png",
}


def square_crop(im: Image.Image, focus=(0.5, 0.45)) -> Image.Image:
    w, h = im.size
    side = min(w, h)
    cx, cy = int(w * focus[0]), int(h * focus[1])
    left = max(0, min(cx - side // 2, w - side))
    top = max(0, min(cy - side // 2, h - side))
    return im.crop((left, top, left + side, top + side))


def crop_recommend_clean(im: Image.Image) -> Image.Image:
    """Remove sage border + bottom text overlay; keep food photo."""
    rgb = im.convert("RGB")
    arr = np.asarray(rgb)
    h, w = arr.shape[:2]

    # Detect near-white text box: bright rows in lower half
    gray = arr.mean(axis=2)
    row_bright = (gray > 210).mean(axis=1)
    # Find where large white overlay starts (bottom third typically)
    overlay_start = h
    for y in range(int(h * 0.45), h):
        if row_bright[y] > 0.35:
            overlay_start = y
            break

    # Detect sage/green border: edges with low saturation green-gray
    # Sample border pixels - light sage around #c8d0c0-ish
    def is_border_pixel(px):
        r, g, b = px.astype(float)
        return g > r - 5 and g > b - 5 and 140 < g < 210 and abs(r - b) < 40 and (g - min(r, b)) > 5

    # Find content inset by scanning inward until non-border
    def inset_from_edge(axis: str) -> int:
        limit = w if axis == "x" else h
        for i in range(min(80, limit // 4)):
            if axis == "x":
                col = arr[:, i]
            else:
                col = arr[i, :]
            border_ratio = np.mean([is_border_pixel(p) for p in col[:: max(1, len(col) // 40)]])
            # also check uniform light green via mean
            mean = col.mean(axis=0)
            sage = mean[1] > mean[0] and mean[1] > mean[2] and 150 < mean[1] < 205
            if border_ratio < 0.4 and not sage:
                return max(0, i - 1)
        return 0

    left = inset_from_edge("x")
    top = inset_from_edge("y")
    # right/bottom: mirror scan
    right = w
    for i in range(w - 1, max(w - 80, w // 2), -1):
        col = arr[:, i]
        mean = col.mean(axis=0)
        sage = mean[1] > mean[0] and mean[1] > mean[2] and 150 < mean[1] < 205
        if not sage:
            right = i + 1
            break
    bottom = min(overlay_start - 4, h)
    for i in range(min(overlay_start, h) - 1, max(0, min(overlay_start, h) - 60), -1):
        row = arr[i, :]
        mean = row.mean(axis=0)
        # stop above white overlay fluff
        if mean.mean() < 200:
            bottom = i + 1
            break

    left = max(0, left)
    top = max(0, top)
    right = min(w, max(right, left + 50))
    bottom = min(h, max(bottom, top + 50))

    cropped = rgb.crop((left, top, right, bottom))
    print(f"  recommend crop box=({left},{top},{right},{bottom}) from {w}x{h}")
    return square_crop(cropped, focus=(0.5, 0.48))


def export(name: str, src_name: str, special: str | None = None, focus=(0.5, 0.45)):
    src = SRC / src_name
    im = Image.open(src).convert("RGB")
    print(f"{name}: {im.size}")
    if special == "recommend":
        out_im = crop_recommend_clean(im)
    elif special == "desserty":
        # focus on plate, crop out arms/shoes
        out_im = square_crop(im, focus=(0.5, 0.38))
    elif special == "zakuski":
        out_im = square_crop(im, focus=(0.52, 0.42))
    elif special == "uglyakh":
        out_im = square_crop(im, focus=(0.48, 0.55))
    elif special == "pasta":
        out_im = square_crop(im, focus=(0.48, 0.55))
    elif special == "salaty":
        out_im = square_crop(im, focus=(0.52, 0.52))
    else:
        out_im = square_crop(im, focus=focus)

    out_im = out_im.resize((SIZE, SIZE), Image.Resampling.LANCZOS)
    dest = OUT / name
    out_im.save(dest, "WEBP", quality=QUALITY, method=6)
    print(f"  -> {dest.name} {dest.stat().st_size // 1024}KB")


def main():
    export("kitchen-kompaniya.webp", SOURCES["kitchen-kompaniya.webp"], focus=(0.5, 0.48))
    export("kitchen-zakuski.webp", SOURCES["kitchen-zakuski.webp"], special="zakuski")
    export("kitchen-recommend.webp", SOURCES["kitchen-recommend.webp"], special="recommend")
    export("kitchen-salaty.webp", SOURCES["kitchen-salaty.webp"], special="salaty")
    export("kitchen-desserty.webp", SOURCES["kitchen-desserty.webp"], special="desserty")
    export("kitchen-pizza.webp", SOURCES["kitchen-pizza.webp"], focus=(0.42, 0.48))
    export("kitchen-uglyakh.webp", SOURCES["kitchen-uglyakh.webp"], special="uglyakh")
    export("kitchen-pasta.webp", SOURCES["kitchen-pasta.webp"], special="pasta")


if __name__ == "__main__":
    main()
