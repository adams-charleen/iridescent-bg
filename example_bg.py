# Copyright (c) 2025 Charleen Adams
# Licensed under the MIT License. See the LICENSE file for details.

from iridescent_bg import generate_iridescent_background, add_text

# Generate a wide, slightly taller background
bg = generate_iridescent_background(width=1600, height=240, enhance_vibrancy=True)

# Add centered white text
final_logo = add_text(
    bg,
    text="iridescent-bg",
    font_size=100,
    font_color=(255, 255, 255),
    position=(480, 70)
)

# Save the logo
final_logo.save("logo.png", dpi=(600, 600))

from iridescent_bg import generate_iridescent_background
from PIL import Image

# Generate a black-based iridescent background (default)
bg = generate_iridescent_background(width=1080, height=1080, enhance_vibrancy=True)
bg.save("my_background.png", dpi=(600, 600))

# Optional: Customize base color (e.g., red)
bg_custom = generate_iridescent_background(width=1080, height=1080, base_color='#FF0000', enhance_vibrancy=True)
bg_custom.save("my_red_background.png", dpi=(600, 600))
