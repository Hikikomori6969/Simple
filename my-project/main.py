from PIL import Image
import os

# Function to resize images
def resize_image(input_path, output_path, width):
    try:
        with Image.open(input_path) as img:
            # Calculate new height to maintain aspect ratio
            width_percent = width / float(img.size[0])
            new_height = int((float(img.size[1]) * float(width_percent)))
            img_resized = img.resize((width, new_height), Image.ANTIALIAS)
            img_resized.save(output_path)
            print(f"Saved resized image to {output_path}")
    except Exception as e:
        print(f"Failed to process image {input_path}: {e}")

# Configuration
input_dir = 'input'
output_dir = 'output'
resize_width = 800  # Default width in pixels

# Ensure input and output directories exist
if not os.path.exists(input_dir):
    print(f"Input directory '{input_dir}' does not exist. Please create it and add images.")
    exit(1)
os.makedirs(output_dir, exist_ok=True)

# Process each image in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):  # Include PNG format
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        resize_image(input_path, output_path, resize_width)
