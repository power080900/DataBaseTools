import os
import json
from glob import glob
import cv2

json_list = glob(os.path.join(os.getcwd(),'select_data','*','*', '*.json'))

for json_file in json_list:
    with open(json_file, 'r',encoding='utf-8-sig') as f:
        json_data = json.load(f)

    img_name = json_data['image']['filename']
    annotations = json_data['annotations']
    # print(json_data)
    for annotation in annotations:
        class_name = annotation['class']

        if class_name == '04':
            if annotation['polygon']:
                polygon = annotation['polygon']
                max_x = max([x for x,y in polygon])
                max_y = max([y for x,y in polygon])
                min_x = min([x for x,y in polygon])
                min_y = min([y for x,y in polygon])

            elif annotation['box']:
                max_x, max_y, min_x, min_y = annotation['box']

            img_dir = json_file.replace('label','image').replace('json','jpg')
            img = cv2.imread(img_dir)
            cv2.rectangle(img, (min_x,min_y), (max_x,max_y), (0,0,255), 2)
            cv2.imshow('img',img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


    

            
            