import pyheif
import os
from PIL import Image
import sys

def heic_to_png(heic_file):
    heif_file = pyheif.read(heic_file)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
        )
    
    png_file = os.path.splitext(heic_file)[0] + ".png"
    image.save(png_file, "PNG")

def main():
    # check if file names provided
    if len(sys.argv) < 2:
        print("Usage: python convert.py <filename1.heic> <filename2.heic> ...")
        return

    # convert each file
    for filename in sys.argv[1:]:
        if filename.lower().endswith(".heic"):
            print(f"Converting {filename} to PNG...")
            try:
                heic_to_png(filename)
                print(f"Successfully converted {filename} to PNG.")
            except Exception as e:
                print(f"Failed to convert {filename} due to error: {e}")
        else:
            print(f"Skipped {filename} as it does not end with '.heic'.")

if __name__ == "__main__":
    main()
