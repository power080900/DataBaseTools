import os
import pandas as pd
import numpy as np

root_dir = 'Z:\\frgc\\data\\RGB\\labeldata' 

dpi = '96'

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
            for line in f:
                try:
                    x, y = map(float, line.split())
                    data.append((x, y))
                except ValueError:
                    continue
        data = np.array(data)
        Facelmk_pts = len(data)
        # print(data)
        eyelids = get_eyelid(data)
        for eyelid in eyelids:
            eyeside = 'left' if eyelid == eyelids[0] else 'right'        
            df1.loc[len(df1)] = [file, Facelmk_pts, eyeside, eyelid, dpi]
        df = pd.concat([df, df1])

        df.to_csv('el_frgc.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'eye_side','eyelid', 'dpi'])

df.to_csv('el_frgc.csv', index=False)