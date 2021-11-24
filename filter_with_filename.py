from PIL import Image
import numpy as np

imgIn = "ahmed_epic.jpg"
img = Image.open(imgIn)
imgArr = np.array(img)
height = len(imgArr)
width = len(imgArr[1])
cellSize = 10
grayScaleSteps = 50


def getGrayLvlInCell(imgArr, cellSize, i, j):
    grayLevel = 0
    for n in range(i, i + cellSize):
        for m in range(j, j + cellSize):
            red = imgArr[n][m][0]
            green = imgArr[n][m][1]
            blue = imgArr[n][m][2]
            rgbSum = int(red) + int(green) + int(blue)
            grayLevel += rgbSum / 3
    return int(grayLevel // (cellSize * cellSize))


def colorCell(imgArr, cellSize, grayScaleSteps, i, j, grayLevel):
    for n in range(i, i + cellSize):
        for m in range(j, j + cellSize):
            imgArr[n][m][0] = int(grayLevel // grayScaleSteps) * grayScaleSteps
            imgArr[n][m][1] = int(grayLevel // grayScaleSteps) * grayScaleSteps
            imgArr[n][m][2] = int(grayLevel // grayScaleSteps) * grayScaleSteps


i = 0
while i < height - 1:
    j = 0
    while j < width - 1:
        grayLevel = getGrayLvlInCell(imgArr, cellSize, i, j)

        colorCell(imgArr, cellSize, grayScaleSteps, i, j, grayLevel)

        j = j + cellSize
    i = i + cellSize

res = Image.fromarray(imgArr)
res.save(f"res_{imgIn}")
print("Результат готов!")
