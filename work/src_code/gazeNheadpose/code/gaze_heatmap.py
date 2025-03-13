import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df1 = pd.read_csv('gaze_sai.csv')
df2 = pd.read_csv('gaze_eth.csv')
df3 = pd.read_csv('gaze_360.csv')
df4 = pd.read_csv('gaze_mpii.csv')
df5 = pd.read_csv('gaze_mpii2.csv')
df6 = pd.read_csv('gaze_eth1.csv')
df7 = pd.read_csv('gaze_eth2.csv')
df8 = pd.read_csv('gaze_eth3.csv')
df9 = pd.read_csv('gaze_eth4.csv')
df10 = pd.read_csv('gaze_utmulti.csv')
df11 = pd.read_csv('gaze_utmulti1.csv')

df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8,df9,df10,df11])

# print(df)

df['pitch_bins'] = pd.cut(df['Gaze_y'], bins=[-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45])
df['yaw_bins'] = pd.cut(df['Gaze_x'], bins=[-45,-40,-35,-30,-25,-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45])

plt.figure(figsize=(13, 13))
heatmap_data = df.pivot_table(index='pitch_bins', columns='yaw_bins', values='label', aggfunc='count')
sns.heatmap(heatmap_data, cmap='Blues', annot=True, fmt="d")  # annot=True 추가하여 숫자 표시, fmt="d"로 정수 표시

plt.xlabel('Yaw')
plt.ylabel('Pitch')
plt.title('Gaze Heatmap')
plt.gca().invert_yaxis()
plt.savefig('gaze_heatmap.png')
plt.show()