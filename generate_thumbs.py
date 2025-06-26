from PIL import Image, ImageDraw, ImageFont
import os

# Output thumbnails directories
os.makedirs("thumbs/150", exist_ok=True)
os.makedirs("thumbs/50", exist_ok=True)

for i in range(1, 11):
    img = Image.new("RGB", (300, 300), color=(20*i, 25*i, 15*i))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 100)
    except:
        font = ImageFont.load_default()

    text = str(i)
    bbox = draw.textbbox((0, 0), text, font=font)
    textwidth = bbox[2] - bbox[0]
    textheight = bbox[3] - bbox[1]
    draw.text(
        ((300 - textwidth) / 2, (300 - textheight) / 2),
        text,
        fill=(255, 255, 255),
        font=font
    )

    img_150 = img.copy()
    img_150.thumbnail((150, 150))
    img_150.save(f"thumbs/150/thumb{i}.jpg", quality=85)

    img_50 = img.copy()
    img_50.thumbnail((50, 50))
    img_50.save(f"thumbs/50/thumb{i}.jpg", quality=85)

print("Done. Thumbnails are now in thumbs/150 and thumbs/50.")

