from PIL import Image
import numpy as np

img = Image.open("CP77-KV-en.jpg")
arr = np.array(img, dtype=np.int32)
a = len(arr)
a1 = len(arr[1])
i = 0
while i < a - 11:
    j = 0
    while j < a1 - 11:
        s = 0
        for n in range(i, i + 10):
            for x in range(j, j + 10):
                n1 = arr[n][x][0]
                n2 = arr[n][x][1]
                n3 = arr[n][x][2]
                M = n1 + n2 + n3
                s += M
        s = int(s // 100)
        for n in range(i, i + 10):
            for y in range(j, j + 10):
                arr[n][y][0] = int(s // 50) * 50
                arr[n][y][1] = int(s // 50) * 50
                arr[n][y][2] = int(s // 50) * 50
        j = j + 10
    i = i + 10
res = Image.fromarray(arr)
res.save('Cyber_old.res.jpg')
