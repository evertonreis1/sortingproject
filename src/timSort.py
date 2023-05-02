import sys
import time
from datetime import datetime
from typing import Literal


def compareStr(first, second, operation: Literal['gt', 'lt'] = 'gt'):
    try:
        firstDate = datetime.fromisoformat(first)
        secondDate = datetime.fromisoformat(second)

        if operation == 'lt':
            return firstDate < secondDate
        else:
            return firstDate > secondDate

    except:
        if operation == 'lt':
            return first.lower() < second.lower()
        else:
            return first.lower() > second.lower()


def compare(first, second, operation: Literal['gt', 'lt'] = 'gt'):
    if operation == 'lt':
        return first < second
    else:
        return first > second


def calcMinRun(n):
    r = 0
    while n >= 32:
        r |= n & 1
        n >>= 1
    return n + r


def mergeSort(left, right, operation: Literal['gt', 'lt'] = 'gt'):
    result = []
    while len(left) != 0 or len(right) != 0:
        if len(left) == 0:
            result.extend(right)
            right = []
        elif len(right) == 0:
            result.extend(left)
            left = []
        elif operation == 'gt' and left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        elif operation == 'lt' and left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)
    return result


def insertionSort(items, operation: Literal['gt', 'lt'] = 'gt'):
    result = []

    for currentIndex, item in enumerate(items):
        currentKey = item[0]
        currentValue = item[1]
        insertIn = currentIndex

        for index, item in reversed(list(enumerate(result[:currentIndex]))):
            itemValue = item[1]

            if isinstance(itemValue, str) and isinstance(currentValue, str):
                if compareStr(itemValue, currentValue, operation):
                    insertIn = index
            elif (isinstance(itemValue, int) or isinstance(itemValue, float)) and (isinstance(currentValue, int) or isinstance(currentValue, float)) or isinstance(itemValue, bool) and isinstance(currentValue, bool):
                if compare(itemValue, currentValue, operation):
                    insertIn = index

            else:
                raise ValueError(
                    f'Impossível comparar {itemValue} com {currentValue}')

        result.insert(insertIn, (currentKey, currentValue))

    return result


def timSort(items, operation: Literal['gt', 'lt'] = 'gt'):
    RUN = calcMinRun(len(items))
    runs = [items[i:i+RUN] for i in range(0, len(items), RUN)]

    try:
        runs = [insertionSort(run, operation) for run in runs]
    except ValueError:
        print(ValueError)

    while len(runs) > 1:
        left = runs[0]
        right = runs[1]
        merged = mergeSort(left, right, operation)
        runs[0:2] = [merged]
    return runs[0]
