import os
import pandas as pd
import json
import numpy as np
from PIL import Image
import math

root_dir = 'Z:\\SAI\\data\\IR\\labeldata'
image = 'Z:\\SAI\\data\\IR\\rawdata\\id_00\\id_00_case01_0.cam_rearview.f_1.rgb.png'
ids = os.listdir(root_dir)

image = Image.open(image)
dpi = image.info.get('dpi',96)

df1 = pd.DataFrame(columns=['label','eye_side','iris_size','dpi'])

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
        eye_side = 'left'
        left_eye_points = data[36:42]
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

        
        
    df1.to_csv(f'iris_sai_{id_}.csv', index=False)
    df1 = pd.DataFrame(columns=['label','eye_side','iris_size','dpi'])

# file_pattern = "iris_sai_id_{:02d}.csv"

# # 빈 리스트를 만들어서 데이터를 저장할 준비
# dataframes = []

# # 0부터 34까지의 파일을 읽어들여 리스트에 추가
# for i in range(35):
#     file_name = file_pattern.format(i)
#     df = pd.read_csv(file_name)
#     dataframes.append(df)

# # 모든 데이터를 하나의 데이터프레임으로 결합
# combined_df = pd.concat(dataframes, ignore_index=True)

# # 결합된 데이터를 새로운 CSV 파일로 저장
# combined_df.to_csv("combined_iris_sai.csv", index=False)