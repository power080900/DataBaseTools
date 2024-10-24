import os
import sys
sys.path.append('../../src')
import DISData as DD
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

doUT = DD.SQL()
data_name = 'AIhub_drivers_monitoring'
query = f'''select label, count(label) as count from DeepInSight.{data_name}_box_info group by label;'''

db = doUT.db
conn = doUT.conn
conn.execute(query)
column_names = [desc[0] for desc in conn.description]
result = conn.fetchall()
db.commit()

df = pd.DataFrame(result, columns=column_names)
df['count'] = df['count'].astype('int64')

df = df.sort_values(by='count')

try:
    plt.figure(figsize=(20, 8))
    sns.set(style="whitegrid")
    ax = sns.barplot(x='count', y='label', data=df, hue='label')
    for p in ax.patches:
        count = p.get_width()  # 막대의 너비를 가져와서 count로 사용
        label = p.get_y() + p.get_height() / 2  # 막대의 y 좌표를 가져와서 label로 사용
        ax.annotate(f'{count}', (count, label), ha='center', va='center', fontsize=10, color='black')
    plt.xlabel('Count')
    plt.ylabel('Label')
    plt.title('Count of Labels')
    save_path = f'label/{data_name}_label.png'
    if not os.path.exists('label'):
        os.makedirs('label')
    if os.path.exists(save_path):
        os.remove(save_path)
    plt.savefig(save_path)
except Exception as e:
    print(e)

query2 = f'''select action, count(label) as count from DeepInSight.{data_name}_box_info group by action;'''

df2 = pd.DataFrame(result2, columns=column_names)
df2['count'] = df2['count'].astype('int64')

df2 = df2.sort_values(by='count')
df2

try:
    plt.figure(figsize=(20, 8))
    plt.rc('font', family='NanumBarunGothic')
    plt.rc('axes', unicode_minus=False)
    sns.set(style="whitegrid")
    ax = sns.barplot(x='count', y='action', data=df2, hue='action')
    for p in ax.patches:
        count = p.get_width()  # 막대의 너비를 가져와서 count로 사용
        label = p.get_y() + p.get_height() / 2  # 막대의 y 좌표를 가져와서 label로 사용
        ax.annotate(f'{count}', (count, action), ha='center', va='center', fontsize=10, color='black')
    plt.xlabel('Count')
    plt.ylabel('Label')
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
