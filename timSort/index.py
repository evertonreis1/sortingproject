import curses
import os
import sys
import time

import pandas as pd
from utils import getExecTime

from timSort import timSort

DATABASE = "src/database/Google-Playstore.csv"
ROWS = 10000
COLUMN = 'Installs'

sys.setrecursionlimit(1000)

df = pd.read_csv(DATABASE).head(ROWS)
columns = list(df.columns)
column = list(df[COLUMN].to_dict().items())

start = time.time()
result = timSort(column)
sortedIndexes = [item[0] for item in result]

for col in df.keys():
    df[col] = [df[col][i] for i in sortedIndexes]

end = time.time()
execTime = (getExecTime(start, end))

print(df)
print(f"Tempo de execução: {execTime}")
