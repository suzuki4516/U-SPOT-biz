# -*- coding: utf-8 -*-
import os
import fitz  # PyMuPDF

# Paths
project_path = r'c:\Users\Victu\OneDrive\Desktop\Ai関連\hp_development\projects\hp\Usen関連\U-SPOT-biz'
pdf_path = r'C:\Users\Victu\OneDrive\Desktop\20251209送付\（クイックイノベーション株式会社様）【提案書】U-SPOT_biz_提案資料_ver1.0.pdf'
images_path = os.path.join(project_path, 'images')

# Create images folder if not exists
os.makedirs(images_path, exist_ok=True)

# Open PDF
print("Converting PDF to images...")
doc = fitz.open(pdf_path)
total_pages = len(doc)

base_name = "（クイックイノベーション株式会社様）【提案書】U-SPOT_biz_提案資料_ver1.0"

# Convert each page to image
for page_num in range(total_pages):
    page = doc[page_num]

    # Render page to image with high resolution (2x zoom)
    mat = fitz.Matrix(2, 2)  # 2x zoom for better quality
    pix = page.get_pixmap(matrix=mat)

    # Save image
    page_num_str = str(page_num + 1).zfill(4)
    output_path = os.path.join(images_path, f'{base_name}_page-{page_num_str}.jpg')
    pix.save(output_path)
    print(f"Saved page {page_num + 1}: {output_path}")

doc.close()
print(f"\nTotal pages converted: {total_pages}")
