import utils
import os
import mysql.connector
from PIL import Image
import scipy.io

img_list = utils.file_list('*.jpg')
label_list = utils.file_list('*.mat')

config = {
  'user': 'diadmin',
  'password': 'Dinsight0625!',
  'host': '192.168.0.128',
  'port': '3306',
  'database': 'DeepInSight',
  'raise_on_warnings': True
}

db = mysql.connector.connect(**config)
conn = db.cursor()

project_name = os.getcwd().split('\\')[-1]
project_dir = '/'.join(os.getcwd().split('\\')[-2:])
print(project_name)
print(project_dir)

try:
    conn.execute(f'''CREATE TABLE IF NOT EXISTS {project_name}_info(
                id INT PRIMARY KEY AUTO_INCREMENT,
                img_dir VARCHAR(1000) NOT NULL,
                img_format VARCHAR(10) NOT NULL,
                img_width INT NOT NULL,
                img_height INT NOT NULL,
                color_space VARCHAR(10) NOT NULL,
                label_dir VARCHAR(1000) NOT NULL,
                label_format VARCHAR(10) NOT NULL,
                label VARCHAR(20) NOT NULL,
                points_num INT,
                project_id INT,
                FOREIGN KEY (project_id) REFERENCES dataset_info(id));''')
except:
    pass

project_id = None
value_list1 = []
error_list = []

for cnt, label_file in enumerate(label_list):
    # print(label_file)
    file_name = os.path.basename(label_file)
    img_file = label_file.replace('_pts.mat','.jpg').replace('.mat','.jpg')
    # print(img_file)
    mat_data = scipy.io.loadmat(label_file)
    # print(mat_data)
        
    for para in mat_data.keys():
        label = None

        if para == '__header__' or para == '__version__' or para == '__globals__':
            continue
        elif para == 'pt2d':
            label = 'FaceLandmark'
            points_num = len(mat_data[para][0])
        elif para in ['roi','Illum_Para','Color_Para','Pose_Para']:
            label = para
            points_num = len(mat_data[para][0])
        elif para in ['Tex_Para','Shape_Para','Exp_Para']:

            label = para
            points_num = len(mat_data[para])
        elif para == 'pts_3d':
            label = 'FaceLandmark3D'
            points_num = len(mat_data[para])
        elif para == 'pts_2d':
            label = 'FaceLandmark2D'
            points_num = len(mat_data[para])

        # conn.execute(f'''insert into dataset_info(data_name, data_type, dataset_dir, dataset_id)
        #     values ('{project_name}','{para}', '{project_dir}','5')''')
        # db.commit()

        query1 = (f'''INSERT INTO {project_name}_info 
            (img_dir, img_format, img_width, img_height, color_space,
            label_dir, label_format, label, points_num, project_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''')
        
        conn.execute('''
            SELECT dataset_id, data_name, dataset_dir, data_type
            FROM dataset_info;''')
        result = conn.fetchall()
        
        if project_id == None:
            project_ids = {}
            for row in result:
                # print('row:',row)
                project_ids[row[1]] = row[0]
        # print(project_ids)

        # print(label_file)
        color_space = label_file.split('\\')[-4]
        
        dataset = label_file.split('\\')[-6]
        if project_id == None:
            project_id = project_ids.get(dataset, None)
        
        label_dir = '/'.join(os.path.dirname(label_file).split('\\')[-7:]+[os.path.basename(label_file)])
        label_name, label_format = os.path.splitext(os.path.basename(label_file))
        label_format = label_format.replace('.','')
        color_space = label_file.split('\\')[-4]
        
        img = label_file.split('\\')[-1].replace('_pts.mat','.jpg').replace('.mat','.jpg')
        img_dir = '/'.join(os.path.dirname(label_file).replace('label','image').split('\\')[-7:]+[f'{img}'])
        img_load = '\\'.join(os.path.dirname(label_file).replace('label','image').split('\\')+[f'{img}'])

        img_name, img_format = img.split('.')

        try:
            img = Image.open(img_load)
        except:
            print(f"error : {img_load}")
            error_list.append(img_load)
            continue
        img_width, img_height = img.size
        img_area = img_width * img_height
        img.close()
        

        value = (img_dir, img_format, img_width, img_height, color_space,
            label_dir, label_format, label, points_num, project_id)
        value_list1.append(value)
        # print(value_list1)
    
        if len(value_list1) >= 500:
            conn.executemany(query1,value_list1)
            print(f'{cnt} / {len(label_list)}')
            print(label_file)
            value_list1 = []
            db.commit()
conn.executemany(query1,value_list1)
value_list1 = []
db.commit()
print('done')      

conn.close()
db.close()