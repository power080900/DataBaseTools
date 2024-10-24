import os
import pandas as pd
import json

root_dir = 'Z:\\SAI\\data\\IR\\labeldata'
ids = os.listdir(root_dir)

df = pd.DataFrame(columns = ['label','expression', 'hair_style', 'hair_length',
               'facial_hair', 'facial_hair_length', 'mask', 'glasses', 
               'glasses_lens','glasses_transparency', 'headwear'])
df1 = pd.DataFrame(columns = ['label','expression', 'hair_style', 'hair_length',
                'facial_hair', 'facial_hair_length', 'mask', 'glasses', 
                'glasses_lens','glasses_transparency', 'headwear'])

for id_ in ids:
    print(id_)
    sai_file_path = os.path.join(root_dir, id_)
    sai_file = os.listdir(sai_file_path)
    for num, file in enumerate(sai_file):
        print(num,'/',len(sai_file))
        with open(os.path.join(sai_file_path, file)) as f:
            data = json.load(f)

        expression = data['facial_attributes']['expression']['name']
        hair_style = data['facial_attributes']['hair']['style']
        hair_length = data['facial_attributes']['hair']['relative_length']
        if 'facial_hair' not in data['facial_attributes']:
            facial_hair = 'None'
            facial_hair_length = 'None'
        else:
            facial_hair = data['facial_attributes']['facial_hair']['style']
            facial_hair_length = data['facial_attributes']['facial_hair']['relative_length']
        mask = data['accessories']['mask']['style']
        glasses = data['accessories']['glasses']['style']
        glasses_lens = data['accessories']['glasses']['lens_color']
        glasses_transparency = data['accessories']['glasses']['transparency']
        headwear = data['accessories']['headwear']['style']

        
        df1.loc[len(df1)] = [file, expression, hair_style, hair_length, facial_hair, facial_hair_length, mask, glasses, glasses_lens, glasses_transparency, headwear]
    df = pd.concat([df, df1])
        
    df.to_csv(f'fa_sai_{id_}.csv', index=False)
    df1 = pd.DataFrame(columns = ['label','expression', 'hair_style', 'hair_length',
            'facial_hair', 'facial_hair_length', 'mask', 'glasses', 
            'glasses_lens','glasses_transparency', 'headwear'])
    df = pd.DataFrame(columns = ['label','expression', 'hair_style', 'hair_length',
            'facial_hair', 'facial_hair_length', 'mask', 'glasses', 
            'glasses_lens','glasses_transparency', 'headwear'])
        

file_pattern = "fa_sai_id_{:02d}.csv"

# 빈 리스트를 만들어서 데이터를 저장할 준비
dataframes = []

# 0부터 34까지의 파일을 읽어들여 리스트에 추가
for i in range(35):
    file_name = file_pattern.format(i)
    df = pd.read_csv(file_name)
    dataframes.append(df)

# 모든 데이터를 하나의 데이터프레임으로 결합
combined_df = pd.concat(dataframes, ignore_index=True)

# 결합된 데이터를 새로운 CSV 파일로 저장
combined_df.to_csv("fa_iris_sai.csv", index=False)
