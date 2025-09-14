from PIL import Image
import os

def optimize_image(input_path, output_path=None, max_size=(1920, 1080), quality=75):
    if output_path is None:
        output_path = input_path
    
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if necessary
        if img.mode == 'RGBA':
            # For PNG files, keep transparency
            if input_path.lower().endswith('.png'):
                img.thumbnail(max_size, Image.Resampling.LANCZOS)
                img.save(output_path, 'PNG', optimize=True)
            else:
                # Convert RGBA to RGB for JPG
                rgb_img = Image.new('RGB', img.size, (255, 255, 255))
                rgb_img.paste(img, mask=img.split()[3])
                rgb_img.thumbnail(max_size, Image.Resampling.LANCZOS)
                rgb_img.save(output_path, 'JPEG', quality=quality, optimize=True)
        else:
            # Resize image while maintaining aspect ratio
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            if input_path.lower().endswith('.png'):
                img.save(output_path, 'PNG', optimize=True)
            else:
                img.save(output_path, 'JPEG', quality=quality, optimize=True)

# Optimize slide images
slide_images = [
    "첫번째 슬라이드.JPG",
    "두번째 슬라이드.JPG",
    "세번째 슬라이드.jpg",
    "네번째 슬라이드.jpg",
    "다섯번째 슬라이드.jpg"
]

for image in slide_images:
    if os.path.exists(image):
        print(f"Optimizing {image}...")
        optimize_image(image, max_size=(1920, 1080), quality=75)

# Optimize logo images with different settings
logo_images = ["마크.png", "글자.png", "가로.png"]
for image in logo_images:
    if os.path.exists(image):
        print(f"Optimizing {image}...")
        optimize_image(image, max_size=(800, 800), quality=90)

print("Image optimization completed!") 