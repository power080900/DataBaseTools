import utils
import glob
import os
import mysql.connector
from PIL import Image
import numpy as np
import shutil

label_list = utils.file_list('*.label')

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

project_name = os.getcwd().split('\\')[-1]
project_dir = f'Database/{project_name}'

print(project_name)
print(project_dir)

conn.execute(f'''insert into dataset_info(project_name, project_dir, description)
             values ('{project_name}', '{project_dir}', 8)''')
db.commit()

conn.execute(f'''CREATE TABLE IF NOT EXISTS {project_name}_gazeAngle_info(
            id INT PRIMARY KEY AUTO_INCREMENT,
            img_name VARCHAR(255) NOT NULL,
            img_dir VARCHAR(1000) NOT NULL,
            img_format VARCHAR(10) NOT NULL,
            img_width INT NOT NULL,
            img_height INT NOT NULL,
            color_space VARCHAR(10) NOT NULL,
            label_name VARCHAR(255) NOT NULL,
            label_dir VARCHAR(1000) NOT NULL,
            label_format VARCHAR(10) NOT NULL,
            label VARCHAR(20) NOT NULL,
            landmark VARCHAR(1000),
            project_id INT,
            FOREIGN KEY (project_id) REFERENCES dataset_info(project_id));''')
