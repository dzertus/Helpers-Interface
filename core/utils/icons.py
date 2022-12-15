# Template file
"""
Icons Utils
"""
# TODO Make it a class
import logging

from PIL import Image

logger = logging.getLogger('icons_utils')


def open_image(image_path):
    """

    :param image_path:
    :return:
    """
    image = Image.open(image_path)
    return image


def get_image_data(image):
    """

    :param image:
    :return:
    """
    data = image.getdata()
    return data


def convert_to_rgb(image):
    """

    :param image:
    :return:
    """
    image = image.convert("RGB")
    return image


def convert_to_grayscale(image):
    """

    :param image:
    :return:
    """
    image = image.convert("L")
    return image


def change_color(image_data, new_color):
    """

    :param image_data:
    :param new_color:
    :return:
    """
    new_image_data = []
    for item in image_data:
        if item[0] in list(range(200, 256)):
            new_image_data.append(new_color)
        else:
            new_image_data.append(item)
    return new_image_data


def save_image(image, path):
    """

    :param image:
    :param path:
    :return:
    """
    image.save(path)
    print('logging')
    logger.debug('image saved to {}'.format(path))


def main():
    """

    :return:
    """
    image_path = r"C:\Users\youss\Documents\GitHub\Maya-Helpers-Interface\python\examples" \
                 r"\print_example\print_example" \
                 r".png "
    im = open_image(image_path)
    im = convert_to_rgb(im)
    data = get_image_data(im)
    pink_color = (255, 0, 0)
    new_image_data = change_color(data, pink_color)

    im.putdata(new_image_data)
    im.show()
    save_path = r"C:\Users\youss\Desktop\flower_image_altered.jpg"
    save_image(im, save_path)


if __name__ == '__main__':
    main()
