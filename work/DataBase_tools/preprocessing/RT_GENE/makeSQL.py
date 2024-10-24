import sys
import os
import pandas as pd
import cv2
from glob import glob
sys.path.append('../')
import EDA_utils as EU

# query 실행
query1 = (f'''CREATE TABLE rt_gene_info (
            id INT(11) NOT NULL AUTO_INCREMENT primary key,
            Face_img_dir VARCHAR(100) NOT NULL,
            Face_img_format VARCHAR(10) NOT NULL,
            Face_img_width INT(11) NOT NULL,
            Face_img_height INT(11) NOT NULL,
            Face_color_space VARCHAR(10) NOT NULL,
        
            Left_img_dir VARCHAR(100) NOT NULL,
            Left_img_format VARCHAR(10) NOT NULL,
            Left_img_width INT(11) NOT NULL,
            Left_img_height INT(11) NOT NULL,
            Left_color_space VARCHAR(10) NOT NULL,
          
            Right_img_dir VARCHAR(100) NOT NULL,
            Right_img_format VARCHAR(10) NOT NULL,
            Right_img_width INT(11) NOT NULL,
            Right_img_height INT(11) NOT NULL,
            Right_color_space VARCHAR(10) NOT NULL,
          
            label_dir VARCHAR(100) NOT NULL,
            label_format VARCHAR(10) NOT NULL,
            Origin VARCHAR(100) NOT NULL,
            Gaze_3D VARCHAR(1000) NOT NULL,
            Head_3D VARCHAR(1000) NOT NULL,
            Gaze_2D VARCHAR(1000) NOT NULL,
            Head_2D VARCHAR(1000) NOT NULL);''')
try:
    EU.MakeSQL.create_table(query1)
except:
    pass

query2 = (f'''INSERT INTO rt_gene_info 
        (Face_img_dir, Face_img_format, Face_img_width, Face_img_height, Face_color_space,
          Left_img_dir, Left_img_format, Left_img_width, Left_img_height, Left_color_space,
          Right_img_dir, Right_img_format, Right_img_width, Right_img_height, Right_color_space,
          label_dir, label_format, Origin, Gaze_3D, Head_3D, Gaze_2D, Head_2D) 
          VALUES (%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s)''')



# label 경로
label_path = 'Z:\\RT_GENE\\data\\RGB\\labeldata\\*'

label_file = glob(os.path.join(label_path, '*.label'))
print(label_file)

value_list1 = []
error_list = []

for label in label_file:
    with open(label, 'r') as f:
        texts = f.readlines()
    for line in texts[1:]:
        Face_img, Left_img, Right_img , Origin, Gaze_3D, Head_3D, Gaze_2D, Head_2D = line.split(' ')
        Face_img_dir = f'Z:\\RT_GENE\\data\\RGB\\rawdata\\{Face_img}'
        Left_img_dir = f'Z:\\RT_GENE\\data\\RGB\\rawdata\\{Left_img}'
        Right_img_dir = f'Z:\\RT_GENE\\data\\RGB\\rawdata\\{Right_img}'

        Face_img_name = Face_img_dir.split('\\')[-1]
        Left_img_name = Left_img_dir.split('\\')[-1]
        Right_img_name = Right_img_dir.split('\\')[-1]

        Face_img = cv2.imread(Face_img_dir)
        Left_img = cv2.imread(Left_img_dir)
        Right_img = cv2.imread(Right_img_dir)

        Face_img_format = 'png'
        Left_img_format = 'png'
        Right_img_format = 'png'

        Face_img_width = Face_img.shape[1]
        Face_img_height = Face_img.shape[0]
        Left_img_width = Left_img.shape[1]
        Left_img_height = Left_img.shape[0]
        Right_img_width = Right_img.shape[1]
        Right_img_height = Right_img.shape[0]

        Face_color_space = 'RGB'
        Left_color_space = 'RGB'
        Right_color_space = 'RGB'

        label_dir = label
        label_format = 'label'

        Face_img_dir = Face_img_dir.replace('Z:','DataBase')
        Left_img_dir = Left_img_dir.replace('Z:','DataBase')
        Right_img_dir = Right_img_dir.replace('Z:','DataBase')

        Head_2D = Head_2D.replace('\n','')

        value = (Face_img_dir, Face_img_format, Face_img_width, Face_img_height, Face_color_space,
          Left_img_dir, Left_img_format, Left_img_width, Left_img_height, Left_color_space,
          Right_img_dir, Right_img_format, Right_img_width, Right_img_height, Right_color_space,
          label_dir, label_format, Origin, Gaze_3D, Head_3D, Gaze_2D, Head_2D)
        
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
      