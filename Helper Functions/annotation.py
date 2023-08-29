import os
import cv2

folder_path = "./testleaf"  # Change this to the path of your image folder

healthy_count = 1
unhealthy_count = 1

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)

        # Calculate the scale factor to fit the image into a 600x800 window
        max_width = 600
        max_height = 800
        scale = min(max_width / img.shape[1], max_height / img.shape[0])
        window_width = int(img.shape[1] * scale)
        window_height = int(img.shape[0] * scale)

        cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Image", window_width, window_height)

        cv2.imshow("Image", img)
        key = cv2.waitKey(0)

        if key == ord('h'):
            new_name = f"test_healthy_{healthy_count}.jpg"
            healthy_count += 1
        elif key == ord('u'):
            new_name = f"test_unhealthy_{unhealthy_count}.jpg"
            unhealthy_count += 1
        else:
            continue

        new_folder_path = os.path.join(folder_path, new_name.split("_")[1])
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)

        new_img_path = os.path.join(new_folder_path, new_name)

        # Resize the image to 50% while maintaining aspect ratio
        new_img = cv2.resize(img, (int(img.shape[1] * 0.5), int(img.shape[0] * 0.5)))
        cv2.imwrite(new_img_path, new_img, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

cv2.destroyAllWindows()
