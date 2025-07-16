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
