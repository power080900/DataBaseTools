import sys
import os
import numpy as np
import pandas as pd
import cv2
sys.path.append('../')
import EDA_utils as EU

result = EU.MakeSQL.search_SQL('mpiigaze')

df = pd.DataFrame(result)
df.columns = ['id','img_dir', 'img_format', 'img_width', 'img_height', 'color_space', 'label_dir', 'label_format', 'Origin', 'WhichEye', 'Gaze_3D', 'Head_3D', 'Gaze_2D', 'Head_2D', 'Rmat', 'Smat', 'GazeOrigin']


for i in range(len(df['img_dir'])):
    img_dir = df['img_dir'][i].replace('DataBase', 'Z:')
    img_save = img_dir.replace('rawdata', 'checkdata')

    if not os.path.exists(os.path.dirname(img_save)):
        os.makedirs(os.path.dirname(img_save))
    
    x_2d, y_2d = map(float,df['Gaze_2D'][i].split(','))

    img = cv2.imread(img_dir)
    height, width, channel = img.shape

    center_x = int(width/2)
    center_y = int(height/2)
    
    line_length = 50

    img = cv2.line(img, (center_x, center_y), (int(center_x - x_2d*100), int(center_y - y_2d*100)), (0,0,255), 2)
    if not os.path.isfile(img_save):
        cv2.imwrite(img_save, img)
        cv2.destroyAllWindows()
        print(f'write {df["img_dir"][i]} done')
        # print(x_2d, y_2d)
