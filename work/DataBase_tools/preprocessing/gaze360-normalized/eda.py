import sys
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sys.path.append('../')
import numpy as np
import EDA_utils as EU

df = EU.search_SQL('Gaze360_normalized')


df.columns = ['id','face_dir','left_dir', 'right_dir', 'img_format', 'color_space', 'label_dir', 'label_format', 'x_3d', 'y_3d', 'z_3d', 'yaw_2d', 'pitch_2d', 'project_id']
df1 = df.drop(['id','face_dir','left_dir', 'right_dir', 'img_format', 'color_space', 'label_dir', 'label_format', 'x_3d', 'y_3d', 'z_3d', 'project_id'], axis=1)
df1['x_2d'] = np.rad2deg(df1['yaw_2d'].astype(float).round(4))
df1['y_2d'] = np.rad2deg(df1['pitch_2d'].astype(float).round(4))

df2 = df1
print(df2['x_2d'].max())
print(df2['x_2d'].min())
print(df2['y_2d'].max())
print(df2['y_2d'].min())
df2['x_2d_category'] = pd.cut(df2['x_2d'], bins=[round(-200.0 + 50.0*i,4) for i in range(10)], labels=[round(-200.0 + 50.0*i,4) for i in range(9)])
df2['y_2d_category'] = pd.cut(df2['y_2d'], bins=[round(-100.0 + 25.0*i,4) for i in range(10)], labels=[round(-100.0 + 25.0*i,4) for i in range(9)])

df3 = df2.drop(['yaw_2d','pitch_2d', 'x_2d', 'y_2d'], axis=1)
df3 = df3.pivot_table(index='y_2d_category', columns='x_2d_category', aggfunc='size')

EU.draw_heatmap(df3,'x_2d','y_2d','Figure_1.png',reverse=True)
# EU.draw_jointplot(df2,'x_2d','y_2d','Figure_2.png')

