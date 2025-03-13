import os
import pandas as pd

df = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])
df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

root_dir = 'Z:\\xm2vts\\data\\RGB\\labeldata'    

ids = os.listdir(root_dir)

for id_ in ids:
    print(id_)
    id_path = os.path.join(root_dir, id_)
    files = os.listdir(id_path)
    for num, file in enumerate(files):
        print(num,'/',len(files))
        with open(os.path.join(id_path, file)) as f:
            data = f.readlines()
        Facelmk_pts = len(data)
        head_yaw = 'None'
        head_pitch = 'None'
        head_roll = 'None'
        
        df1.loc[len(df1)] = [file, Facelmk_pts, head_yaw, head_pitch, head_roll]
        df = pd.concat([df, df1])

        df.to_csv('FaceLandmark_xm2vts.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

df.to_csv('FaceLandmark_xm2vts.csv', index=False)