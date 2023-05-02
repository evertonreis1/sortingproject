import curses
import os
import sys
import time

import pandas as pd

from timSort import timSort
from utils import getExecTime

DATABASE = "src/database/Google-Playstore.csv"
ROWS = 10000
COLUMN = 'Installs'

sys.setrecursionlimit(1000)

df = pd.read_csv(DATABASE).head(ROWS)
columns = list(df.columns)


def exec(function, data):
    global df

    start = time.time()
    result = function(data)
    sortedIndexes = [item[0] for item in result]

    for col in df.keys():
        df[col] = [df[col][i] for i in sortedIndexes]

    end = time.time()
    execTime = (getExecTime(start, end))

    print(df)
    print(f"Tempo de execução: {execTime}")


def main():
    global COLUMN

    while True:
        column = list(df[COLUMN].to_dict().items())

        print('------------------------------------------')
        print('Qual algorítmo que deseja usar?')
        print('------------------------------------------')
        print('1 - Quick Sort')
        print('2 - Counting Sort')
        print('3 - Tim Sort')
        print(f'4 - Alterar Coluna de base para ordenação (default:{COLUMN})')
        print('------------------------------------------')
        print('5 - Sair')
        selected = int(input('Digite a opção selecionada: '))

        if selected == 5:
            os.system('cls')
            os.system('clear')

            print('------------------------------------------')

            print('Até mais!')

            print('------------------------------------------')
            break
        elif selected == 1:
            os.system('cls')
            os.system('clear')

            print('Quick Sort')
            print('')
            print('------------------------------------------')

        elif selected == 2:
            os.system('cls')
            os.system('clear')

            print('Counting Sort')

            print('')
            print('------------------------------------------')
        elif selected == 3:
            os.system('cls')
            os.system('clear')
            print('Tim sort')

            exec(timSort, column)

            print('')
            print('------------------------------------------')

        elif selected == 4:

            os.system('cls')
            os.system('clear')
            print('Alterar coluna de base para ordenação: ')
            for index, column in enumerate(columns):
                print(f'{index} - {column}')

            while True:
                columnSelected = input('Nome da coluna: ')

                if not columnSelected in columns:
                    print('Esta coluna não existe')
                    pass
                else:
                    COLUMN = columnSelected
                    break

            print('')
            print('------------------------------------------')
        else:
            os.system('cls')
            os.system('clear')

            print('Opção inválida')
            print('------------------------------------------')

            pass


main()
