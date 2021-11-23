from PIL import Image
import numpy as np

imgIn = input("Введите имена исходного изображения")
img = Image.open(imgIn)
img_arr = np.array(img)
height = len(img_arr)
width = len(img_arr[1])
cell_size = input("Введите размер мозаики (по умолч. 2)")
try:
    cell_size = int(cell_size)
except ValueError:
    cell_size = 2
gray_scale_steps = input("Введите количество градаций серого (по умолч. 50)")
try:
    gray_scale_steps = int(gray_scale_steps)
except ValueError:
    gray_scale_steps = 50


def get_gray_lvl_in_cell(img_arr, cell_size, i, j):
    """

    :param img_arr: Исходное изображение в виде матрицы numpy
    :param cell_size: Размер мозаики
    :param i: Начальная координата y
    :param j:
    :return:
    """
    gray_level = 0
    for n in range(i, i + cell_size):
        for m in range(j, j + cell_size):
            red = img_arr[n][m][0]
            green = img_arr[n][m][1]
            blue = img_arr[n][m][2]
            rgb_sum = int(red) + int(green) + int(blue)
            gray_level += rgb_sum / 3
    return int(gray_level // (cell_size * cell_size))


i = 0
while i < height - 1:
    j = 0
    while j < width - 1:
        gray_level = get_gray_lvl_in_cell(img_arr, cell_size, i, j)
        gray_color = int(gray_level // gray_scale_steps) * gray_scale_steps

        for n in range(i, i + cell_size):
            for m in range(j, j + cell_size):
                img_arr[n][m][0] = gray_color
                img_arr[n][m][1] = gray_color
                img_arr[n][m][2] = gray_color

        j = j + cell_size
    i = i + cell_size

res = Image.fromarray(img_arr)
res.save(f"res_{imgIn}")
print("Результат готов!")
