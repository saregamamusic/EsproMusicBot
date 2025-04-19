import os
import re
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont
from unidecode import unidecode
from EsproMusic import app
from config import YOUTUBE_IMG_URL


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


def clear(text):
    list = text.split(" ")
    title = ""
    for i in list:
        if len(title) + len(i) < 60:
            title += " " + i
    return title.strip()


async def get_thumb(videoid):
    try:
        title = "Aapki Custom Video Title"
        duration = "3:45"
        channel = "Custom Channel"
        views = "1.2M Views"

        your_image_path = "IMG_20250417_090653_759.jpg"
        youtube = Image.open(your_image_path)
        image1 = changeImageSize(1280, 720, youtube)
        image2 = image1.convert("RGBA")
        background = image2.filter(filter=ImageFilter.BoxBlur(10))
        enhancer = ImageEnhance.Brightness(background)
        background = enhancer.enhance(0.5)
        draw = ImageDraw.Draw(background)

        arial = ImageFont.truetype("EsproMusic/assets/font2.ttf", 30)
        font = ImageFont.truetype("EsproMusic/assets/font.ttf", 30)

        draw.text((1110, 8), unidecode(app.name), fill="white", font=arial)
        draw.text((55, 560), f"{channel} | {views[:23]}", (255, 255, 255), font=arial)
        draw.text((57, 60), clear(title), (255, 255, 255), font=font)

        draw.line([(55, 660), (1220, 660)], fill="white", width=5, joint="curve")
        draw.ellipse([(918, 648), (942, 672)], outline="white", fill="white", width=15)
        draw.text((36, 685), "00:00", (255, 255, 255), font=arial)
        draw.text((1185, 685), f"{duration[:23]}", (255, 255, 255), font=arial)

        final_path = f"cache/{videoid}.png"
        background.save(final_path)
        return final_path

    except Exception as e:
        print(e)
        return YOUTUBE_IMG_URL
