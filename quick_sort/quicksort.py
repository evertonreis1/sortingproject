import pandas as pd
import sys


sys.setrecursionlimit(1000) 


df = pd.read_csv('/content/Google-Playstore.csv')


df = df['Scraped Time'].apply(lambda x: pd.Series(str(x).split(',')))


def quicksort(arr, depth):
   
    if len(arr) <= 1:
        return arr
    
    
    if depth <= 0:
        return []
    
   
    pivot = arr[0]
    left = []
    right = []
    
    for item in arr[1:]:
        if item < pivot:
            left.append(item)
        else:
            right.append(item)
    
   
    left_sorted = quicksort(left, depth-1) 
    right_sorted = quicksort(right, depth-1)
    
   
    return left_sorted + [pivot] + right_sorted


for col in df.columns:
    
    sorted_col = quicksort(df[col].tolist(), depth=900) 
    
    sorted_col += [None] * (len(df) - len(sorted_col)) 
    
    df[col] = sorted_col 


print(df)


