import pandas as pd
import numpy as np
import os

def lineCounter(df):
    counts = {}
    main_charachters = ['ted', 'robin', 'barney', 'marshall', 'lily']
    for row in df.itertuples():
        charachter = str(row[4]).lower()
        if charachter in main_charachters:
            if charachter not in counts:
                counts[charachter]  = 0
            counts[charachter] += 1
    return counts
        

if __name__=='__main__':
    directory = '/Users/abhishekkumar/Documents/programming/himym/data/dataframes/'
    for file in os.listdir(directory):
        fileName = os.fsdecode(file)
        df = pd.read_csv(directory+file)
        print(dict(sorted(lineCounter(df).items())))

