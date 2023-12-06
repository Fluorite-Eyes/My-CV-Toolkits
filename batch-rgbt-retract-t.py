import os
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tqdm import tqdm

def process_images(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all PNG files
    png_files = [filename for filename in os.listdir(input_folder) if filename.endswith(".png")]

    # Use tqdm to display a progress bar
    for filename in tqdm(png_files, desc="Processing Images", unit="image"):
        # Construct input and output file paths
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Process a single image
        process_single_image(input_path, output_path)

def process_single_image(input_path, output_path):
    # Open the color image
    img = Image.open(input_path)

    # Extract the fourth channel (assuming it's RGBA)
    img_array = np.array(img)
    fourth_channel = img_array[:, :, 3]

    # Save the fourth channel as a grayscale image
    img_fourth_channel = Image.fromarray(fourth_channel, mode='L')
    img_fourth_channel.save(output_path)

if __name__ == "__main__":
    input_folder = r"C:\Users\chenjiashun\Desktop\ir_seg_dataset\images"  # 替换为输入文件夹的路径
    output_folder = R"C:\Users\chenjiashun\Desktop\MFNET"  # 替换为输出文件夹的路径
    process_images(input_folder, output_folder)
