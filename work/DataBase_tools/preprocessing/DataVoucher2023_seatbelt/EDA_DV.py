import sys
sys.path.append('..\\..\\src')
import EDA_utils as EDA
import pandas as pd

label_file = 'label_data.csv'

df = pd.read_csv(label_file)

config = {
    ('userID','ID','count', 'ID Distribution', 'ID Distribution.png'),
    ('sex','sex','count','sex Distribution','sex Distribution.png'),
    ('age','age','count','age Distribution','age Distribution.png'),
    ('mask','mask','count','mask Distribution','mask Distribution.png'),
    ('glasses','glasses','count','glasses Distribution','glasses Distribution.png'),
    ('seatbelt','seatbelt','count','seatbelt Distribution','seatbelt Distribution.png'),
    ('cigar','cigar','count','cigar Distribution','cigar Distribution.png'),
    ('phone','phone','count','phone Distribution','phone Distribution.png')
}

for col, xlabel, ylabel, title, filename in config:
    if col == 'userID':
        df1 = df[col].value_counts().sort_index()
        EDA.plot_bar(df1, col, xlabel, ylabel, title, filename)
    elif col == 'sex':
        # print(df)
        df1 = df.drop_duplicates(subset=['userID'])
        # print(df1)
        df1 = df1[col].value_counts().sort_index()
        df1.index = ['M','F']
        EDA.plot_pie(df1, col, title, filename)
    elif col == 'age':
        df2 = df.drop_duplicates(subset=['userID'])
        # print(df2)
        df2 = df2[col].value_counts().sort_index()
        df2.index = ['20-29','30-39','40-49','50-59','60-69','70-']
        EDA.plot_pie(df2, col, title, filename)
    else:
        df1 = df[col].value_counts().sort_index()
        EDA.plot_bar(df1, col, xlabel, ylabel, title, filename)

