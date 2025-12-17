# -*- coding: utf-8 -*-
import os
from PIL import Image, ImageDraw

project_path = r'c:\Users\Victu\OneDrive\Desktop\Ai関連\hp_development\projects\hp\Usen関連\U-SPOT-biz'
images_path = os.path.join(project_path, 'images')

# Get all jpg files
jpg_files = [f for f in os.listdir(images_path) if f.lower().endswith('.jpg')]
jpg_files.sort()

print(f"Processing {len(jpg_files)} images...")

for i, jpg_file in enumerate(jpg_files):
    file_path = os.path.join(images_path, jpg_file)
    img = Image.open(file_path)
    draw = ImageDraw.Draw(img)

    width, height = img.size

    # Remove only the logo text area (USEN NETWORKS | U-NEXT HOLDINGS)
    # Cover the logo area in the top right corner
    logo_box = (int(width * 0.65), 20, width, 160)
    draw.rectangle(logo_box, fill='white')

    # Remove bottom copyright text (©2023 USEN NETWORKS Co.,Ltd.)
    bottom_box = (0, height - 45, width, height)
    draw.rectangle(bottom_box, fill='white')

    # Save
    img.save(file_path, quality=95)
    print(f"Processed {i+1}/{len(jpg_files)}: {jpg_file}")

print("\nDone! All watermarks removed.")
