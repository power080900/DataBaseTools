import os
import pandas as pd
import json

sai = 'Z:\\sai\\data\\IR\\labeldata'
sai_ids = os.listdir(sai)

data_list = []

for num, id_ in enumerate(sai_ids):
    print(num, '/', len(sai_ids))
    sai_path = os.path.join(sai, id_)
    sai_files = os.listdir(sai_path)
    for cnt, file in enumerate(sai_files):
        print(cnt, '/', len(sai_files))
        file_path = os.path.join(sai_path, file)
        with open(file_path, 'r', encoding='UTF-8') as f:
            data = json.load(f)
            age = data['identity_metadata']['age']
            gender = 'M' if data.get('identity_metadata', {}).get('sex') == 'male' else 'F'
            ethnicity_list = data.get('identity_metadata', {}).get('ethnicity', []).split(',')
            height = data['identity_metadata']['height_cm']
            weight = data['identity_metadata']['weight_kg']
            skin_type = data['identity_metadata']['skin_tone']
            glasses = 'N'
            if data.get('accessories', {}).get('glasses', {}).get('style') is not None:
                lens_color = data.get('accessories', {}).get('glasses', {}).get('lens_color')
                if lens_color == 'default':
                    glasses = 'Y'
                elif lens_color == 'black':
                    glasses = 'sunglasses'

            cap = 'N' if data.get('accessories', {}).get('headwear', {}).get('style') == "none" else 'Y'
            mask = 'N' if not data.get('accessories', {}).get('mask', {}).get('style') else 'Y'

            for ethnicity in ethnicity_list:
                data_list.append([file, age, gender,height,weight, ethnicity,skin_type, glasses, cap, mask])

    # 중간 저장
    df = pd.DataFrame(data_list, columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])
    df.to_csv(f'human_attribute_sai_{id_}.csv', index=False)
    
    # 데이터 리스트 초기화
    data_list = []

# 마지막 저장 (모든 ID를 처리한 후에 마지막으로 저장)
if data_list:  # 남아 있는 데이터가 있을 경우
    df = pd.DataFrame(data_list, columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])
    df.to_csv('human_attribute_sai_final.csv', index=False)

df_combine = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])

for i in range(35):
    file_name = f'human_attribute_sai_id_{i:02d}.csv'
    df = pd.read_csv(file_name)
    df_combine = pd.concat([df_combine, df])

try:
    # df - pd.read_csv('human_attribute_sai_final.csv')
    df_combine = pd.concat([df_combine, df])
    df_combine.to_csv('human_attribute_sai.csv')
except:
    pass

for i in range(35):
    file_name = f'human_attribute_sai_id_{i:02d}.csv'
    os.remove(file_name)
    # os.remove('human_attribute_sai_final.csv')