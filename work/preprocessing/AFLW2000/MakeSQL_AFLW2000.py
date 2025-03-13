import sys
import os
import cv2
from scipy import io
sys.path.append('../../src')
import DISData as DD

doUT = DD.SQL()

query1 = (f'''CREATE TABLE IF NOT EXISTS AFLW2000_landmark_info (
        id INT(11) NOT NULL AUTO_INCREMENT primary key,
        img_dir VARCHAR(100) NOT NULL,
        img_format VARCHAR(10) NOT NULL,
        img_width INT(11) NOT NULL,
        img_height INT(11) NOT NULL,
        color_space VARCHAR(10) NOT NULL,
        label_dir VARCHAR(100) NOT NULL,
        label_format VARCHAR(10) NOT NULL,
        label VARCHAR(20) NOT NULL,
        landmark VARCHAR(2000) NOT NULL)''')

query2 = (f'''INSERT INTO AFLW2000_landmark_info 
        (img_dir, img_format, img_width, img_height, color_space,
          label_dir, label_format, label, landmark) VALUES 
          (%s, %s, %s, %s, %s,  %s, %s, %s, %s)''')

try:
    doUT.create_table(query1)
except Exception as e:
    print(f"Error during table creation: {e}")

    # label 경로
label_path = 'Z:\\AFLW2000\\data\\RGB\\labeldata'
image_path = 'Z:\\AFLW2000\\data\\RGB\\rawdata'

value_list1 = []
error_list = []
count = 0

label_ids = os.listdir(label_path)
for label_id in label_ids:
    label_files = os.listdir(os.path.join(label_path,label_id))
    for label_file in label_files:
        # try:
        label = os.path.join(label_path,label_id,label_file)
        text = io.loadmat(label)
        # print(text)
        img_dir = label.replace('labeldata','rawdata').replace('.mat','.jpg')
        # print(img_dir)
        img_format = 'jpg'
        image = cv2.imread(img_dir)
        img_width = image.shape[1]
        img_height = image.shape[0]
        color_check = img_dir.split('\\')[-2]

        color_space = 'RGB'
        label_dir = label
        label_format = 'mat'
        label1 = 'face_21'
        label2 = 'face_3d_68'

        pt2d_x = text['pt2d'][0]
        pt2d_y = text['pt2d'][1]
        pt3d_x = text['pt3d_68'][0]
        pt3d_y = text['pt3d_68'][1]
        pt3d_z = text['pt3d_68'][2]

        point = []
        point_3d = []
        for pt in range(len(pt2d_x)):
            point.append((int(float(pt2d_x[pt])),int(float(pt2d_y[pt]))))
            point_3d.append((int(float(pt3d_x[pt])),int(float(pt3d_y[pt])),int(float(pt3d_z[pt]))))

        landmark1 = ','.join(map(str, [ (x,y) for x,y in point]))
        landmark2 = ','.join(map(str, [ (x,y,z) for x,y,z in point_3d]))

        img_dir = img_dir.replace('Z:', 'DataBase').replace('\\','/')
        label_dir = label_dir.replace('Z:', 'DataBase').replace('\\','/')

        value1 = (img_dir, img_format, img_width, img_height, color_space, label_dir, label_format, label1, landmark1)
        value_list1.append(value1)
        value2 = (img_dir, img_format, img_width, img_height, color_space, label_dir, label_format, label2, landmark2)
        value_list1.append(value2)


        # except Exception as ex:
        #     error_list.append((label, str(ex)))
        #     print(f"Error loading data from file: {label}")
        #     print(f"Error details: {ex}")

        # query 실행
        if len(value_list1) >= 500:
            print(value_list1[0])
            doUT.insert_dataset_values(query2, value_list1)
            value_list1 = []

doUT.insert_dataset_values(query2, value_list1)
# print(value_list2)
value_list1 = []
print('done')