from PIL import Image
import os
import numpy as np

def ft_load(path: str) -> np.ndarray:
    """
    Loads an image from the given path, prints its shape, and returns its pixels in RGB format as a NumPy array.

    Parameters:
    path (str): The file path to the image.

    Returns:
    np.ndarray: A NumPy array containing the pixel data of the image in RGB format, or None if an error occurs.

    This function handles JPG and JPEG image formats. It checks if the file exists and if the file extension is valid.
    If the image is not in RGB format, it converts the image to RGB. The function also includes error handling to
    print clear error messages in case of issues.
    """
    if not os.path.exists(path):
        print(f"Error: The file '{path}' does not exist.")
        return

    valid_extensions = ['jpg', 'jpeg', 'png']
    if not any(path.lower().endswith(ext) for ext in valid_extensions):
        print(f"Error: The file '{path}' is not a valid image file (jpg or jpeg).")
        return

    try:
        with Image.open(path) as img:
            print(img.format, img.size, img.mode)
            if img.mode != 'RGB':
                img = img.convert('RGB')

            pixels = np.array(img)

            print(f"The shape of image is: {pixels.shape}")

            return pixels
    except Exception as e:
        print(f"Error: An error occurred while processing the image. {str(e)}")
        return



def main():
    pass


if __name__ == "__main__":
    main()