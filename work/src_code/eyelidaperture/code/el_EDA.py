import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('el_300vw.csv')
df2 = pd.read_csv('el_300w.csv')
df3 = pd.read_csv('el_300w_lp.csv')
df4 = pd.read_csv('el_300w_3d.csv')
df5 = pd.read_csv('el_aflw2000.csv')
df6 = pd.read_csv('el_cofw.csv')
df7 = pd.read_csv('el_dibox.csv')
df8 = pd.read_csv('el_frgc.csv')
df9 = pd.read_csv('el_Menpo2D.csv')
df10 = pd.read_csv('el_MultiPIE.csv')
# df11 = pd.read_csv('el_sai.csv')
df12 = pd.read_csv('el_xm2vts.csv')

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df12])
df['dpi'] = df['dpi'].fillna(96)

df['eyelid_group'] = pd.cut(df['eyelid'], bins=[0,25, 50, 75, 100, 125, 150],labels=['[0, 25)', '[25, 50)', '[50, 75)', '[75, 100)', '[100, 125)', '[125, 150)'])
# df['eyelid_cm'] = df['eyelid'] / df['dpi'] * 2.54
# df['eyelid_cm_group'] = pd.cut(df['eyelid_cm'], bins=[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5], labels=['[0, 0.5)', '[0.5, 1)', '[1, 1.5)', '[1.5, 2)', '[2, 2.5)', '[2.5, 3)', '[3, 3.5)', '[3.5, 4)', '[4, 4.5)', '[4.5, 5)'])
# print(df.head())

def draw_barplot(df, column, title):
    df_column = df[column].value_counts().reset_index().sort_index()
    df_column.columns = [column, 'count']
    df_column = df_column.sort_values(by=column)

    plt.figure(figsize=(10, 6))
    sns.barplot(x=column, y='count', data=df_column)
    for index, value in enumerate(df_column['count']):
        plt.text(index, value, str(value), ha='center', va='bottom')
    plt.title(title)
    plt.savefig(f'{column}_distribution.png')

def draw_heatmap(df, column1, column2, title):
    plt.figure(figsize=(15, 15))
    heatmap_data = df.pivot_table(index=column1, columns=column2, values='label', aggfunc='count')
    sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt="d")  # annot=True 추가하여 숫자 표시, fmt="d"로 정수 표시
    plt.xlabel(column2)
    plt.ylabel(column1)
    plt.title(title)
    plt.gca().invert_yaxis()
    plt.savefig(f'{column1}_{column2}_heatmap.png')

draw_barplot(df, 'eyelid_group', 'eyelid_group distribution')
draw_heatmap(df, 'dpi', 'eyelid_group', 'dpi vs eyelid_group heatmap')