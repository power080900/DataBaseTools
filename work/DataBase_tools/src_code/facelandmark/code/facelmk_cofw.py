import os
import pandas as pd

df = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])
df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

cofw_root = 'Z:\\COFW\\data\\RGB\\labeldata'    

cofw_id = os.listdir(cofw_root)

for id_ in cofw_id:
    print(id_)
    cofw_path = os.path.join(cofw_root, id_)
    cofw_file = os.listdir(cofw_path)
    for num, file in enumerate(cofw_file):
        print(num,'/',len(cofw_file))
        with open(os.path.join(cofw_path, file)) as f:
            data = f.readlines()
        Facelmk_pts = len(data)
        head_yaw = 'None'
        head_pitch = 'None'
        head_roll = 'None'
        
        df1.loc[len(df1)] = [file, Facelmk_pts, head_yaw, head_pitch, head_roll]
        df = pd.concat([df, df1])

        df.to_csv('FaceLandmark_cofw.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'Head_yaw', 'Head_pitch', 'Head_roll'])

df.to_csv('FaceLandmark_cofw.csv', index=False)