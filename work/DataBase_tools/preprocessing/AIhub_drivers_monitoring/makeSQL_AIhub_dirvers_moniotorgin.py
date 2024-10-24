import os
import json
import cv2
import sys
sys.path.append('../../src')
import DISData as DD

doUT = DD.SQL()

query1 = (f'''CREATE TABLE IF NOT EXISTS AIhub_drivers_monitoring_box_info(
            id INT PRIMARY KEY AUTO_INCREMENT,
            img_name VARCHAR(255) NOT NULL,
            img_dir VARCHAR(255) NOT NULL,
            img_format VARCHAR(10) NOT NULL,
            img_width INT NOT NULL,
            img_height INT NOT NULL,
            color_space VARCHAR(10) NOT NULL,
            label_name VARCHAR(255) NOT NULL,
            label_dir VARCHAR(255) NOT NULL,
            label_format VARCHAR(10) NOT NULL,
            attr_id VARCHAR(20) NOT NULL,
            label VARCHAR(20) NOT NULL,
            box_xtl INT,
            box_ytl INT,
            box_xbr INT,
            box_ybr INT);''')

query2 = (f'''CREATE TABLE IF NOT EXISTS AIhub_drivers_monitoring_attr_info(
            id INT PRIMARY KEY AUTO_INCREMENT,
            img_name VARCHAR(255) NOT NULL,
            img_dir VARCHAR(255) NOT NULL,
            img_format VARCHAR(10) NOT NULL,
            img_width INT NOT NULL,
            img_height INT NOT NULL,
            color_space VARCHAR(10) NOT NULL,
            label_name VARCHAR(255) NOT NULL,
            label_dir VARCHAR(255) NOT NULL,
            label_format VARCHAR(10) NOT NULL,
            attr_id VARCHAR(20) NOT NULL,
            attr_sex VARCHAR(10) NOT NULL,
            attr_age VARCHAR(20) NOT NULL,
            attr_act VARCHAR(50) NOT NULL,
            attr_emotion VARCHAR(50) NOT NULL);''')

query1_1 = (f'''INSERT INTO AIhub_drivers_monitoring_box_info 
        (img_name, img_dir, img_format, img_width, img_height, color_space,
        label_name, label_dir, label_format, 
        attr_id, label, box_xtl, box_ytl, box_xbr, box_ybr)
        VALUES (%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s );''')

query2_1 = (f'''INSERT INTO AIhub_drivers_monitoring_attr_info 
        (img_name, img_dir, img_format, img_width, img_height, 
        color_space, label_name, label_dir, label_format, attr_id, 
        attr_sex, attr_age, attr_act, attr_emotion) 
        VALUES (%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s );''')

try:
    doUT.create_table(query1)
except Exception as e:
    print(f"Error during table creation: {e}")

try:
    doUT.create_table(query2)
except Exception as e:
    print(f"Error during table creation: {e}")

value_list = []
error_list = []

label_path = 'Z:\\AIhub_drivers_monitoring\\data\\RGB\\labeldata'
img_path = 'Z:\\AIhub_drivers_monitoring\\data\\RGB\\rawdata'
label_lists = os.listdir(label_path)

