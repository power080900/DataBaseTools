import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# 데이터 로드
df1 = pd.read_csv('human_attribute_prevent_controll.csv')
df2 = pd.read_csv('human_attribute_prevent_real.csv')
df3 = pd.read_csv('human_attribute_prevent_semi.csv')
df4 = pd.read_csv('human_attribute_sai.csv', index_col=0)

df = pd.concat([df1, df2, df3, df4])

df['age_group'] = pd.cut(df['age'], bins=[0, 19, 29, 39, 49, 59, 69, 100], labels=['0-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70+'])
df['height'] = df['height'].replace('unknown', np.nan)
df['weight'] = df['weight'].replace('unknown', np.nan)
df['skin_type'] = df['skin_type'].replace('unknown', np.nan)
df['height_check'] = df['height'].apply((lambda x: 'unknown' if pd.isna(x) else 'known'))
df['weight_check'] = df['weight'].apply((lambda x: 'unknown' if pd.isna(x) else 'known'))
df['skin_type_check'] = df['skin_type'].apply((lambda x: 'unknown' if pd.isna(x) else 'known'))

df['height_group'] = pd.cut(df['height'], bins=[0, 150, 160, 170, 180, 190, 200], labels=['-150)', '[150, 160)', '[160, 170)', '[170, 180)', '[180, 190)', '[190+'])
df['weight_group'] = pd.cut(df['weight'], bins=[50, 60, 70, 80, 90, 100, 110], labels=['-60)', '[60-70)', '[70-80)', '[80-90)', '[90-100)', '[100+'])
df['skin_type_group'] = pd.cut(df['skin_type'], bins=[1, 2, 3, 4, 5, 6], labels=['1-2', '2-3', '3-4', '4-5', '5-6'])

def draw_barplot(df, column, title):
    df_column = df[column].value_counts().reset_index()
    df_column.columns = [column, 'count']

    df_column = df_column.sort_values(by=column)

    print(df_column)
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

draw_barplot(df, 'age_group','Age Distribution')
draw_barplot(df, 'gender','Gender Distribution')
draw_barplot(df, 'height_check','Height Distribution')
draw_barplot(df, 'weight_check','Weight Distribution')
draw_barplot(df, 'skin_type_check','Skin Type Distribution')
draw_barplot(df, 'height_group','Height Distribution')
draw_barplot(df, 'weight_group','Weight Distribution')
draw_barplot(df, 'skin_type_group','Skin Type Distribution')
draw_barplot(df, 'ethnicity','Ethnicity Distribution')
draw_heatmap(df, 'age_group','gender','Age vs Gender Heatmap')
draw_heatmap(df, 'age_group','ethnicity','Age vs Ethnicity Heatmap')
draw_heatmap(df, 'height_group','weight_group','Height vs Weight Heatmap')
draw_heatmap(df, 'gender','ethnicity','Gender vs Ethnicity Heatmap')

draw_barplot(df, 'glasses','Glasses Distribution')
draw_barplot(df, 'cap','Cap Distribution')
draw_barplot(df, 'mask','Mask Distribution')


