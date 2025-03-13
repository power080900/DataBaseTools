import sys
import numpy as np
import pandas as pd
sys.path.append('../')
import EDA_utils as EU

df = EU.MakeSQL.search_SQL('mpiigaze')

# whole data

df.columns = ['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'Origin', 'WhichEye', 'Gaze_3D', 'Head_3D', 'Gaze_2D', 'Head_2D', 'Rmat', 'Smat', 'GazeOrigin']

g_df1 = df.drop(['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'Origin', 'WhichEye', 'Head_3D', 'Gaze_3D', 'Head_2D', 'Rmat', 'Smat', 'GazeOrigin'], axis=1)
g_df1['x_2d'] = np.rad2deg(g_df1['Gaze_2D'].str.split(',').str[0].astype(float).round(4))
g_df1['y_2d'] = np.rad2deg(g_df1['Gaze_2D'].str.split(',').str[1].astype(float).round(4))

g_df2 = g_df1
g_df2['x_2d_category'] = pd.cut(g_df2['x_2d'], bins=[round(-40.0 + 10.0*i,4) for i in range(10)], labels=[round(-40.0 + 10.0*i,4) for i in range(9)])
g_df2['y_2d_category'] = pd.cut(g_df2['y_2d'], bins=[round(-30.0 + 5.0*i,4) for i in range(9)], labels=[round(-30.0 + 5.0*i,4) for i in range(8)])
g_df3 = g_df2.drop(['Gaze_2D','x_2d', 'y_2d'], axis=1)
g_df3 = g_df3.pivot_table(index='y_2d_category', columns='x_2d_category', aggfunc='size')
g_df2 = g_df2.drop(['Gaze_2D','x_2d_category', 'y_2d_category'], axis=1)

EU.draw_heatmap(g_df3,'x_2d','y_2d','Figure_1.png',reverse=True)
EU.draw_jointplot(g_df2,'x_2d','y_2d','Figure_2.png',reverse=False)

# #right_eye
result_right = df.loc[df['WhichEye'] == 'right']
df_right1 = result_right.drop(['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'Origin', 'WhichEye', 'Head_3D', 'Gaze_3D', 'Head_2D', 'Rmat', 'Smat', 'GazeOrigin'], axis=1)
df_right1['x_2d'] = np.rad2deg(df_right1['Gaze_2D'].str.split(',').str[0].astype(float).round(4))
df_right1['y_2d'] = np.rad2deg(df_right1['Gaze_2D'].str.split(',').str[1].astype(float).round(4))

df_right2 = df_right1
df_right2['x_2d_category'] = pd.cut(df_right2['x_2d'], bins=[round(-40.0 + 10.0*i,4) for i in range(10)], labels=[round(-40.0 + 10.0*i,4) for i in range(9)])
df_right2['y_2d_category'] = pd.cut(df_right2['y_2d'], bins=[round(-30.0 + 5.0*i,4) for i in range(9)], labels=[round(-30.0 + 5.0*i,4) for i in range(8)])

df_right3 = df_right2.drop(['Gaze_2D','x_2d', 'y_2d'], axis=1)
df_right3 = df_right3.pivot_table(index='y_2d_category', columns='x_2d_category', aggfunc='size')
df_right2 = df_right2.drop(['Gaze_2D','x_2d_category', 'y_2d_category'], axis=1)

EU.draw_heatmap(df_right3,'x_2d','y_2d','Figure_right_1.png',reverse=True)
EU.draw_jointplot(df_right2,'x_2d','y_2d','Figure_right_2.png',reverse=False)


# # #left_eye
result_left = df.loc[df['WhichEye'] == 'left']
df_left1 = result_left.drop(['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'Origin', 'WhichEye', 'Head_3D', 'Gaze_3D', 'Head_2D', 'Rmat', 'Smat', 'GazeOrigin'], axis=1)

df_left1['x_2d'] = np.rad2deg(df_left1['Gaze_2D'].str.split(',').str[0].astype(float).round(4))
df_left1['y_2d'] = np.rad2deg(df_left1['Gaze_2D'].str.split(',').str[1].astype(float).round(4))

df_left2 = df_left1
df_left2['x_2d_category'] = pd.cut(df_left2['x_2d'], bins=[round(-40.0 + 10.0*i,4) for i in range(10)], labels=[round(-40.0 + 10.0*i,4) for i in range(9)])
df_left2['y_2d_category'] = pd.cut(df_left2['y_2d'], bins=[round(-30.0 + 5.0*i,4) for i in range(9)], labels=[round(-30.0 + 5.0*i,4) for i in range(8)])

df_left3 = df_left2.drop(['Gaze_2D','x_2d', 'y_2d'], axis=1)
df_left3 = df_left3.pivot_table(index='y_2d_category', columns='x_2d_category', aggfunc='size')
df_left2 = df_left2.drop(['Gaze_2D','x_2d_category', 'y_2d_category'], axis=1)

EU.draw_heatmap(df_left3,'x_2d','y_2d','Figure_left_1.png',reverse=True)
EU.draw_jointplot(df_left2,'x_2d','y_2d','Figure_left_2.png',reverse=False)

print('done')