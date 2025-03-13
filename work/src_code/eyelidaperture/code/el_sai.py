import os
import pandas as pd
import json
import numpy as np
from PIL import Image

root_dir = 'Z:\\SAI\\data\\IR\\labeldata'
image = 'Z:\\SAI\\data\\IR\\rawdata\\id_00\\id_00_case01_0.cam_rearview.f_1.rgb.png'

image = Image.open(image)
dpi = image.info.get('dpi')

df = pd.DataFrame(columns=['label','Facelandmark_pts', 'eye_side','eyelid', 'dpi'])
df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'eye_side','eyelid', 'dpi'])

def get_eyelid(data):
    left_eye_upper_indices = list(range(36, 42))
    left_eye_lower_indices = list(range(42, 48))

    right_eye_upper_indices = list(range(17, 23))
    right_eye_lower_indices = list(range(23, 29))  
    left_upper_midpoint = np.mean(data[left_eye_upper_indices], axis=0)
    left_lower_midpoint = np.mean(data[left_eye_lower_indices], axis=0)
    right_upper_midpoint = np.mean(data[right_eye_upper_indices], axis=0)
    right_lower_midpoint = np.mean(data[right_eye_lower_indices], axis=0)
    left_eyelid_aperture = np.linalg.norm(left_upper_midpoint - left_lower_midpoint)
    right_eyelid_aperture = np.linalg.norm(right_upper_midpoint - right_lower_midpoint)

    return left_eyelid_aperture, right_eyelid_aperture


ids = os.listdir(root_dir)

for id_ in ids:
    print(id_)
    id_path = os.path.join(root_dir, id_)
    files = os.listdir(id_path)
    for num, file in enumerate(files):
        print(num,'/',len(files))
        data = []
        with open(os.path.join(id_path, file)) as f:
            data = json.load(f)
        
        Facelmk_pts = len(data['landmarks']['ibug68'])
        face_landmarks = data['landmarks']['ibug68']

        landmark = []
        for i in range(0, len(face_landmarks)):
            
            face_landmark_x , face_landmark_y = face_landmarks[i]['screen_space_pos']
            face_landmark_x = face_landmark_x * 1280
            face_landmark_y = face_landmark_y * 720
            landmark.append((face_landmark_x, face_landmark_y))
        
        data = np.array(landmark)
        eyelids = get_eyelid(data)
        for eyelid in eyelids:
            eyeside = 'left' if eyelid == eyelids[0] else 'right'        
            df1.loc[len(df1)] = [file, Facelmk_pts, eyeside, eyelid, dpi]
        df = pd.concat([df, df1])
        
        df.to_csv('el_sai.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'eye_side','eyelid', 'dpi'])

df.to_csv('el_sai.csv', index=False)