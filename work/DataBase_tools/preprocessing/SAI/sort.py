import os
import pandas as pd
import numpy as np
import cv2
import json

id_list = os.listdir('Z:\\SAI\\data\\IR\\labeldata\\')


for id_ in id_list:
    print(id_)
    results = []
    img_dir = f'Z:\\SAI\\data\\IR\\rawdata\\{id_}'
    label_dir = f'Z:\\SAI\\data\\IR\\labeldata\\{id_}'
    for label_file in os.listdir(label_dir):
        
        label = os.path.join(label_dir,label_file)
        img_file = label_file.replace('.info.json','.rgb.png')
        img_path = os.path.join(img_dir,img_file)
        image = cv2.imread(img_path)

        with open(label,  'r', encoding='utf-8') as f:
            data = json.load(f)
        
        lens_color = data["accessories"]["glasses"]["lens_color"]
        transparency = data["accessories"]["glasses"]["transparency"]
        metalness = data["accessories"]["glasses"]["metalness"]
        gesture = data["gesture"]['name']
        roll = data['facial_attributes']['head_turn']['roll']
        pitch = data['facial_attributes']['head_turn']['pitch']
        yaw = data['facial_attributes']['head_turn']['yaw']
        case = label_file.split('_')[2]
        
        # print(segments_mapping)

        ca_wi = {}

        ca_wi['id'] = id_
        ca_wi['label_file'] = label  # Add label file name to results
        ca_wi['case'] = case
        ca_wi['img_path'] = img_path  # Add image path to results
        ca_wi['lens_color'] = lens_color
        ca_wi['transparency'] = transparency
        ca_wi['metalness'] = metalness
        ca_wi['roll'] = roll
        ca_wi['pitch'] = pitch
        ca_wi['yaw'] = yaw
        ca_wi['gesture'] = gesture

        results.append(ca_wi)
        
    df = pd.DataFrame(results, columns=['id','case','label_file','img_path','lens_color','transparency','metalness','roll','pitch','yaw','gesture'])
    df.to_csv(f'summary_{id_}.csv',index=False)
