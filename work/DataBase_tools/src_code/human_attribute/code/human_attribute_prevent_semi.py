import os
import pandas as pd
import numpy as np
import json

prevent_semi = 'Z:\\preventing_drowsy_semicontrolled\\data\\IR\\labeldata'
prevent_semi_ids = os.listdir(prevent_semi)

df = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])
df1 = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])

gender_list = {
    1: 'M',
    2: 'F'
    }

for num, id_ in enumerate(prevent_semi_ids):
    print(id_)
    print(num, '/', len(prevent_semi_ids))
    prevent_semi_path = os.path.join(prevent_semi, id_)
    # print(prevent_real_path)
    prevent_semi_files = os.listdir(prevent_semi_path)
    # print(prevent_real_files)
    
    for cnt, file in enumerate(prevent_semi_files):
        print(cnt, '/', len(prevent_semi_files))
        file_path = os.path.join(prevent_semi_path, file)
        with open(file_path, 'r',encoding='UTF-8') as f:
            data = json.load(f)
            age = data['UserInfo']['Age']
            gender = gender_list[int(data['UserInfo']['Gender'])]
            height = 'unknown'
            weight = 'unknown'
            skin_type = 'unknown'
            ethnicity = 'asian'
            glasses = 'Y' if data.get('Accessory', {}).get('Glasses', False) else 'N'
            cap = 'Y' if data.get('Accessory', {}).get('Cap', False) else 'N'
            mask = 'Y' if data.get('Accessory', {}).get('Mask', False) else 'N'

            df1.loc[len(df1)] = [file,age,gender,height,weight,ethnicity,skin_type,glasses,cap,mask]
    df = pd.concat([df,df1])
    df.to_csv('human_attribute_prevent_semi.csv', index=False)
    df1 = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])
df.to_csv('human_attribute_prevent_semi.csv', index=False)


                                 
