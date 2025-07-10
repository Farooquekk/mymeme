from PIL import Image, ImageDraw, ImageFont
import textwrap
import os

def create_meme(image_path, top_text, bottom_text, output_path="output_meme.jpg"):
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    img = Image.open(image_path).convert("RGB")  # Converting PNG to RGB (if needed)
    draw = ImageDraw.Draw(img)
    width, height = img.size

    # Loading font 
    try:
        font = ImageFont.truetype("impact.ttf", size=int(height / 10))
    except IOError:
        font = ImageFont.truetype("arialbd.ttf", size=int(height / 10))  # Arial Bold

    def draw_text_wrapped(text, y_pos):
        lines = textwrap.wrap(text.upper(), width=20)
        line_height = font.getbbox("Ay")[3] + 10
        for i, line in enumerate(lines):
            # line_width = draw.textlength(line, font=font)
            x = width / 2
            y = y_pos + i * line_height

            # Drawing outline
            for dx in [-2, -1, 1, 2]:
                for dy in [-2, -1, 1, 2]:
                    draw.text((x + dx, y + dy), line, font=font, fill="black", anchor="ma")

            # Drawing main text
            draw.text((x, y), line, font=font, fill="#ffcc00", anchor="ma") 

    draw_text_wrapped(top_text, 15)
    draw_text_wrapped(bottom_text, height - int(height / 3))

    img.save(output_path)
