import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

data = pd.read_csv('/content/drive/MyDrive/Google-Playstore.csv')

print(data.columns)

lista = []

for d in data['Rating Count']:
    if isinstance(d, float) and str(d) != 'nan':
        lista.append(int(d))
    else:
        lista.append(0)

def counting_sort(l):
    counting_values = [0] * (max(l) + 1)
    for number in l:
        counting_values[number] += 1

    positions = [0] * len(l)
    current = 0

    for index, value in enumerate(counting_values):
        for pos in range(value):
            positions[current] = index
            current += 1

    return positions

sorted_elements = counting_sort(lista)

import time
import matplotlib.pyplot as plot

start = time.process_time()
counting_sort(lista)
end = time.process_time()

print("Tempo de execução: {:.5f} segundos".format(end-start))

data['Sorted Rating Count'] = counting_sort(lista)

data = data.sort_values(by="Rating Count")

"""
Especificações de execução:

- Sistema: Windows 7 Pro
- Tipo SO: 64 bits
- RAM: 2 GB
- Ambiente: Google Colaboratory © 2023
- Linguagem: Python 3
- Análise de código: Manual
- Tempo de execução total médio da função: 23s
"""
