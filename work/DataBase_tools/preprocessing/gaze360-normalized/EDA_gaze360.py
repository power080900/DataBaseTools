import os
from glob import glob
import cv2
import numpy as np

img_folder = os.path.join(os.getcwd(), 'data', 'RGB', 'rawdata','Face')
label_folder = os.path.join(os.getcwd(), 'data', 'RGB', 'labeldata','Face')
save_folder = 'C:\\lee\\work\\gazedimgdata'

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

label_list = glob(os.path.join(label_folder, '*.label'))

for label in label_list:
    
    with open(label, 'r') as f:
        lines = f.readlines()
    for line in lines[1:]:
        
        face, left, right, origin, point_3ds, point_2ds = line.split(' ')
        save_name = '_'.join([label.split('\\')[-1].split('.')[0],face.split('/')[-1]])
        face = face.split('/')[-1]
        
        x_3d, y_3d, z_3d = map(float, point_3ds.split(','))
        x_2d, y_2d = map(float, point_2ds.split(','))

        x_rad = -x_2d
        y_rad = y_2d

        x_deg = np.rad2deg(x_rad)
        y_deg = np.rad2deg(y_rad)

        img_file = os.path.join(img_folder, face)
        img = cv2.imread(img_file)

        height, width = img.shape[:2]

        center_x = width // 2
        center_y = height // 2
 
        arrow_length = 80

        end_x3 = int(center_x + arrow_length * np.sin(x_rad)* np.cos(y_rad))
        end_y3 = int(center_y - arrow_length * np.sin(y_rad))
        end_x2 = int(center_x + arrow_length * np.sin(x_rad))
        end_y2 = int(center_y - arrow_length * np.sin(y_rad))

        cv2.arrowedLine(img, (center_x, center_y), (end_x3, end_y3), (0, 0, 255), 2)
        cv2.arrowedLine(img, (center_x, center_y), (end_x2, end_y2), (0, 255, 0), 2)

        save_file = os.path.join(save_folder, save_name) 
        # print(save_file)
        cv2.imwrite(save_file, img)
