import os
import pandas as pd
import scipy.io
import numpy as np


df = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])
df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

root_dir = 'Z:\\DIS_300W_3D\\data\\RGB\\labeldata'    

ids = os.listdir(root_dir)

for id_ in ids:
    print(id_,'/',len(ids))
    id_path = os.path.join(root_dir, id_)
    files = os.listdir(id_path)
    for num, file in enumerate(files):
        print(num,'/',len(files))
        data = scipy.io.loadmat(os.path.join(id_path, file))
        # print(data.keys())
        Facelmk_pts = len(data['pt2d'][0])
        # print(Facelmk_pts)
        posepara = np.array(data['Pose_Para'][0])
        head_yaw = np.rad2deg(posepara[0])
        head_pitch = np.rad2deg(posepara[1])
        head_roll = np.rad2deg(posepara[2])
        
        df1.loc[len(df1)] = [file, Facelmk_pts, head_yaw, head_pitch, head_roll]
        df = pd.concat([df, df1])

        df.to_csv('FaceLandmark_300w_3d.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

df.to_csv('FaceLandmark_300w_3d.csv', index=False)