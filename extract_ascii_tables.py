import os
import shutil
import os.path
import pandas as pd

directory = 'Matelda-main/datasets/GitTables-subsets/subset_1000'
#directory = 'Matelda-main/datasets/DGov-subsets/dgov-1173'
    
counter = 0
valid_chars = []

#printable ascii characters
for elem in range(32, 127):
    valid_chars.append(elem)

#common symbols
valid_chars.extend([8217, 8211, 8221, 8220, 8212, 8230, 8216])

#Not so common symbols
#valid_chars.extend([8243, 8242, 8208, 180, 176])

#letters
#valid_chars.extend([233, 228, 246, 252, 234, 232, 225, 224, 250, 243, 237, 231, 269])

for filename in os.listdir(directory):
    if not filename.startswith('.'):
        for extra_file in os.listdir(directory + '/' + filename):
            if extra_file == 'clean.csv':
                future_filename = filename + '____' + 'clean.csv'
                current_file_path = directory + '/' + filename + '/' + 'clean.csv'
                #print(complete)

                df = pd.read_csv(current_file_path, sep = None, engine = 'python', on_bad_lines = 'skip', encoding = 'utf-8-sig')
                if list(df)[0] == 'Unnamed: 0':
                    df = pd.read_csv(current_file_path, sep = None, engine = 'python', on_bad_lines = 'skip', encoding = 'utf-8-sig', index_col = 0)

                valid = True

                if df.shape[0] < 10 or df.shape[1] < 3:
                    valid = False
                else:
                    column_names = list(df)
                    for column in column_names:
                        if (False in [(ord(elem) in valid_chars) for elem in str(column)]):
                            '''print('Current File: ' + current_file_path)
                            print("Column Name: " + str(column))'''
                            valid = False
                            break
                        if False in df[column].apply(lambda x: (not (False in [(ord(elem) in valid_chars) for elem in x])) if isinstance(x, str) else True).to_list():
                            '''temp = []
                            for elem in df[column].to_list():
                                if (isinstance(elem, str)):
                                    for ch in elem:
                                        if (ord(ch) not in valid_chars):
                                            temp.append('Char ' + str(ord(ch)) + ': ' + ch)
                            if len(temp) < 20:
                                print('Current File: ' + current_file_path)
                                print(temp)
                                print()'''
                            valid = False
                            break
                if valid:
                    counter += 1
                    df.to_csv('data/' + future_filename, index = False)
                    '''if os.path.isfile('data/' + future_filename):
                        print("file already exists")
                    else:
                        shutil.copy2(current_file_path, 'data/' + future_filename)'''
print(counter)