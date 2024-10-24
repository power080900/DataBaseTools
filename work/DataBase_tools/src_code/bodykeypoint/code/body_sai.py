import os
import pandas as pd
import json
import numpy as np

sai = 'Z:\\sai\\data\\IR\\labeldata'
sai_ids = os.listdir(sai)

df = pd.DataFrame(columns=['label', 'gesture', 'angle'])

for num, id_ in enumerate(sai_ids):
    print(num, '/', len(sai_ids))
    sai_path = os.path.join(sai, id_)
    sai_files = os.listdir(sai_path)
    for cnt, file in enumerate(sai_files):
        print(cnt, '/', len(sai_files))
        file_path = os.path.join(sai_path, file)
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
        gesture = data['gesture']['name']
        whole_body = data['landmarks']["coco"]["whole_body"]
        point_6 = None
        point_7 = None
        point_12 = None
        point_13 = None

        for item in whole_body:
            if item["name"] == "6":
                point_6 = item["world_space_pos"]
            elif item["name"] == "7":
                point_7 = item["world_space_pos"]
            elif item["name"] == "12":
                point_12 = item["world_space_pos"]
            elif item["name"] == "13":
                point_13 = item["world_space_pos"]

        # 벡터 계산
        vector_u = np.array(point_7) - np.array(point_6)
        vector_v = np.array(point_13) - np.array(point_12)

        # 내적 계산
        dot_product = np.dot(vector_u, vector_v)

        # 벡터 크기 계산
        magnitude_u = np.linalg.norm(vector_u)
        magnitude_v = np.linalg.norm(vector_v)

        # 각도 계산
        cos_theta = dot_product / (magnitude_u * magnitude_v)
        theta = np.arccos(cos_theta)

        # 라디안에서 각도로 변환
        angle_degrees = np.degrees(theta)

        df.loc[len(df)] = [file, gesture, angle_degrees]


    # 중간 저장
    df.to_csv(f'bodykey_sai_{id_}.csv', index=False)
    df = pd.DataFrame(columns=['label', 'gesture', 'angle'])
    
df_combine = pd.DataFrame(columns=['label', 'gesture', 'angle'])

for i in range(35):
    file_name = f'bodykey_sai_id_{i:02d}.csv'
    df = pd.read_csv(file_name)
    df_combine = pd.concat([df_combine, df])

df_combine.to_csv('bodykey_sai.csv')

# for i in range(35):
#     file_name = f'bodykey_sai_id_{i:02d}.csv'
#     os.remove(file_name)