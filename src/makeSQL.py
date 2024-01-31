#makeSQL.py
import sys
import os
import pandas as pd
import cv2
from glob import glob
import EDA_utils as EU

# query 실행
query1 = (f'''CREATE TABLE _shanghaiTechGaze_info ( 
        id INT(11) NOT NULL AUTO_INCREMENT primary key,
        img_dir VARCHAR(100) NOT NULL,
        img_format VARCHAR(10) NOT NULL,
        img_width INT(11) NOT NULL,
        img_height INT(11) NOT NULL,
        color_space VARCHAR(10) NOT NULL,
          
        label_dir VARCHAR(100) NOT NULL,
        label_format VARCHAR(10) NOT NULL,
        Origin VARCHAR(100) NOT NULL,
        WhichEye VARCHAR(10) NOT NULL,
        Gaze_3D VARCHAR(1000) NOT NULL,
          
        Head_3D VARCHAR(1000) NOT NULL,
        Gaze_2D VARCHAR(1000) NOT NULL,
        Head_2D VARCHAR(1000) NOT NULL,
        Rmat VARCHAR(1000) NOT NULL,
        Smat VARCHAR(1000) NOT NULL,
          
        GazeOrigin VARCHAR(100) NOT NULL);''')
try:
    EU.MakeSQL.create_table(query1)
except:
    pass

query2 = (f'''INSERT INTO mpiigaze_info 
        (img_dir, img_format, img_width, img_height, color_space,
          label_dir, label_format, Origin, WhichEye, Gaze_3D, 
          Head_3D, Gaze_2D, Head_2D, Rmat, Smat, 
          GazeOrigin) VALUES (%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s)''')



# label 경로
label_path = 'Z:\\mpiigaze\\data\\IR\\labeldata'

label_file = glob(os.path.join(label_path, '*.label'))
# print(label_file)

value_list1 = []
error_list = []

for label in label_file:
    with open(label, 'r') as f:
        texts = f.readlines()
    for line in texts[1:]:
        img, Origin, WhichEye, Gaze_3D, Head_3D, Gaze_2D, Head_2D, Rmat, Smat, GazeOrigin = line.split(' ')
        img = img.replace('Z:','DataBase')
        img_name = img.split('\\')[-1]
        img_dir = label.replace('labeldata', 'rawdata').replace('.label', f'\\{img_name}')
        # print(img_dir)
        img_format = 'jpg'
        img = cv2.imread(img_dir)
        img_width = img.shape[1]
        img_height = img.shape[0]
        color_space = 'RGB'
        label_dir = label
        label_format = 'label'
        img_dir = img_dir.replace('Z:','DataBase')

        value = (img_dir, img_format, img_width, img_height, color_space,  label_dir, label_format, Origin, WhichEye, Gaze_3D,  Head_3D, Gaze_2D, Head_2D, Rmat, Smat,  GazeOrigin)
        # print(value)
        value_list1.append(value)

        # query 실행

        if len(value_list1) >= 500:
            print(value_list1[0])
            EU.MakeSQL.insert_dataset_values(query2, value_list1)
            value_list1 = []
            print(f'{len(value_list1)} / {len(label_file)}')
EU.MakeSQL.insert_dataset_values(query2, value_list1)
# print(value_list2)
value_list1 = []
print('done')