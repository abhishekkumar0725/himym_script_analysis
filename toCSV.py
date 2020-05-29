import pandas as pd
import numpy as np
import os

def main():
    directory = '/Users/abhishekkumar/Documents/programming/himym/data'
    for folder in os.listdir(directory):
        foldername = os.fsdecode(folder)
        current_folder = os.path.join(directory, foldername)
        df = pd.DataFrame(columns=['Season', 'Episode', 'Line Number', 'Speaker', 'Line'])
        season = int(folder[-2:])
        for file in os.listdir(current_folder):
            filename = os.fsdecode(file)
            current_file = os.path.join(current_folder, file)
            episode = int(file[-6:-4])
            i = 1
            with open(current_file, 'r') as f:
                for line in f:
                #line = f.read()
                    if ':' in line:
                        df = df.append({
                            'Season': season,
                            'Episode': episode,
                            'Line Number': i,
                            'Speaker': line[:line.index(':')],
                            'Line': line[line.index(':')+2:]
                        }, ignore_index=True)
                        i += 1
        df.to_csv(foldername+'.csv', encoding="utf-8", index = False)

if __name__=='__main__':
    main()



