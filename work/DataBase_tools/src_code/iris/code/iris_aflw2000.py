import os
import pandas as pd
import math
from PIL import Image
import scipy.io
import numpy as np

root_dir = 'Z:\\AFLW2000\\data\\RGB\\labeldata'

dpi = '96'

df = pd.DataFrame(columns=['label','eye_side','iris_size','dpi'])
df1 = pd.DataFrame(columns=['label','eye_side','iris_size','dpi'])

ids = os.listdir(root_dir)

for id_ in ids:
    print(id_,'/',len(ids))
    id_path = os.path.join(root_dir, id_)
    files = os.listdir(id_path)
    for num, file in enumerate(files):
        print(num,'/',len(files))
        data = scipy.io.loadmat(os.path.join(id_path, file))
        
        x = data['pt3d_68'][0]
        y = data['pt3d_68'][1]
        data = np.array(list(zip(x, y)))
        
        eye_side = 'left'
        left_eye_points = data[36:42]
        # print(left_eye_points)
        center_x = sum([float(point[0]) for point in left_eye_points]) / len(left_eye_points)
        center_y = sum([float(point[1]) for point in left_eye_points]) / len(left_eye_points)
        eye_center = (center_x, center_y)
        # print(eye_center)
        distances = [math.sqrt((float(point[0]) - eye_center[0]) ** 2 + (float(point[1]) - eye_center[1]) ** 2) for point in left_eye_points]
        radius = max(distances)
        iris_size = math.pi * (radius ** 2)
        df1.loc[len(df1)] = [file, eye_side, iris_size, dpi]

        eye_side = 'right'
        right_eye_points = data[42:48]
        center_x = sum([float(point[0]) for point in right_eye_points]) / len(right_eye_points)
        center_y = sum([float(point[1]) for point in right_eye_points]) / len(right_eye_points)
        eye_center = (center_x, center_y)
        distances = [math.sqrt((float(point[0]) - eye_center[0]) ** 2 + (float(point[1]) - eye_center[1]) ** 2) for point in right_eye_points]
        radius = max(distances)
        iris_size = math.pi * (radius ** 2)
        df1.loc[len(df1)] = [file, eye_side, iris_size, dpi]

        df = pd.concat([df, df1])
        df.to_csv('iris_aflw2000.csv', index=False)
        df1 = pd.DataFrame(columns=['label','eye_side','iris_size','dpi'])

