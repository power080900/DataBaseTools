import os
import sys
from glob import glob
import json
import cv2
import matplotlib.pyplot as plt
sys.path.append('../')
import EDA_utils as EU

root = 'Z:\\GazeCapture\\data\\RGB\\'
save_root = 'Z:\\GazeCapture\\data\\RGB\\checkdata\\'
label_root = 'Z:\\GazeCapture\\data\\RGB\\labeldata\\*'
# img_root = 'Z:\\GazeCapture\\data\\RGB\\rawdata\\*'
# img_id = glob(img_root)

# n = 0
# for img in img_id:
#     img_files = glob(img+'\\*')
#     print(os.path.basename(img),len(img_files))
#     n += len(img_files)

# print(n)


label_id = glob(label_root)

for label in label_id[0:1]:
    label_files = glob(label+'\\*')
    

    with open(label_files[0],'r') as f:
        face_label = json.load(f)
    with open(label_files[1],'r') as f:
        left_eye_label = json.load(f)
    with open(label_files[2],'r') as f:
        right_eye_label = json.load(f)
    with open(label_files[3],'r') as f:
        dot_label = json.load(f)
    with open(label_files[4],'r') as f:
        face_grid_label = json.load(f)
    with open(label_files[5],'r') as f:
        frame_label = json.load(f)
    with open(label_files[6],'r') as f:
        info_label = json.load(f)
    with open(label_files[7],'r') as f:
        motion_label = json.load(f)
    with open(label_files[8],'r') as f:
        screen_label = json.load(f)
    
    print(info_label.keys())
    print(screen_label.keys())

    for motion in motion_label[:1]:
        print(len(motion_label))
        print(motion)


    for i in range(len(face_label['X'])):
        img_path = os.path.join(os.path.dirname(label_files[0]).replace('labeldata','rawdata')+f'\\{i:05d}.jpg')
        print(label_files[0])
        print(label_files[1])
        print(label_files[2])
        print(label_files[3])
        print(img_path)

        face_isvalid = int(float(face_label['IsValid'][i]))
        if face_isvalid == 1:    
            face_x = int(float(face_label['X'][i]))
            face_y = int(float(face_label['Y'][i]))
            face_w = int(float(face_label['W'][i]))
            face_h = int(float(face_label['H'][i]))
        elif face_isvalid == 0:
            face_x = 0
            face_y = 0
            face_w = 0
            face_h = 0
        
        left_eye_isvalid = int(float(left_eye_label['IsValid'][i]))
        if left_eye_isvalid == 1:
            left_eye_x = face_x + int(float(left_eye_label['X'][i]))
            left_eye_y = face_y + int(float(left_eye_label['Y'][i]))
            left_eye_w = int(float(left_eye_label['W'][i]))
            left_eye_h = int(float(left_eye_label['H'][i]))
        elif left_eye_isvalid == 0:
            left_eye_x = 0
            left_eye_y = 0
            left_eye_w = 0
            left_eye_h = 0
        
        right_eye_isvalid = int(float(right_eye_label['IsValid'][i]))
        if right_eye_isvalid == 1:
            right_eye_x = face_x + int(float(right_eye_label['X'][i]))
            right_eye_y = face_y + int(float(right_eye_label['Y'][i]))
            right_eye_w = int(float(right_eye_label['W'][i]))
            right_eye_h = int(float(right_eye_label['H'][i]))
        elif right_eye_isvalid == 0:
            right_eye_x = 0
            right_eye_y = 0
            right_eye_w = 0
            right_eye_h = 0

        face_grid_x = int(float(face_grid_label['X'][i]))
        face_grid_y = int(float(face_grid_label['Y'][i]))
        face_grid_w = int(float(face_grid_label['W'][i]))
        face_grid_h = int(float(face_grid_label['H'][i]))

        # scale_x = face_grid_w / 

        screen_orientation = int(float(screen_label['Orientation'][i]))
        screen_h = int(float(screen_label['H'][i]))
        screen_w = int(float(screen_label['W'][i]))

        dot_xpts = int(float(dot_label['XPts'][i]))
        dot_ypts = int(float(dot_label['YPts'][i]))
        if screen_orientation == 1:
            print('cam1')
            dot_xcam = int(float(dot_label['XCam'][i]))
            dot_ycam = int(float(dot_label['YCam'][i]))
        elif screen_orientation == 2:
            print('cam2')
            dot_xcam = int(float(dot_label['XCam'][i]))
            dot_ycam = -int(float(dot_label['YCam'][i]))
        elif screen_orientation == 3:
            print('cam3')
            dot_xcam = -int(float(dot_label['YCam'][i]))
            dot_ycam = int(float(dot_label['XCam'][i]))
        elif screen_orientation == 4:
            print('cam4')
            dot_xcam = int(float(dot_label['YCam'][i]))
            dot_ycam = int(float(dot_label['XCam'][i]))

        
                 
        img = cv2.imread(img_path)
        print('face box:', face_x,face_y,face_w,face_h)
        print('left eye box:', left_eye_x,left_eye_y,left_eye_w,left_eye_h)
        print('right eye box:', right_eye_x,right_eye_y,right_eye_w,right_eye_h)
        print('dot_pts:', dot_xpts,dot_ypts)
        print('dot_predict:', dot_xcam,dot_ycam)
        print('face grid:', face_grid_x,face_grid_y,face_grid_w,face_grid_h)
        img = cv2.rectangle(img,(face_x,face_y),(face_x+face_w,face_y+face_h),(0,0,255),2) #red
        img = cv2.rectangle(img,(left_eye_x,left_eye_y),(left_eye_x+left_eye_w,left_eye_y+left_eye_h),(0,0,255),2) #red
        img = cv2.rectangle(img,(right_eye_x,right_eye_y),(right_eye_x+right_eye_w,right_eye_y+right_eye_h),(0,0,255),2) #red
    #     # img = cv2.rectangle(img,(face_grid_x,face_grid_y),(face_grid_x+face_grid_w,face_grid_y+face_grid_h),(0,255,255),2) #yellow
        img = cv2.circle(img,(dot_xpts,dot_ypts),10,(255,0,0),-1) #blue
    #     # img = cv2.circle(img,((dot_xcam+25)*10,(dot_ycam+25)*10),10,(0,255,0),-1) #green
        cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        