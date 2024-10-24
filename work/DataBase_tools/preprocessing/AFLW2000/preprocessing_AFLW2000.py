import os
import sys
sys.path.append('../../src')
from scipy import io
import cv2

label_path = 'Z:\AFLW2000\data\RGB\Labels'
label_ids = os.listdir(label_path)

for label_id in label_ids[:1]:
    label_files = os.listdir(os.path.join(label_path,label_id))
    for label_file in label_files[:1]:
        label = os.path.join(label_path,label_id,label_file)
        text = io.loadmat(label)
        # print(text)
        image = label.replace('labeldata','imagedata').replace('.mat','.jpg')
        # print(image)
        keys = text.keys()
        # for i in keys:
        #     # print(i)
        #     # print(text[i])
        #     # print(len(text[i]))
        #     if i not in ['__header__','__version__','__globals__']:
        #         print(i)
        #         print(text[i])
        #         print(len(text[i]))
        
        img1 = cv2.imread(image)
        img2 = cv2.imread(image)
        
        pt2d_x = text['pt2d'][0]
        pt2d_y = text['pt2d'][1]
        
        pt3d_x = text['pt3d_68'][0]
        pt3d_y = text['pt3d_68'][1]
        
        # print(pt2d_x)
        for pt in range(len(pt2d_x)):
            x = int(float(pt2d_x[pt]))
            y = int(float(pt2d_y[pt]))
            cv2.circle(img1,(x,y),5,(0,255,0),-1)
        # cv2.imshow('image',img1)
        # cv2.waitKey()
        # cv2.destroyAllWindows()
        
        for pt in range(len(pt3d_x)):
            x = int(float(pt3d_x[pt]))
            y = int(float(pt3d_y[pt]))
            cv2.circle(img2,(x,y),5,(0,255,0),-1)
        cv2.imshow('image',img2)
        cv2.waitKey()
        cv2.destroyAllWindows()