for num, label_list in enumerate(label_lists):
    # print(num)
    label_files = os.listdir(os.path.join(label_path,label_list))
    total_cnt = len(label_lists)
    for cnt,label_file in enumerate(label_files):
        # print('start',label_file)
        label_dir = os.path.join(label_path,label_list,label_file)
        
        img_ = os.path.dirname(label_dir)
        label_name, label_format = os.path.splitext(os.path.basename(label_file))
        label_format = label_format.replace('.','')
        color_space = 'RGB'
        
        with open(label_dir,'r',encoding='utf-8') as f:
            data = json.load(f)
        scene_data = data['scene']['data']
        occupant_info = data['occupant_info']
        for i in range(len(scene_data)):
            img_file = scene_data[i]['img_name']
            
        
            img_dir = os.path.join(img_,img_file)
            img_dir = img_dir.replace('label','raw')
            
            img_name, img_format = os.path.splitext(img_file)
            img_format = img_format.replace('.','')
            if not os.path.isfile(img_dir) or os.path.getsize(img_dir) == 0:
                print(img_dir)
                error_list.append(img_dir)
                continue
            img = cv2.imread(img_dir)
            
            if img is None:
                print(img_dir)
                error_list.append(img_dir)
                continue
            img_width = img.shape[0]
            img_height = img.shape[1]
            occupant = scene_data[i]['occupant'][0]
            
            attr_id = occupant['occupant_id']
            
            for i in occupant.keys():
                if 'b_box' in i:

                    label = i.split('_')[0]
                    b_box = occupant[i]
                    box_xtl, box_ytl, box_width, box_height =  map(int,b_box)
                    box_xbr, box_ybr = box_xtl + box_width, box_ytl + box_height
                    img_dir = img_dir.replace('Z:','DataBase')
                    label_dir = label_dir.replace('Z:','DataBase')
                    values = (img_name, img_dir, img_format, img_width, img_height, color_space,
                            label_name, label_dir, label_format, 
                            attr_id, label, box_xtl, box_ytl, box_xbr, box_ybr)
                    value_list.append(values)
              
            
                if len(value_list) >= 500:
                    # print(value_list1[0])
                    print(f'box {num}/{total_cnt}')
                    doUT.insert_dataset_values(query1_1, value_list)
                    value_list = []

doUT.insert_dataset_values(query1_1, value_list)
# print(value_list2)
value_list = []
print('done')      

value_list1 = []
error_list = []

label_path = 'Z:\\AIhub_drivers_monitoring\\data\\RGB\\labeldata'
img_path = 'Z:\\AIhub_drivers_monitoring\\data\\RGB\\rawdata'
label_lists = os.listdir(label_path)

for num, label_list in enumerate(label_lists):
    # print(num)
    label_files = os.listdir(os.path.join(label_path,label_list))
    total_cnt = len(label_lists)
    for cnt,label_file in enumerate(label_files):
        # print('start',label_file)
        label_dir = os.path.join(label_path,label_list,label_file)
        
        img_ = os.path.dirname(label_dir)
        label_name, label_format = os.path.splitext(os.path.basename(label_file))
        label_format = label_format.replace('.','')
        color_space = 'RGB'
        
        with open(label_dir,'r',encoding='utf-8') as f:
            data = json.load(f)
        scene_data = data['scene']['data']
        occupant_info = data['occupant_info']
        for i in range(len(scene_data)):
            img_file = scene_data[i]['img_name']
            
        
            img_dir = os.path.join(img_,img_file)
            img_dir = img_dir.replace('label','raw')
            
            img_name, img_format = os.path.splitext(img_file)
            img_format = img_format.replace('.','')
            if not os.path.isfile(img_dir) or os.path.getsize(img_dir) == 0:
                print(img_dir)
                error_list.append(img_dir)
                continue
            img = cv2.imread(img_dir)
            
            if img is None:
                print(img_dir)
                error_list.append(img_dir)
                continue
            img_width = img.shape[0]
            img_height = img.shape[1]
            occupant = scene_data[i]['occupant'][0]
            
            attr_id = occupant['occupant_id']
            for occ in occupant_info:
                # print(occ)
                if occ['occupant_id'] == attr_id:
                    attr_sex = occ['occupant_sex']
                    attr_age = occ['occupant_age'].replace('대','')
            attr_act = occupant['action']
            attr_emotion = occupant['emotion']
            
            img_dir = img_dir.replace('Z:','DataBase')
            label_dir = label_dir.replace('Z:','DataBase')
            values1 = (img_name, img_dir, img_format,img_width, img_height, color_space, 
                       label_name, label_dir, label_format, attr_id, attr_sex, 
                       attr_age, attr_act, attr_emotion)
            value_list1.append(values1)


            if len(value_list1) >= 500:
                # print(value_list1[-1])
                print(f'attr {num}/{total_cnt}')
                doUT.insert_dataset_values(query2_1, value_list1)
                value_list1 = []

doUT.insert_dataset_values(query2_1, value_list1)
# print(value_list1[-1])
# value_list = []
print('done')
