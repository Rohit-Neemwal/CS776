from IPython.display import clear_output
from rembg import remove
from PIL import Image
import os

input_path = './croppedplantdoc/Train'
output_path = './croppedbg/Train'
count = 0
for classname in os.listdir():
  for filename in os.listdir(os.path.join(input_path,classname)):
    print(count)
    count+=1

    input_img = Image.open(os.path.join(input_path,classname,filename))

    
    output_img = remove(input_img)

    # black background
    background = Image.new('RGBA', input_img.size, (0, 0, 0, 255))

    # image on top of black background
    result_img = Image.alpha_composite(background, output_img.convert('RGBA'))

    
    black_threshold = 0.85
    black_pixels = sum(1 for pixel in result_img.getdata() if pixel[0] <= 15 and pixel[1] <= 15 and pixel[2] <= 15)
    black_percentage = black_pixels / (result_img.size[0] * result_img.size[1])

    if black_percentage >= black_threshold:
      result_img = input_img

    # Save result image
    if not os.path.exists(os.path.join(output_path,classname)):
      os.makedirs(os.path.join(output_path,classname))
    result_img.convert('RGB').save(os.path.join(output_path,classname,filename))
    clear_output()
