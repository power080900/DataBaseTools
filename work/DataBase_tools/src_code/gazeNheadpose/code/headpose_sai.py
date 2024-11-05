import os
import pandas as pd
import json


df = pd.DataFrame(columns=['label','Gaze_x','Gaze_y', 'Head_yaw', 'Head_pitch', 'Head_roll'])

sai_root = 'Z:\\SAI\\data\\IR\\labeldata'

sai_id = os.listdir(sai_root)

for id_ in sai_id:
    print(id_)
    sai_file_path = os.path.join(sai_root, id_)
    sai_file = os.listdir(sai_file_path)
    for file in sai_file:
        with open(os.path.join(sai_file_path, file)) as f:
            data = json.load(f)
        
        
        gaze_x = data['facial_attributes']['gaze']['horizontal_angle']
        gaze_y = data['facial_attributes']['gaze']['vertical_angle']
        head_yaw = data['facial_attributes']['head_turn']['yaw']
        head_pitch = data['facial_attributes']['head_turn']['pitch']
        head_roll = data['facial_attributes']['head_turn']['roll']
        df.loc[len(df)] = [file, gaze_x, gaze_y, head_yaw, head_pitch, head_roll]

df.to_csv('headpose_sai.csv', index=False)