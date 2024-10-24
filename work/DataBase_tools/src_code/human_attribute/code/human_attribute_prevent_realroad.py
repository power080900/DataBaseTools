import os
import pandas as pd
import numpy as np
import json

prevent_real = 'Z:\\preventing_drowsy_realroad\\data\\IR\\labeldata'
prevent_real_ids = os.listdir(prevent_real)

df = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])
df1 = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])

gender_list = {
    1: 'M',
    2: 'F'
    }

for num, id_ in enumerate(prevent_real_ids):
    print(id_)
    print(num, '/', len(prevent_real_ids))
    prevent_real_path = os.path.join(prevent_real, id_)
    # print(prevent_real_path)
    prevent_real_files = os.listdir(prevent_real_path)
    # print(prevent_real_files)
    
    for cnt, file in enumerate(prevent_real_files):
        print(cnt, '/', len(prevent_real_files))
        file_path = os.path.join(prevent_real_path, file)
        with open(file_path, 'r',encoding='UTF-8') as f:
            data = json.load(f)
            age = data['UserInfo']['Age']
            gender = gender_list[int(data['UserInfo']['Gender'])]
            ethnicity = 'asian'
            height = 'unknown'
            weight = 'unknown'
            skin_type = 'unknown'
            glasses = 'Y' if data.get('Accessory', {}).get('Glasses', False) else 'N'
            cap = 'Y' if data.get('Accessory', {}).get('Cap', False) else 'N'
            mask = 'Y' if data.get('Accessory', {}).get('Mask', False) else 'N'
            df1.loc[len(df1)] = [file,age,gender,height,weight,ethnicity,skin_type,glasses,cap,mask]
    df = pd.concat([df,df1])
    df.to_csv('human_attribute_prevent_real.csv', index=False)
    df1 = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])
df.to_csv('human_attribute_prevent_real.csv', index=False)


                                 
