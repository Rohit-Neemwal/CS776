
from rembg import remove
from PIL import Image
import os

input_path = 'F:\CS776\dataset\croppedplantdoc\Train\Apple leaf\\3249apples_silver-leaf_04_zoom.jpg'
output_path = 'F:\CS776\leaves_oneleaf\hibiscus_leaves\healthy\\test_image.jpg'



input_img = Image.open(os.path.join(input_path))

output_img = remove(input_img)

# Create background
background = Image.new('RGBA', input_img.size, (0, 0, 0, 255))

# add image on top of black background
result_img = Image.alpha_composite(background, output_img.convert('RGBA'))

 # my condition
black_threshold = 0.99 # adjust this value as needed
black_pixels = sum(1 for pixel in result_img.getdata() if pixel[0] <= 15 and pixel[1] <= 15 and pixel[2] <= 15)
black_percentage = black_pixels / (result_img.size[0] * result_img.size[1])

# result image =  input image if it is mostly black
if black_percentage >= black_threshold:
      result_img = input_img
if not os.path.exists("F:\CS776\leaves_oneleaf\hibiscus_leaves\healthy"):
    os.makedirs("F:\CS776\leaves_oneleaf\hibiscus_leaves\healthy")
    # Save result image
result_img.convert('RGB').save(output_path)
 
