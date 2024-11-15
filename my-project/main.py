from PIL import Image
import os

# Configuration
input_dir = 'input'
output_dir = 'output'
resize_width = 800  # pixels

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Resize images
for filename in os.listdir(input_dir):
    if filename.lower().endswith('.jpg'):
        img_path = os.path.join(input_dir, filename)
        with Image.open(img_path) as img:
            # Calculate new height to maintain aspect ratio
            width_percent = resize_width / float(img.size[0])
            new_height = int((float(img.size[1]) * float(width_percent)))
            img_resized = img.resize((resize_width, new_height), Image.ANTIALIAS)
            
            # Save resized image
            output_path = os.path.join(output_dir, filename)
            img_resized.save(output_path)
            print(f"Saved resized image to {output_path}")
