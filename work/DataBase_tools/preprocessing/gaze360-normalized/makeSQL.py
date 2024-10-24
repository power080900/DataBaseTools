import glob
import os
import sys
from PIL import Image
sys.path.append('../')
import EDA_utils as EU

query = '''CREATE TABLE IF NOT EXISTS Gaze360_normalized_info(
                id INT PRIMARY KEY AUTO_INCREMENT,
                Face_dir VARCHAR(1000) NOT NULL,
                left_dir VARCHAR(1000) NOT NULL,
                right_dir VARCHAR(1000) NOT NULL,
                img_format VARCHAR(10) NOT NULL,
                color_space VARCHAR(10) NOT NULL,
                label_dir VARCHAR(1000) NOT NULL,
                label_format VARCHAR(10) NOT NULL,
                x_3d FLOAT NOT NULL,
                y_3d FLOAT NOT NULL, 
                z_3d FLOAT NOT NULL,
                yaw_2d FLOAT NOT NULL, 
                pitch_2d FLOAT NOT NULL,
                project_id INT,
                FOREIGN KEY (project_id) REFERENCES dataset_info(id));'''
try:
    EU.MakeSQL.create_table(query)
except:
    print('table already exists')

# query 작성
query1 = (f'''INSERT INTO Gaze360_normalized_info
        (Face_dir, left_dir, right_dir, img_format, color_space,
        label_dir, label_format, 
        x_3d, y_3d, z_3d, yaw_2d, pitch_2d,
        project_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''')


# label 경로
label_path = 'Z:\\Gaze360_normalized\\data\\RGB\\labeldata'

label_file = glob.glob(os.path.join(label_path, '*\\*.label'))


value_list1 = []
error_list = []

for label in label_file:
    label_name = label.split('\\')[-1].split('.')[0]
    if label_name != 'unused':
        with open(label, 'r') as f:
            texts = f.readlines()
        
        for text in texts[1:]:
            
            face, left, right, origin, point_3ds, point_2ds = text.split(' ')
            face = face.split('/')[-1]

            x_3d, y_3d, z_3d = map(float, point_3ds.split(','))
            x_3d = x_3d
            yaw_2d, pitch_2d = map(float, point_2ds.split(','))
            
            face_dir = f'Z:\\Gaze360_normalized\\data\\RGB\\rawdata\\{face}'
            face_dir = face_dir.replace('Z:','DataBase').replace('\\','/')
            left_dir = f'Z:\\Gaze360_normalized\\data\\RGB\\rawdata\\{left}'
            left_dir = left_dir.replace('Z:','DataBase').replace('\\','/')
            right_dir = f'Z:\\Gaze360_normalized\\data\\RGB\\rawdata\\{right}'
            right_dir = right_dir.replace('Z:','DataBase').replace('\\','/')
            img_format = face.split('.')[-1]
            color_space = 'RGB'
            label_dir = label.replace('Z:','DataBase').replace('\\','/')
            
            label_format = 'label'
        
            value = (face_dir, left_dir, right_dir, img_format, color_space,
                      label_dir, label_format, 
                      x_3d, y_3d, z_3d, yaw_2d, pitch_2d, 8)
            # print(value)
            value_list1.append(value)

            # query 실행

            if len(value_list1) >= 500:
                print(f'insert {len(value_list1)}')
                EU.MakeSQL.insert_dataset_values(query1, value_list1)
                value_list1 = []
EU.MakeSQL.insert_dataset_values(query1, value_list1)
# print(value_list2)
value_list1 = []

print('done')            