import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('headpose_sai.csv')
df2 = pd.read_csv('headpose_utmulti.csv')
df3 = pd.read_csv('headpose_utmulti1.csv')

df = pd.concat([df1,df2,df3])

df['pitch_bins'] = pd.cut(df['Gaze_y'], bins=[-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45])
df['yaw_bins'] = pd.cut(df['Gaze_x'], bins=[-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45])
df['head_yaw_bins'] = pd.cut(df['Head_yaw'], bins=[-40,-30,-20,-10,0,10,20,30,40])
df['head_pitch_bins'] = pd.cut(df['Head_pitch'], bins=[-50,-40,-30,-20,-10,0,10,20,30,40,0])
df['head_roll_bins'] = pd.cut(df['Head_roll'], bins=[-50,-40,-30,-20,-10,0,10,20,30,40,50])

plt.figure(figsize=(10, 10))
heatmap_data = df.pivot_table(index='pitch_bins', columns='yaw_bins', values='label', aggfunc='count')
sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt="d")  # annot=True 추가하여 숫자 표시, fmt="d"로 정수 표시

plt.xlabel('Yaw')
plt.ylabel('Pitch')
plt.title('Gaze Heatmap')
plt.gca().invert_yaxis()
plt.savefig('gaze_heatmap.png')
plt.show()

plt.figure(figsize=(10, 10))
heatmap_data = df.pivot_table(index='head_pitch_bins', columns='head_yaw_bins', values='label', aggfunc='count')
sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt="d")  # annot=True 추가하여 숫자 표시, fmt="d"로 정수 표시

plt.xlabel('Head Yaw')
plt.ylabel('Head Pitch')
plt.title('Head Pose Heatmap')
plt.gca().invert_yaxis()
plt.savefig('headpose_heatmap_py.png')
plt.show()

plt.figure(figsize=(10, 10))
heatmap_data = df.pivot_table(index='head_pitch_bins', columns='head_roll_bins', values='label', aggfunc='count')
sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt="d")  # annot=True 추가하여 숫자 표시, fmt="d"로 정수 표시

plt.xlabel('Head Roll')
plt.ylabel('Head Pitch')
plt.title('Head Pose Heatmap')
plt.gca().invert_yaxis()
plt.savefig('headpose_heatmap_pr.png')
plt.show()

plt.figure(figsize=(10, 10))
heatmap_data = df.pivot_table(index='head_yaw_bins', columns='head_roll_bins', values='label', aggfunc='count')
sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt="d")  # annot=True 추가하여 숫자 표시, fmt="d"로 정수 표시

plt.xlabel('Head Roll')
plt.ylabel('Head Yaw')
plt.title('Head Pose Heatmap')
plt.gca().invert_yaxis()
plt.savefig('headpose_heatmap_yr.png')
plt.show()

df['Head_gaze_x'] = df['Gaze_x'] + df['Head_yaw']
df['Head_gaze_y'] = df['Gaze_y'] + df['Head_pitch']

df['head_gaze_x_bins'] = pd.cut(df['Head_gaze_x'], bins=[-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90])
df['head_gaze_y_bins'] = pd.cut(df['Head_gaze_y'], bins=[-90,-80,-70,-60,-50,-40,-30,-20,-10,0,10,20,30,40,50,60,70,80,90])

plt.figure(figsize=(10, 10))
heatmap_data = df.pivot_table(index='head_gaze_y_bins', columns='head_gaze_x_bins', values='label', aggfunc='count')
sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt="d")  # annot=True 추가하여 숫자 표시, fmt="d"로 정수 표시

plt.xlabel('Head_yaw + Gaze X')
plt.ylabel('Head_pitch + Gaze Y')
plt.title('Head Gaze Heatmap')
plt.gca().invert_yaxis()
plt.savefig('head_gaze_heatmap.png')
