from datetime import datetime
import numpy as np
import csv

n = 200
a = []
b = []
d = []
c = np.ones((n,n))
maior = []

f = open('./otimizado_invertido.csv', 'w')
writer = csv.writer(f)

for t in range(1,25):
    start = datetime.now()

    for i in range(0,n):
        a.append(i*5.3)
        b.append(i+0.8)
        d.append(i+0.1)
        maior.append(a[i]<=b[i])

    for i in range(0,n):
        for j in range(0,n):
            c[i][j] = i*0.3

    for k in range(0,n):
        if maior[k]:
            for i in range(0,n):
                for j in range(0,n):
                    c[i][j] += k + (b[k] * a[k])/(j + 1)
        else:
            for i in range(0,n):
                for j in range(0,n):
                    c[i][j] += k + (b[k] * a[k])/(j + 1)

    end = datetime.now()
    row = f'otimizado_invertido, {t}, {end - start}'
    writer.writerow(row)
    print(f'Tempo Otimizado :{end - start}')