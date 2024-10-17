import sys
from PIL import Image, ImageOps
import os


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        if check_file(sys.argv[1], sys.argv[2]):
            overlay_shirt(sys.argv[1], sys.argv[2])
        else:
            sys.exit("Not a valid extension")


def check_file(input_file, output_file):
    path = input_file
    filename, ext = os.path.splitext(path)
    ext_list = ['.jpeg', '.jpg', '.png']

    if ext.lower() in ext_list and output_file.endswith(ext.lower()):
        return True

    else:
        return False


def overlay_shirt(input_path, output_path):
    try:
        shirt = Image.open('shirt.png')
        with Image.open(input_path) as person:
            cropped_image = ImageOps.fit(person, shirt.size)
            cropped_image.paste(shirt, mask=shirt)
            cropped_image.save(output_path)

    except FileNotFoundError:
        sys.exit("File doest not exists")


if __name__ == '__main__':
    main()
