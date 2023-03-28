import os
import sys
import pandas as pd
path = "./predict_file/"
csv_file = sys.argv[1]
csv = pd.read_csv(path + csv_file, names=['paragraph'], encoding='utf-8')
for index, row in csv.iterrows():
    print(row['paragraph'])
    df = pd.DataFrame({'paragraph': row['paragraph']})
    df.to_csv(f'{path}paragraph.txt', header=False, index=False)
    os.system(f'curl -X POST http://127.0.0.1:8080/predictions/bert -T {path}paragraph.txt')
