from PIL import Image
import numpy as np


def FindMedianSaturation(i, j):
    """Находит среднюю насыщенность выбранного фрагмента

    >>> FindMedianSaturation(0, 0)
    7
    >>> FindMedianSaturation(100, 100)
    5
    >>> FindMedianSaturation(200, 200)
    2"""
    medianSaturation = 0
    for n in range(i, i + mosaicPartSide):
        for n0 in range(j, j + mosaicPartSide):
            redSat = imageMatrix[n][n0][0]
            greenSat = imageMatrix[n][n0][1]
            blueSat = imageMatrix[n][n0][2]
            pixelSat = int(redSat) + int(greenSat) + int(blueSat)
            medianSaturation += pixelSat / 3
    return int(medianSaturation // 100)


def ApplyMedianSaturation(i, j, medianSat):
    """присваивает всем пикселям фрагмента заданную насыщенность"""
    for n in range(i, i + mosaicPartSide):
        for n1 in range(j, j + mosaicPartSide):
            imageMatrix[n][n1][0] = int(medianSat // graySens) * graySens
            imageMatrix[n][n1][1] = int(medianSat // graySens) * graySens
            imageMatrix[n][n1][2] = int(medianSat // graySens) * graySens


if __name__ == "__main__":
    import filter

    filter.testmod()

print('введите полные названия файлов')
imgadreses = input().split(' ')
img = Image.open(imgadreses[0])
imageMatrix = np.array(img)
mosaicPartSide = 5
graySens = 10
height = len(imageMatrix)
width = len(imageMatrix[1])
for i in range(0, height - 1, mosaicPartSide):
    for j in range(0, width - 1, mosaicPartSide):
        medianSaturation = FindMedianSaturation(i, j)
        ApplyMedianSaturation(i, j, medianSaturation)
res = Image.fromarray(imageMatrix)
res.save(imgadreses[1])

print('pilik pilik')

