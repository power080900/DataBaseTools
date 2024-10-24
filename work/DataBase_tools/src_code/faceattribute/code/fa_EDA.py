import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('fa_sai.csv')
df1['hair_length_group'] = pd.cut(df1['hair_length'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], labels=['(0,10]', '(10,20]', '(20,30]', '(30,40]', '(40,50]', '(50,60]', '(60,70]', '(70,80]', '(80,90]', '(90,100]'])
df1['facial_hair_length_group'] = pd.cut(df1['facial_hair_length'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100], labels=['(0,10]', '(10,20]', '(20,30]', '(30,40]', '(40,50]', '(50,60]', '(60,70]', '(70,80]', '(80,90]', '(90,100]'])
df1['glasses_transparency_group'] = pd.cut(df1['glasses_transparency'], bins=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1], labels=['(0,0.1]', '(0.1,0.2]', '(0.2,0.3]', '(0.3,0.4]', '(0.4,0.5]', '(0.5,0.6]', '(0.6,0.7]', '(0.7,0.8]', '(0.8,0.9]', '(0.9,1]'])

def draw_barplot(df, column, title):
    df_column = df[column].value_counts().reset_index().sort_index()
    df_column.columns = [column, 'count']
    df_column = df_column.sort_values(by=column)

    plt.figure(figsize=(20, 12))
    sns.barplot(x=column, y='count', data=df_column)
    for index, value in enumerate(df_column['count']):
        plt.text(index, value, str(value), ha='center', va='bottom')
    plt.title(title)
    plt.savefig(f'{column}_distribution.png')

def draw_barhplot(df, column, title):
    df_column = df[column].value_counts().reset_index().sort_index()
    df_column.columns = [column, 'count']
    df_column = df_column.sort_values(by=column)

    plt.figure(figsize=(20, 12))
    sns.barplot(x='count', y=column, data=df_column)
    for index, value in enumerate(df_column['count']):
        plt.text(value, index, str(value), ha='center', va='bottom')
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

draw_barhplot(df1, 'expression', 'expression distribution')
draw_barhplot(df1, 'hair_style', 'hair_style distribution')
draw_heatmap(df1, 'hair_style','hair_length_group', 'hair_style vs hair_length heatmap')
draw_barhplot(df1, 'facial_hair', 'facial_hair distribution')
draw_heatmap(df1, 'facial_hair','facial_hair_length_group', 'facial_hair vs facial_hair_length heatmap')
draw_barhplot(df1, 'glasses', 'glasses distribution')
draw_heatmap(df1, 'glasses_lens','glasses_transparency_group', 'glasses_lens vs glasses_transparency heatmap')
draw_barhplot(df1, 'headwear', 'headwear distribution')
