from iridescent_bg import generate_iridescent_background, add_text, add_image
from PIL import Image

# Generate background with text and optional image
bg = generate_iridescent_background(width=1080, height=1080, enhance_vibrancy=True)
bg = add_text(bg, text="My Project", font_size=48, center_top=True)
# Add your own image (replace with your path)
bg = add_image(bg, side_image_path="path/to/your/image.jpg", width=540, position=(0, 0))
bg.save("my_image_background.png", dpi=(600, 600))

# Optional: No image, different color
bg_no_image = generate_iridescent_background(width=1080, height=1080, base_color='#00FF00', enhance_vibrancy=True)
bg_no_image = add_text(bg_no_image, text="Green Background", font_size=48, center_top=True)
bg_no_image.save("my_green_background.png", dpi=(600, 600))
