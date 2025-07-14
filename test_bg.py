import sys
try:
    from iridescent_bg import generate_iridescent_background
    print("Successfully imported iridescent_bg")
    bg = generate_iridescent_background(width=1080, height=1080, base_color="black", enhance_vibrancy=True, full_canvas=True)
    print("Generated enhanced background image")
    bg.save("/Users/charleenadams/iridescent-bg/test_background.png", dpi=(600, 600))
    print("Saved image to /Users/charleenadams/iridescent-bg/test_background.png")
except Exception as e:
    print(f"Error: {str(e)}", file=sys.stderr)
