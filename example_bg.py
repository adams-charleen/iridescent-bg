# Copyright (c) 2025 Charleen Adams
# Licensed under the MIT License. See the LICENSE file for details.

from iridescent_bg import generate_iridescent_background
from PIL import Image

# Generate a black-based iridescent background (default)
bg = generate_iridescent_background(width=1080, height=1080, enhance_vibrancy=True)
bg.save("my_background.png", dpi=(600, 600))

# Optional: Customize base color (e.g., red)
bg_custom = generate_iridescent_background(width=1080, height=1080, base_color='#FF0000', enhance_vibrancy=True)
bg_custom.save("my_red_background.png", dpi=(600, 600))
