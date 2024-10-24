import os
import pandas as pd
import math
from PIL import Image

root_dir = 'Z:\\MultiPIE\\data\\RGB\\labeldata'
ids = os.listdir(root_dir)   

dpi = '120'

df = pd.DataFrame(columns=['label','eye_side','iris_size','dpi'])
df1 = pd.DataFrame(columns=['label','eye_side','iris_size','dpi'])

for id_ in ids:
    print(id_)
    id_path = os.path.join(root_dir, id_)
    files = os.listdir(id_path)
    for num, file in enumerate(files):
        print(num,'/',len(files))
        with open(os.path.join(id_path, file)) as f:
            data = f.readlines()
        
        eye_side = 'left'
        left_eye_points = data[36:42]
        left_eye_points = [point.split(' ') for point in left_eye_points]
        center_x = sum([float(point[0].replace('\n','')) for point in left_eye_points]) / len(left_eye_points)
        center_y = sum([float(point[1].replace('\n','')) for point in left_eye_points]) / len(left_eye_points)
        eye_center = (center_x, center_y)
        # print(eye_center)
        distances = [math.sqrt((float(point[0].replace('\n','')) - eye_center[0]) ** 2 + (float(point[1].replace('\n','')) - eye_center[1]) ** 2) for point in left_eye_points]
        radius = max(distances)
        iris_size = math.pi * (radius ** 2)
        df1.loc[len(df1)] = [file, eye_side, iris_size, dpi]

        eye_side = 'right'
        right_eye_points = data[42:48]
        right_eye_points = [point.split(' ') for point in right_eye_points]
        center_x = sum([float(point[0].replace('\n','')) for point in right_eye_points]) / len(right_eye_points)
        center_y = sum([float(point[1].replace('\n','')) for point in right_eye_points]) / len(right_eye_points)
        eye_center = (center_x, center_y)
        distances = [math.sqrt((float(point[0].replace('\n','')) - eye_center[0]) ** 2 + (float(point[1].replace('\n','')) - eye_center[1]) ** 2) for point in right_eye_points]
        radius = max(distances)
        iris_size = math.pi * (radius ** 2)
        df1.loc[len(df1)] = [file, eye_side, iris_size, dpi]

    df = pd.concat([df, df1])
    df.to_csv('iris_MultiPIE.csv', index=False)
    df1 = pd.DataFrame(columns=['label','eye_side','iris_size','dpi'])
