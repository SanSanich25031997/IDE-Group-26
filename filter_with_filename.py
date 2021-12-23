from PIL import Image
import numpy as np

img_in_way = "test_picture.jpg"

img_out_way = "ouut.jpg"
img_params_size = 10

img_params_grad = 50

img = Image.open(img_in_way)
arr_img = np.array(img)
rows = len(arr_img)
columns = len(arr_img[1])


def set_clarity(size, number_column, number_row):
    """Возвращает уровень серого в клетке

        :param size: Размер мозаики
        :param number_row: Начальная координата y
        :param number_column: Начальная координата x
        :return: Значение серого в клетке

    >>> set_clarity(5, 25, 25)
    200
    >>> set_clarity(10, 322, 322)
    58
    """

    gray_tier = 0
    for n in range(number_row, number_row + size):
        for h in range(number_column, number_column + size):
            r = arr_img[n][h][0]
            g = arr_img[n][h][1]
            b = arr_img[n][h][2]
            sum_rgb = int(r) + int(g) + int(b)
            gray_tier += sum_rgb / 3
    return int(gray_tier // (size ** 2))


def set_grey_color(gray_tier, size, number_column, number_row, gradations):
    """Устанавливает оттенок серого в ячейке

        :param gray_tier: Значение серого для клетки
        :param gradations: Градации серого
        :param size: Размер мозаики
        :param number_row: Начальная координата y
        :param number_column: Начальная координата x
    """
    for n in range(number_row, number_row + size):
        for h in range(number_column, number_column + size):
            arr_img[n][h][0] = int(gray_tier // gradations) * gradations
            arr_img[n][h][1] = int(gray_tier // gradations) * gradations
            arr_img[n][h][2] = int(gray_tier // gradations) * gradations


def create_mosaic(size, gradations):
    """Фильтрует изображение, делая из него мозаику

        :param gradations: Градации серого
        :param size: Размер мозаики
    """

    number_row = 0
    while number_row < rows:
        number_column = 0
        while number_column < columns:
            set_grey_color(set_clarity(size, number_column, number_row), size, number_column, number_row, gradations)
            number_column = number_column + size
        number_row = number_row + size


create_mosaic(int(img_params_size), int(img_params_grad))
res = Image.fromarray(arr_img)
try:
    res.save(img_out_way)
except BaseException:
    print('Ошибка имени выходного изображения')
    quit()
