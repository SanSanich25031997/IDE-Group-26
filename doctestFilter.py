from PIL import Image
import numpy as np

name = input("Введите имя файла, которое хотите конвертировать: ")
img = Image.open(name)
arr = np.array(img)
lengthOfImg = len(arr)
WidthOfImg = len(arr[1])
areaSize = 2
stepSize = 5


def findAvgColor(i, j, areaSize):
    """
    Находит средний цвет в который будет окрашивать определнную область.

    :param i: int, j:int, areaSize:int
    :return: int

    >>> findAvgColor(2, 2, 2)
    248
    >>> findAvgColor(5, 5, 5)
    248
    """
    avgColor = 0
    for areaX in range(i, i + areaSize):
            for areaY in range(j, j + areaSize):
                color1 = arr[areaX][areaY][0]
                color2 = arr[areaX][areaY][1]
                color3 = arr[areaX][areaY][2]
                avgColor += color1/3 + color2/3 + color3/3
    return int(avgColor // (areaSize*areaSize))


if __name__ == "__main__":
    import doctestFilter

    doctestFilter.testmod()