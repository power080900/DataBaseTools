import sys
import numpy as np
import pandas as pd
sys.path.append('../')
import EDA_utils as EU

df = EU.MakeSQL.search_SQL('rt_gene')

# whole data

df.columns = ['id','Face_img_dir', 'Face_img_format', 'Face_img_width', 'Face_img_height', 'Face_color_space',
          'Left_img_dir', 'Left_img_format', 'Left_img_width', 'Left_img_height', 'Left_color_space',
          'Right_img_dir', 'Right_img_format', 'Right_img_width', 'Right_img_height', 'Right_color_space',
          'label_dir', 'label_format', 'Origin', 'Gaze_3D', 'Head_3D', 'Gaze_2D', 'Head_2D']

g_df1 = df.drop(['id','Face_img_dir', 'Face_img_format', 'Face_img_width', 'Face_img_height', 'Face_color_space',
          'Left_img_dir', 'Left_img_format', 'Left_img_width', 'Left_img_height', 'Left_color_space',
          'Right_img_dir', 'Right_img_format', 'Right_img_width', 'Right_img_height', 'Right_color_space',
          'label_dir', 'label_format', 'Origin', 'Gaze_3D', 'Head_3D', 'Head_2D'], axis=1)
g_df1['x_2d'] = np.rad2deg(g_df1['Gaze_2D'].str.split(',').str[0].astype(float).round(4))
g_df1['y_2d'] = np.rad2deg(g_df1['Gaze_2D'].str.split(',').str[1].astype(float).round(4))

g_df2 = g_df1
g_df2['x_2d_category'] = pd.cut(g_df2['x_2d'], bins=[round(-80.0 + 20.0*i,4) for i in range(10)], labels=[round(-80.0 + 20.0*i,4) for i in range(9)])
g_df2['y_2d_category'] = pd.cut(g_df2['y_2d'], bins=[round(-40.0 + 10.0*i,4) for i in range(10)], labels=[round(-40.0 + 10.0*i,4) for i in range(9)])
g_df3 = g_df2.drop(['Gaze_2D','x_2d', 'y_2d'], axis=1)
g_df3 = g_df3.pivot_table(index='y_2d_category', columns='x_2d_category', aggfunc='size')
g_df2 = g_df2.drop(['Gaze_2D','x_2d_category', 'y_2d_category'], axis=1)

EU.draw_heatmap(g_df3,'x_2d','y_2d','Figure_1.png',reverse=True)
EU.draw_jointplot(g_df2,'x_2d','y_2d','Figure_2.png',80,40,reverse=False)

print('done')