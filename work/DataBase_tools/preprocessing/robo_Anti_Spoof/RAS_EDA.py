import sys
sys.path.append('..\\')
import EDA_utils as EDA
import pandas as pd

# RAS 데이터 EDA

# 데이터 불러오기
data = pd.read_csv('labeldata.csv')

# print(data.head())


config = {
    ('label_id','ID','count', 'ID Distribution', 'ID Distribution.png')
}

# 데이터 시각화

for col, xlabel,ylabel, title, filename in config:
    df1 = data[col].value_counts().sort_index()
    # print(df1)
    EDA.plot_bar(df1, col, xlabel, ylabel, title, filename)
    
    # print(col)
    file_name_2 = filename.replace('.png', '_label_name.png')
    cols = ['label_id','label_name']
    EDA.multi_plot_bar(data, cols, xlabel, ylabel, title, file_name_2)
