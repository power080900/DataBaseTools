import utils
import getpass
import glob
import os
import mysql.connector
from PIL import Image
import math

# SQL 연결을 위한 정보

user = input('user: ')
password = getpass.getpass('password: ')
host = input('host: ')
port = input('port: ')
database = input('database: ')

config = {
    'user': user,
    'password': password,
    'host': host,
    'port': port,
    'database': database,
    'raise_on_warnings': True,
}

db = mysql.connector.connect(**config)
conn = db.cursor()

project_name = input('project_name: ')

project_dir = f'Z:\\{project_name}'
project_name = project_dir.split('\\')[-1]
project_id = 8
print(project_name)
print(project_dir)

try:
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {project_name}_gaze_info(
                id INT PRIMARY KEY AUTO_INCREMENT,
                img_dir VARCHAR(1000) NOT NULL,
                img_format VARCHAR(10) NOT NULL,
                img_width INT NOT NULL,
                img_height INT NOT NULL,
                color_space VARCHAR(10) NOT NULL,
                label_dir VARCHAR(1000) NOT NULL,
                label_format VARCHAR(10) NOT NULL,
                x_3d FLOAT NOT NULL,
                y_3d FLOAT NOT NULL, 
                z_3d FLOAT NOT NULL,
                yaw_2d FLOAT NOT NULL, 
                pitch_2d FLOAT NOT NULL,
                pitch_degrees FLOAT NOT NULL,
                yaw_degrees FLOAT NOT NULL,
                project_id INT,
                FOREIGN KEY (project_id) REFERENCES dataset_info(id));''')
except:
    pass

# conn.execute(f'''insert into dataset_info(data_name, data_type, dataset_dir, dataset_id)
#              values ('{project_name}','gaze', '{project_dir}','{project_id}')''')
db.commit()

# query 작성
query1 = (f'''INSERT INTO {project_name}_gaze_info 
        (img_dir, img_format, img_width, img_height, color_space,
        label_dir, label_format, 
        x_3d, y_3d, z_3d, yaw_2d, pitch_2d, pitch_degrees, yaw_degrees,
        project_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''')



# label 경로
label_path = f'{project_dir}\\data\\RGB\\labeldata\\Face'

label_file = glob.glob(os.path.join(label_path, '*.label'))
print(label_file)

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

            magnitude = math.sqrt(x_3d**2 + y_3d**2 + z_3d**2)

            unit_vector = (x_3d / magnitude, y_3d / magnitude, z_3d / magnitude)

            pitch = math.asin(unit_vector[1])  # arcsin(y)
            yaw = math.atan2(unit_vector[0], -unit_vector[2])  # arctan(x/z)

            pitch_degrees = math.degrees(pitch)
            yaw_degrees = math.degrees(yaw)
            
            # if math.degrees(yaw) < 0:
            #     yaw_degrees = -180 - math.degrees(yaw) 
            # elif math.degrees(yaw) > 0:
            #     yaw_degrees = 180 - math.degrees(yaw)
            
            img_dir = f'{project_dir}\\data\\RGB\\rawdata\\Face\\{face}'
            img_format = face.split('.')[-1]
            img = Image.open(img_dir)
            img_width, img_height = img.size
            color_space = 'RGB'
            label_dir = label.replace('Z:','DataBase').replace('\\','/')
            img_dir = img_dir.replace('Z:','DataBase').replace('\\','/')
            label_format = 'label'
        
            value = (img_dir, img_format, img_width, img_height, color_space,
                      label_dir, label_format, 
                      x_3d, y_3d, z_3d, yaw_2d, pitch_2d, pitch_degrees, yaw_degrees, project_id)
            # print(value)
            value_list1.append(value)

            # query 실행

            if len(value_list1) >= 500:
                print(value_list1[0])
                conn.executemany(query1, value_list1)
                db.commit()
                value_list1 = []
                print(f'{len(value_list1)} / {len(label_file)}')
conn.executemany(query1,value_list1)
# print(value_list2)
value_list1 = []
db.commit()
print('done')      

conn.close()
db.close()        