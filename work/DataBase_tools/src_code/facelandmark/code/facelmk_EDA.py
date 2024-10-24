import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('FaceLandmark_300vw.csv')
df2 = pd.read_csv('FaceLandmark_300w.csv')
df3 = pd.read_csv('FaceLandmark_300w_lp.csv')
df4 = pd.read_csv('FaceLandmark_300w_3d.csv')
df5 = pd.read_csv('FaceLandmark_aflw2000.csv')
df6 = pd.read_csv('FaceLandmark_cofw.csv')
df7 = pd.read_csv('FaceLandmark_dibox.csv')
df8 = pd.read_csv('FaceLandmark_frgc.csv')
df9 = pd.read_csv('FaceLandmark_Menpo2D.csv')
df10 = pd.read_csv('FaceLandmark_MultiPIE.csv')
df11 = pd.read_csv('FaceLandmark_sai.csv')
df12 = pd.read_csv('FaceLandmark_xm2vts.csv')

df = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12])
df['head_angle_check'] = df['Head_yaw'].apply(lambda x: 'unknown' if pd.isna(x) else 'known')
df['head_yaw_bins'] = pd.cut(df['Head_yaw'], bins=[-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90])
df['head_pitch_bins'] = pd.cut(df['Head_pitch'], bins=[-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90])
df['head_roll_bins'] = pd.cut(df['Head_roll'], bins=[-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90])

def draw_barplot(df, column, title):
    df_column = df[column].value_counts().reset_index()
    df_column.columns = [column, 'count']
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

# print(df.head())

draw_barplot(df, 'Facelandmark_pts','Facelandmark_pts Distribution')
draw_barplot(df, 'head_angle_check','head_angle_check Distribution')
draw_heatmap(df, 'head_pitch_bins', 'head_yaw_bins', 'head_pitch_bins vs head_yaw_bins')
draw_heatmap(df, 'head_yaw_bins', 'head_roll_bins', 'head_yaw_bins vs head_roll_bins')
draw_heatmap(df, 'head_pitch_bins', 'head_roll_bins', 'head_pitch_bins vs head_roll_bins')
