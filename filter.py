from PIL import Image
import numpy as np


def check_image(image_names):
    """Проверяет, подходит ли имя входного файла под название изображения и имеется ли название файла с результатом

        :param image_names: Названия входного файла и файла с результатом обработки
    """

    if image_names[0] == "" or '.' not in image_names[0]:
        quit()
    if len(image_names) == 1:
        image_names.append("output.jpg")


def get_grayscale(pixels_array, i, j, size):
    """Возвращает уровень серого в клетке

        :param pixels_array: Исходное изображение в виде матрицы numpy
        :param size: Размер мозаики
        :param i: Начальная координата y
        :param j: Начальная координата x
        :return: Значение серого в клетке

    >>> get_grayscale(np.array(Image.open("test_picture.jpg")), 25, 25, 5)
    120
    >>> get_grayscale(np.array(Image.open("test_picture.jpg")), 322, 322, 10)
    140
    """

    grayscale = 0
    for row in range(i, i + size):
        for column in range(j, j + size):
            red = pixels_array[row][column][0]
            green = pixels_array[row][column][1]
            blue = pixels_array[row][column][2]
            rgb_total = int(red) + int(green) + int(blue)
            grayscale += rgb_total / 3
    return int(grayscale // (size ** 2))


def set_color(i, j, size, grayscale, gray_spread, pixels_array):
    """Устанавливает оттенок серого в ячейке

        :param pixels_array: Исходное изображение в виде матрицы numpy
        :param grayscale: Значение серого для клетки
        :param gray_spread: Градации серого
        :param size: Размер мозаики
        :param i: Начальная координата y
        :param j: Начальная координата x
    """
    for row in range(i, i + size):
        for column in range(j, j + size):
            for n in range(3):
                pixels_array[row][column][n] = int(grayscale // gray_spread) * gray_spread


def make_mosaic(size, gray_spread, pixels_array):
    """Фильтрует изображение, делая из него мозаику

        :param pixels_array: Исходное изображение в виде матрицы numpy
        :param gray_spread: Градации серого
        :param size: Размер мозаики
    """

    i = 0
    while i < height - 1:
        j = 0
        while j < width - 1:
            set_color(i, j, size, get_grayscale(pixels_array, i, j, size), gray_spread, pixels_array)
            j = j + size
        i = i + size


names_input = input(
    "Введите название входного и выходного изображения, например, \"my_picture.jpg mosaic_picture.jpg\": ").split(
    ' ')
check_image(names_input)
img = Image.open(names_input[0])
image_pixels = np.array(img)
height = len(image_pixels)
width = len(image_pixels[1])
make_mosaic(int(input("Введите высоту ячейки мозаики: ")), int(input("Введите шаг градации серого: ")), image_pixels)
res = Image.fromarray(image_pixels)
res.save(names_input[1])
