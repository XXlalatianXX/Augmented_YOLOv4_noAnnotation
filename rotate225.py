import os
import cv2
import numpy as np
from concurrent.futures import ThreadPoolExecutor

dataset_folder = "D:/Dataset_All_Train/data1"  # Replace with the path to your dataset folder
output_folder = "D:/Dataset_All_Train/data2"  # Replace with the desired output folder

os.makedirs(output_folder, exist_ok=True)

image_files = [f for f in os.listdir(dataset_folder) if f.endswith('.jpg')]

def rotate_image(image_file):
    image_path = os.path.join(dataset_folder, image_file)
    output_image_name = os.path.splitext(image_file)[0] + "_225.jpg"
    output_image_path = os.path.join(output_folder, output_image_name)

    # Read the image
    image = cv2.imread(image_path)

    # Get the image dimensions
    height, width = image.shape[:2]

    # Calculate the center point of the image
    center = (width // 2, height // 2)

    # Define the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, 225, 1.0)

    # Perform the rotation on the image
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height), flags=cv2.INTER_LINEAR)

    # Save the rotated image with the new name
    cv2.imwrite(output_image_path, rotated_image)

    return f"Rotated image saved: {output_image_path}"

# Set the number of threads for concurrent execution
num_threads = 4

# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Process the images using concurrent execution
    results = executor.map(rotate_image, image_files)

    # Print the results
    for result in results:
        print(result)
