import os
import json
import pandas as pd

seatbelt_DV2023 = 'Z:\\DataVoucher2023_seatbelt\\data\\IR\\labeldata'
seatbelt_DV2023_ids = os.listdir(seatbelt_DV2023)
df = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion','item'])
df1 = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion','item'])

gender_list = {
    1: 'M',
    2: 'F'
    }

for num, id in enumerate(seatbelt_DV2023_ids):
    print(num, '/', len(seatbelt_DV2023_ids))
    seatbelt_DV2023_path = os.path.join(seatbelt_DV2023, id)
    seatbelt_DV2023_files = os.listdir(seatbelt_DV2023_path)
    for cnt, file in enumerate(seatbelt_DV2023_files):
        file_path = os.path.join(seatbelt_DV2023_path, file)
        with open(file_path, 'r',encoding='UTF-8') as f:
            data = json.load(f)
            age = data['UserInfo']['Age']
            gender = gender_list[int(data['UserInfo']['Gender'])]
            Lighting = 'Unknown'
            Action = 'Unknown'
            Occlusion = 'Unknown'
            item = 'seatbelt'
            df1.loc[len(df1)] = [file,age,gender,Lighting,Action,Occlusion]
    df = pd.concat([df,df1])
    df.to_csv('seatbelt_DV2023.csv', index=False)
    df1 = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion'])
df.to_csv('seatbelt_DV2023.csv', index=False)