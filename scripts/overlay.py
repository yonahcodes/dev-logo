from PIL import Image
from pathlib import Path

# Configuration
background_path = "img/png/udem.png"
logo_path = "img/png/java.png"
logo_name = Path(logo_path).stem
# logo_name = os.path.splitext(os.path.basename(logo_path))[0] To get filename without pathlib
output_path = f"img/overlay/udem_{logo_name}.png"

# ---------- Adjust these values as needed for different logos -----------
target_logo_height_pct = 0.40  # Percentage of background height for logo
x_position_pct = 0.73  # Horizontal position
y_position_pct = 0.18  # Vertical position
# ------------------------------------------------------------------------

# Load the images
try:
    background = Image.open(background_path).convert("RGBA")
    logo = Image.open(logo_path).convert("RGBA")
except FileNotFoundError as e:
    print(f"Error: Image file not found - {e}")
    exit()

# Resize the logo
target_logo_height = int(background.height * target_logo_height_pct)
logo_aspect_ratio = logo.width / logo.height
new_logo_width = int(target_logo_height * logo_aspect_ratio)
resized_logo = logo.resize((new_logo_width, target_logo_height))

# Calculate the position for the logo
x_position = int(background.width * x_position_pct)
y_position = int(background.height * y_position_pct)

# Overlay the logo onto the background
background.paste(resized_logo, (x_position, y_position), resized_logo)

# Save the output image
try:
    background.save(output_path)
    print(f"Successfully overlaid the logo. Output saved to {output_path}")
except Exception as e:
    print(f"Error saving the output image: {e}")
