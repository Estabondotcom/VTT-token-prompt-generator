import os
import json

# Path to your local examples directory
C:\Users\frank\Desktop\examples

# Get all image files (you can add more extensions if needed)
valid_extensions = (".png", ".jpg", ".jpeg", ".webp")
image_files = [f for f in os.listdir(examples_dir) if f.lower().endswith(valid_extensions)]

# Output to images.json inside the same folder
with open(os.path.join(examples_dir, "images.json"), "w") as f:
    json.dump(image_files, f, indent=2)

print(f"{len(image_files)} image(s) added to images.json.")
