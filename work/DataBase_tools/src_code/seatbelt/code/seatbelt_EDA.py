import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('seatbelt_coco.csv')
df2 = pd.read_csv('seatbelt_DV2023.csv')
df3 = pd.read_csv('seatbelt_images_cv.csv')

df = pd.concat([df1,df2,df3])

def draw_barplot(df, column, title):
    df_column = df[column].value_counts().reset_index()
    df_column.columns = [column, 'count']
    plt.figure(figsize=(10, 6))
    sns.barplot(x=column, y='count', data=df_column)
    for index, value in enumerate(df_column['count']):
        plt.text(index, value, str(value), ha='center', va='bottom')
    plt.title(title)
    plt.savefig(f'{column}_distribution.png')


df['age'] = df['age'].replace('unknow', 'unknown')
df['gender'] = df['gender'].replace('unknow', 'unknown')
df['Lighting'] = df['Lighting'].replace('Unknown', 'unknown')
df['Action'] = df['Action'].replace('Unknown', 'unknown')
df['Occlusion'] = df['Occlusion'].replace('Unknown', 'unknown')
df['item'] = df['item'].replace('seatbelt_seatbelt', 'seatbelt')

draw_barplot(df, 'Lighting', 'Lighting Distribution')
draw_barplot(df, 'Action', 'Action Distribution')
draw_barplot(df, 'Occlusion', 'Occlusion Distribution')
draw_barplot(df, 'item', 'Item Distribution')
