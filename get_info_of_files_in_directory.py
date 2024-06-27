import os
import pandas as pd

for elem in ['data_testing_at_least_5000']:
    directory = elem

    list_number_rows = []
    list_number_cols = []
    counter_rows = 0
    counter_total_rows = 0
    counter_cols = 0
    counter_total_cols = 0

    at_least_rows = 1000
    at_least_cols = 10

    for filename in os.listdir(directory):
        full_path = directory + '/' + filename
        df = pd.read_csv(full_path)
        list_number_rows.append(df.shape[0])
        list_number_cols.append(df.shape[1])

        if df.shape[0] >= at_least_rows:
            counter_rows += 1
        if df.shape[1] >= at_least_cols:
            counter_cols += 1
        
        counter_total_rows += 1
        counter_total_cols += 1

    print(f'stats for {elem}:')
    print(f'total number of files in directory: {counter_total_rows}')
    print(f'avg number rows: {sum(list_number_rows) / len(list_number_rows)}')
    print(f'avg number cols: {sum(list_number_cols) / len(list_number_cols)}')
    print(f'median number rows: {list_number_rows[round(len(list_number_rows)/2)]}')
    print(f'median number cols: {list_number_cols[round(len(list_number_cols)/2)]}')
    print()
    print(f'number of csv with more that {at_least_rows} rows: {counter_rows}')
    print(f'percentage of csv with more that {at_least_rows} rows: {counter_rows / counter_total_rows}')
    print()
    print(f'number of csv with more that {at_least_cols} cols: {counter_cols}')
    print(f'percentage of csv with more that {at_least_cols} cols: {counter_cols / counter_total_cols}')
    print()
    print()