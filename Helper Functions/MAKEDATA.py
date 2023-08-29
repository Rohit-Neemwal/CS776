from PIL import Image
import pandas as pd
import os

train_df  = pd.read_csv('./PlantDoc-Object-Detection-Dataset-master/train_labels.csv')

input_dir = 'F:\CS776\dataset\PlantDoc-Object-Detection-Dataset-master\TRAIN'

for i in range(len(train_df)):
    print(i)
    for filename in os.listdir(input_dir):
        if(filename == train_df['filename'][i]):
            if filename.endswith('.jpg'):
                # Open the  file jpg image 
              if os.path.exists(os.path.join(input_dir, filename)):
                with Image.open(os.path.join(input_dir, filename)) as img:
                   
                    cropped_img = img.crop((train_df['xmin'][i], train_df['ymin'][i], train_df['xmax'][i], train_df['ymax'][i]))
                    rgb_img = cropped_img.convert('RGB')
                    
                    output_dir = '.\croppedplantdoc\Train\\' + train_df['class'][i]

                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)

                    rgb_img.save(os.path.join(output_dir, str(i)+filename))


test_df  = pd.read_csv('./PlantDoc-Object-Detection-Dataset-master/test_labels.csv')

input_dir = 'F:\CS776\dataset\PlantDoc-Object-Detection-Dataset-master\TEST'

for i in range(len(test_df)):
    print(i)
    for filename in os.listdir(input_dir):
        if(filename == test_df['filename'][i]):
            if filename.endswith('.jpg'):
                
              if os.path.exists(os.path.join(input_dir, filename)):
                with Image.open(os.path.join(input_dir, filename)) as img:
                  
                    cropped_img = img.crop((test_df['xmin'][i], test_df['ymin'][i], test_df['xmax'][i], test_df['ymax'][i]))
                    rgb_img = cropped_img.convert('RGB')
                    # Save the cropped image to the output directory
                    output_dir = '.\croppedplantdoc\Test\\' + test_df['class'][i]

                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)

                    rgb_img.save(os.path.join(output_dir, str(i)+filename))