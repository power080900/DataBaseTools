import os
import pandas as pd
import json


df = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])
df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

sai_root = 'Z:\\SAI\\data\\IR\\labeldata'

sai_id = os.listdir(sai_root)

for id_ in sai_id:
    print(id_)
    sai_file_path = os.path.join(sai_root, id_)
    sai_file = os.listdir(sai_file_path)
    for num, file in enumerate(sai_file):
        print(num,'/',len(sai_file))
        with open(os.path.join(sai_file_path, file)) as f:
            data = json.load(f)
        
        Facelmk_pts = len(data['landmarks']['ibug68'])
        head_yaw = data['facial_attributes']['head_turn']['yaw']
        head_pitch = data['facial_attributes']['head_turn']['pitch']
        head_roll = data['facial_attributes']['head_turn']['roll']
        df1.loc[len(df1)] = [file, Facelmk_pts, head_yaw, head_pitch, head_roll]
        df = pd.concat([df, df1])
        
        df.to_csv('FaceLandmark_sai.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])


df.to_csv('FaceLandmark_sai.csv', index=False)