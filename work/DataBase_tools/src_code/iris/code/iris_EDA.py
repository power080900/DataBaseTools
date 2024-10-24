import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('iris_300vw.csv')
df2 = pd.read_csv('iris_300w.csv')
df3 = pd.read_csv('iris_300w_lp.csv')
df4 = pd.read_csv('iris_300w_3d.csv')
df5 = pd.read_csv('iris_aflw2000.csv')
df6 = pd.read_csv('iris_cofw.csv')
df7 = pd.read_csv('iris_dibox.csv')
df8 = pd.read_csv('iris_frgc.csv')
df9 = pd.read_csv('iris_Menpo2D.csv')
df10 = pd.read_csv('iris_MultiPIE.csv')
df11 = pd.read_csv('combined_iris_sai.csv')
df12 = pd.read_csv('iris_xm2vts.csv')

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df12])

df['iris_size_group'] = pd.cut(df['iris_size'], bins=[0,250,500,750,1000,1250,1500,1750,2000,2250,2500,2750,3000,10000], labels=['(0,250]', '(250,500]', '(500,750]', '(750,1000]', '(1000,1250]', '(1250,1500]', '(1500,1750]', '(1750,2000]', '(2000,2250]', '(2250,2500]', '(2500,2750]', '(2750,3000]', '(3000+'])

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

draw_barplot(df, 'iris_size_group', 'iris_size_group distribution')
draw_heatmap(df, 'iris_size_group', 'eye_side', 'iris_size_group vs eye_side heatmap')