# Copyright (c) 2025 Charleen Adams
# Licensed under the MIT License. See the LICENSE file for details.

import sys
try:
    from iridescent_bg import generate_iridescent_background, add_text, add_image
    print("Successfully imported iridescent_bg modules")
    bg = generate_iridescent_background(width=1080, height=1080, base_color='black', enhance_vibrancy=True, full_canvas=True)
    print("Generated enhanced background image")
    bg = add_text(bg, text="Sample Text", font_size=48, center_top=True)
    print("Added centered top text to image")
    # Optional image, comment out to test without it
    bg = add_image(bg, side_image_path="/Users/charleenadams/sp_instagram/free_gift.jpg", width=540, position=(0, 0))
    print("Added side image to image")
    bg.save("/Users/charleenadams/iridescent-bg/installed_test.png", dpi=(600, 600))
    print("Saved image to /Users/charleenadams/iridescent-bg/installed_test.png")
except Exception as e:
    print(f"Error: {str(e)}", file=sys.stderr)
