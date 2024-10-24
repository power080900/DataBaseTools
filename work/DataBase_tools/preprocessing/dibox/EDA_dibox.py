import os
import pandas as pd
import sys
sys.path.append('..\\..\\src')
import EDA_utils as eda


root_path = 'Z:\\dibox\\data\\IR\\rawdata'
id_list = os.listdir(root_path)
df = pd.DataFrame(columns=['id', 'file'])

for id_ in id_list:
    id_path = os.path.join(root_path, id_)
    file_list = os.listdir(id_path)
    
    for file in file_list:
        file_path = os.path.join(id_path, file)
        # print(file_path,id_)
        df.loc[len(df)] = [id_, file]

df.to_csv('dibox.csv', index=False)

df1 = df.value_counts('id')

print(df1.head())


eda.plot_barh(df1, 'id', 'Count', 'id', 'Count', 'dibox_id_count.psng', rotation=0)
