from iridescent_bg import generate_iridescent_background, add_text
from PIL import Image

# Generate background with centered top text
bg = generate_iridescent_background(width=1080, height=1080, enhance_vibrancy=True)
bg = add_text(bg, text="My Title", font_size=48, center_top=True)
bg.save("my_text_background.png", dpi=(600, 600))

# Optional: Change base color and text position
bg_custom = generate_iridescent_background(width=1080, height=1080, base_color='white', enhance_vibrancy=True)
bg_custom = add_text(bg_custom, text="Custom Text", font_size=40, position=(100, 100))
bg_custom.save("my_custom_text_background.png", dpi=(600, 600))
