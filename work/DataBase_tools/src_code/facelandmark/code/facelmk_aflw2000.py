import os
import pandas as pd
import scipy.io
import numpy as np


df = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])
df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

aflw2000_root = 'Z:\\AFLW2000\\data\\RGB\\labeldata'

aflw2000_id = os.listdir(aflw2000_root)

for id_ in aflw2000_id:
    print(id_)
    aflw2000_path = os.path.join(aflw2000_root, id_)
    aflw2000_file = os.listdir(aflw2000_path)
    for num, file in enumerate(aflw2000_file):
        print(num,'/',len(aflw2000_file))
        data = scipy.io.loadmat(os.path.join(aflw2000_path, file))
        Facelmk_pts = len(data['pt3d_68'][0])
        posepara = np.array(data['Pose_Para'][0])
        head_yaw = np.rad2deg(posepara[0])
        head_pitch = np.rad2deg(posepara[1])
        head_roll = np.rad2deg(posepara[2])
        
        df1.loc[len(df1)] = [file, Facelmk_pts, head_yaw, head_pitch, head_roll]
        df = pd.concat([df, df1])

        df.to_csv('FaceLandmark_aflw2000.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

    df.to_csv('FaceLandmark_aflw2000.csv', index=False)