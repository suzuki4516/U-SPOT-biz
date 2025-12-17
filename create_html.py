# -*- coding: utf-8 -*-
import os
import urllib.parse

project_path = r'c:\Users\Victu\OneDrive\Desktop\Ai関連\hp_development\projects\hp\Usen関連\U-SPOT-biz'
images_path = os.path.join(project_path, 'images')

# Get all jpg files and sort them
jpg_files = [f for f in os.listdir(images_path) if f.lower().endswith('.jpg')]
jpg_files.sort()

print(f"Found {len(jpg_files)} images")

# Generate HTML
html_content = '''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>U-SPOT biz</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .image-wrapper {
            width: 100%;
            line-height: 0;
        }
        .image-wrapper img {
            width: 100%;
            height: auto;
            display: block;
        }
    </style>
</head>
<body>
    <div class="container">
'''

for jpg_file in jpg_files:
    encoded_name = urllib.parse.quote(jpg_file)
    html_content += f'        <div class="image-wrapper"><img src="images/{encoded_name}" alt="" loading="lazy"></div>\n'

html_content += '''    </div>
</body>
</html>
'''

# Write HTML file
output_path = os.path.join(project_path, 'index.html')
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"Created: {output_path}")
