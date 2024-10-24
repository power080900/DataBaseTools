import os
import pandas as pd
import json

prevent_controll = 'Z:\\preventing_drowsy_controlled\\data\\IR\\labeldata'
prevent_controll_ids = os.listdir(prevent_controll)

df = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])
df1 = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])

gender_list = {
    1: 'M',
    2: 'F'
    }

for num, id in enumerate(prevent_controll_ids):
    print(num, '/', len(prevent_controll_ids))
    prevent_controll_path = os.path.join(prevent_controll, id)
    prevent_controll_files = os.listdir(prevent_controll_path)
    for cnt, file in enumerate(prevent_controll_files):
        file_path = os.path.join(prevent_controll_path, file)
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
    df.to_csv('human_attribute_prevent_controll.csv', index=False)
    df1 = pd.DataFrame(columns=['label', 'age', 'gender','height','weight', 'ethnicity','skin_type', 'glasses', 'cap', 'mask'])
df.to_csv('human_attribute_controll.csv', index=False)


                                 
