import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def draw_barplot(df, column, title):
    df_column = df[column].value_counts().reset_index()
    df_column.columns = [column, 'count']

    df_column = df_column.sort_values(by=column)
    plt.figure(figsize=(10, 6))
    sns.barplot(x=column, y='count', data=df_column)
    for index, value in enumerate(df_column['count']):
        plt.text(index, value, str(value), ha='center', va='bottom')
    plt.title(title)
    plt.savefig(f'{column}_distribution.png')

def draw_barh_plot(df, column, title):
    df_column = df[column].value_counts().reset_index()
    df_column.columns = [column, 'count']
    df_column = df_column.sort_values(by='count')
    plt.figure(figsize=(20, 10))
    plt.barh(df_column[column], df_column['count'], color='skyblue')
    
    for index, value in enumerate(df_column['count']):
        plt.text(value, index, str(value), va='center', ha='left')
    plt.title(title)
    plt.xlabel('Count')
    plt.ylabel(column)
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

df = pd.read_csv('bodykey_sai.csv')

df['angle_group'] = pd.cut(df['angle'], bins=[0,5,10,15,20,25],labels=['(0,5]','(5,10]','(10,15]','(15,20]','(20,25]'])

draw_barplot(df,'angle_group','body angle distribution')
draw_barh_plot(df,'gesture','gesture distribution')