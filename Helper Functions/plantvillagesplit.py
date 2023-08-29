import os
import random
import shutil

# Define the root directory containing the 29 folders
root_dir = 'F:\CS776\Leaves'

# Define the directory names for train and test splits
train_dir = 'train'
test_dir = 'test'

# Define the train-test split ratio
split_ratio = 0.8

# Create the directory for the train and test folders
data_dir = os.path.dirname(root_dir)
train_test_dir = os.path.join(data_dir, 'leafnew_splitted')
os.makedirs(train_test_dir)

# Loop over the 29 folders and split the data into train and test
for folder_name in os.listdir(root_dir):
    folder_path = os.path.join(root_dir, folder_name)
    if os.path.isdir(folder_path):
        train_folder_path = os.path.join(train_test_dir, train_dir, folder_name)
        test_folder_path = os.path.join(train_test_dir, test_dir, folder_name)
        os.makedirs(train_folder_path)
        os.makedirs(test_folder_path)
        files = os.listdir(folder_path)
        random.shuffle(files)
        split_index = int(len(files) * split_ratio)
        train_files = files[:split_index]
        test_files = files[split_index:]
        for train_file in train_files:
            src_path = os.path.join(folder_path, train_file)
            dst_path = os.path.join(train_folder_path, train_file)
            shutil.copy(src_path, dst_path)
        for test_file in test_files:
            src_path = os.path.join(folder_path, test_file)
            dst_path = os.path.join(test_folder_path, test_file)
            shutil.copy(src_path, dst_path)
