import os
import pandas as pd
import scipy.io
import numpy as np

root_dir = 'Z:\\DIS_300W_3D\\data\\RGB\\labeldata'

dpi = '96'

df = pd.DataFrame(columns=['label','Facelandmark_pts', 'eye_side','eyelid', 'dpi'])
df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'eye_side','eyelid', 'dpi'])

ids = os.listdir(root_dir)

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
        x = data['pt2d'][0]
        y = data['pt2d'][1]
        data = np.array(list(zip(x, y)))
        eyelids = get_eyelid(data)
        for eyelid in eyelids:
            eyeside = 'left' if eyelid == eyelids[0] else 'right'
            df1.loc[len(df1)] = [file, Facelmk_pts, eyeside, eyelid, dpi]
        df = pd.concat([df, df1])

        df.to_csv('el_300w_3d.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Facelandmark_pts', 'eye_side','eyelid', 'dpi'])

df.to_csv('el_300w_3d.csv', index=False)