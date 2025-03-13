import cv2
import numpy as np
import os
import sys
sys.path.append('../../src')
import DISData as DD
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

doUT = DD.SQL()

data_name = 'AIhub_drivers_monitoring_video'
query = f'''select label, count(video_dir) as count from DeepInSight.{data_name}_info group by label;'''

db = doUT.db
conn = doUT.conn
conn.execute(query)
column_names = [desc[0] for desc in conn.description]
result = conn.fetchall()
db.commit()

df = pd.DataFrame(result, columns=column_names)
df['count'] = df['count'].astype('int64')

df = df.sort_values(by='count',ascending=False)

plt.rcParams['axes.unicode_minus'] = False  # 음수 부호 깨짐 방지
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['font.size'] = 12

try:
    plt.figure(figsize=(8, 6))
    plt.rc('font', family='NanumGothic')
    sns.set(style="whitegrid")
    ax = sns.barplot(x='label', y='count', data=df, hue='label')
    for p in ax.patches:
        label = p.get_height()  # 막대의 너비를 가져와서 count로 사용
        count = p.get_x() + p.get_width() / 2  # 막대의 y 좌표를 가져와서 label로 사용
        ax.annotate(f'{label}', (count, label), ha='center', va='center', fontsize=10, color='black')
    plt.xlabel('label')
    plt.ylabel('count')
    plt.title('Count of Labels')
    save_path = f'label/{data_name}_label.png'
    if not os.path.exists('label'):
        os.makedirs('label')
    if os.path.exists(save_path):
        os.remove(save_path)
    plt.savefig(save_path)
except Exception as e:
    print(e)

query2 = f'''select label, count(img_dir) as count from DeepInSight.{data_name}_landmark_info group by label;'''

db = doUT.db
conn = doUT.conn
conn.execute(query2)
column_names = [desc[0] for desc in conn.description]
result2 = conn.fetchall()
db.commit()

df2 = pd.DataFrame(result2, columns=column_names)
df2['count'] = df2['count'].astype('int64')

df2 = df2.sort_values(by='count',ascending=False)

try:
    plt.figure(figsize=(8, 6))
    sns.set(style="whitegrid")
    ax = sns.barplot(x='label', y='count', data=df2, hue='label')
    for p in ax.patches:
        label = p.get_height()  # 막대의 너비를 가져와서 count로 사용
        count = p.get_x() + p.get_width() / 2  # 막대의 y 좌표를 가져와서 label로 사용
        ax.annotate(f'{label}', (count, label), ha='center', va='center', fontsize=10, color='black')
    plt.xlabel('label')
    plt.ylabel('count')
    plt.title('Count of Labels')
    save_path = f'label/{data_name}_label2.png'
    if not os.path.exists('label'):
        os.makedirs('label')
    if os.path.exists(save_path):
        os.remove(save_path)
    plt.savefig(save_path)
except Exception as e:
    print(e)

conn.close()
