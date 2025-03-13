import glob
import os
import mysql.connector
from PIL import Image
import math

# SQL 연결을 위한 정보
config = {
    'user': 'diadmin',
    'password': 'Dinsight0625!',
    'host': '192.168.0.128',
    'port': '3306',
    'database': 'DeepInSight',
    'raise_on_warnings': True,
}

db = mysql.connector.connect(**config)
conn = db.cursor()


project_dir = 'Z:\\GI4E'
project_name = project_dir.split('\\')[-1]
project_id = 9
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
                landmark VARCHAR(1000) NOT NULL,
                project_id INT,
                FOREIGN KEY (project_id) REFERENCES dataset_info(id));''')
except:
    pass

conn.execute(f'''insert into dataset_info(data_name, data_type, dataset_dir, dataset_id)
             values ('{project_name}','gaze', '{project_dir}','{project_id}')''')
db.commit()

# query 작성
query1 = (f'''INSERT INTO {project_name}_gaze_info 
        (img_dir, img_format, img_width, img_height, color_space,
        label_dir, label_format, 
        landmark, project_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)''')



# label 경로
label_path = 'Z:\GI4E\labels'

label_file = glob.glob(os.path.join(label_path, '*.txt'))
# print(label_file)

value_list1 = []
error_list = []

for label in label_file:
    label_name = label.split('\\')[-1].split('.')[0]
    with open(label, 'r') as f:
        config = f.readlines()
    
    for i in config:
        i.replace('\n','')
        file_name, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6 = i.split('\t')
        file_dir = os.path.join(os.path.dirname(label.replace('labels','images')), file_name)

        landmark = str(f'({x1},{y1}),({x2},{y2}),({x3},{y3}),({x4},{y4}),({x5},{y5}),({x6},{y6})')
            
        img_dir = f'Z:\\GI4E\\images\\{file_name}'
        img_format = file_name.split('.')[-1]
        img = Image.open(img_dir)
        img_width, img_height = img.size
        color_space = 'RGB'
        label_dir = label.replace('Z:','DataBase').replace('\\','/')
        img_dir = img_dir.replace('Z:','DataBase').replace('\\','/')
        label_format = 'txt'
    
        value = (img_dir, img_format, img_width, img_height, color_space,
                    label_dir, label_format, landmark, project_id)
        print(value)
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