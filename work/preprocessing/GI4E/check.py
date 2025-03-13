import os
from glob import glob
import matplotlib.pyplot as plt
import cv2

txt_list = glob('Z:\\GI4E\\labels\\*.txt')

for txt in txt_list[:1]:
    # print(txt)
    with open(txt, 'r') as f:
        config = f.readlines()
    
    for i in config:
        file_name, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6 = i.split('\t')
        file_dir = os.path.join(os.path.dirname(txt.replace('labels','images')), file_name)
        # print(file_dir)
        
        x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6 = float(x1), float(y1), float(x2), float(y2), float(x3), float(y3), float(x4), float(y4), float(x5), float(y5), float(x6), float(y6)


        img = cv2.imread(file_dir)
        img = cv2.circle(img, (int(x1), int(y1)), 3, (0, 0, 255), -1)
        img = cv2.circle(img, (int(x2), int(y2)), 3, (0, 0, 255), -1)
        img = cv2.circle(img, (int(x3), int(y3)), 3, (0, 0, 255), -1)
        img = cv2.circle(img, (int(x4), int(y4)), 3, (0, 0, 255), -1)
        img = cv2.circle(img, (int(x5), int(y5)), 3, (0, 0, 255), -1)
        img = cv2.circle(img, (int(x6), int(y6)), 3, (0, 0, 255), -1)
        
        cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        