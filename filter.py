from PIL import Image
import numpy as np


def get_gray_color(img_arr, cell_size, i, j, gray_scale_steps):
    """
    Находит цвет, в который надо покрасить ячейку мозаики
    :param numpy.ndarray img_arr: Исходное изображение в виде матрицы numpy
    :param int cell_size: Размер ячейки мозаики
    :param int i: Координата y ячейки
    :param int j: Координата x ячейки
    :param int gray_scale_steps: Количество градаций серого
    :return: Насыщенность найденного серого цвета

    >>> get_gray_color(np.array(Image.open("ahmed_epic.jpg")), 2, 0, 0, 50)
    200
    >>> get_gray_color(np.array(Image.open("ahmed_epic.jpg")), 5, 250, 250, 50)
    100
    """
    sat_level = 0
    for n in range(i, i + cell_size):
        for m in range(j, j + cell_size):
            red = img_arr[n][m][0]
            green = img_arr[n][m][1]
            blue = img_arr[n][m][2]
            rgb_sum = int(red) + int(green) + int(blue)
            sat_level += rgb_sum / 3
    avg_sat = int(sat_level // (cell_size * cell_size))
    return int(avg_sat // gray_scale_steps) * gray_scale_steps


img_in = input("Введите имена исходного изображения\n")
img = Image.open(img_in)
img_arr = np.array(img)
height = len(img_arr)
width = len(img_arr[1])

cell_size = input("Введите размер мозаики (по умолч. 2)\n")
try:
    cell_size = int(cell_size)
except ValueError:
    cell_size = 2

gray_scale_steps = input("Введите количество градаций серого (по умолч. 50)\n")
try:
    gray_scale_steps = int(gray_scale_steps)
except ValueError:
    gray_scale_steps = 50

i = 0
while i < height - 1:
    j = 0
    while j < width - 1:
        gray_color = get_gray_color(img_arr, cell_size, i, j, gray_scale_steps)
        for n in range(i, i + cell_size):
            for m in range(j, j + cell_size):
                img_arr[n][m][0] = gray_color
                img_arr[n][m][1] = gray_color
                img_arr[n][m][2] = gray_color

        j = j + cell_size
    i = i + cell_size

res = Image.fromarray(img_arr)
res.save(f"res_{img_in}")
print("Результат готов!")
