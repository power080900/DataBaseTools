import sys
import os
import numpy as np
import pandas as pd
import cv2
sys.path.append('../')
import EDA_utils as EU

result = EU.search_SQL('Gaze360_normalized')

df = pd.DataFrame(result)
df.columns = ['id','face_dir','left_dir', 'right_dir', 'img_format',  'color_space', 'label_dir', 'label_format', 'x_3d', 'y_3d', 'z_3d', 'yaw_2d', 'pitch_2d', 'project_id']
df1 = df.drop(['id','face_dir','left_dir', 'right_dir', 'img_format',  'color_space', 'label_dir', 'label_format', 'x_3d', 'y_3d', 'z_3d', 'project_id'], axis=1)
df1['x_2d'] = -df1['yaw_2d'].astype(float).round(4)
df1['y_2d'] = -df1['pitch_2d'].astype(float).round(4)

for i in range(len(df['face_dir'])):
    face_dir = df['face_dir'][i].replace('DataBase', 'Z:')
    face_save = face_dir.replace('rawdata', 'checkdata')

    if not os.path.exists(os.path.dirname(face_save)):
        os.makedirs(os.path.dirname(face_save))

    x_2d = np.rad2deg(df1['x_2d'][i])
    y_2d = np.rad2deg(df1['y_2d'][i])
    
    face_image = cv2.imread(face_dir)
    height, width, channel = face_image.shape
    face_image = cv2.line(face_image, (int(width/2), int(height/2)), (int(width/2 + x_2d*100), int(height/2 + y_2d*100)), (0,0,255), 2)
    cv2.imwrite(face_save, face_image)

    print(f'write {i} done')
    



    
    

    
    

    

    
