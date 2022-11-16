import sys
from PIL import Image
from PIL import ImageOps


def main():
    # require two files
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # require input as .jpg, .jpeg or .png
    elif sys.argv[1].endswith(("jpg", "jpeg", "png")) == False:
        sys.exit("Invalid input")
    # require output as .jpg, .jpeg or .png
    elif sys.argv[2].endswith(("jpg", "jpeg", "png")) == False:
        sys.exit("Invalid output")
    # require input and output have the same file extension
    elif sys.argv[1].split(".")[1] != sys.argv[2].split(".")[1]:
        sys.exit("Input and output have different extensions")


    open_and_apply(sys.argv[1], sys.argv[2])


def open_and_apply(input_image, output_image):
    try:
        with Image.open(input_image) as im:
            # resize
            im = ImageOps.fit(im, size=(600, 600))
            # open shirt
            with Image.open("shirt.png") as shirt:
                # paste
                im.paste(shirt, shirt)
                # resize
                im.save(output_image)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()