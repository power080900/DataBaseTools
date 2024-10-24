import os
import pandas as pd
import json

label_dir = 'Z:\\DataVoucher2023_seatbelt\\data\\IR\\labeldata'
img_dir = 'Z:\\DataVoucher2023_seatbelt\\data\\IR\\rawdata'
label_states = os.listdir(label_dir)
label_ids = os.listdir(label_dir)

df = pd.DataFrame(columns=['userID','sex','age','mask','glasses','seatbelt','cigar','phone'])

for label_id in label_ids:
    id_dir = os.path.join(label_dir, label_id)
    label_files = os.listdir(id_dir)

    for label_file in label_files:
        print(label_file)
        label_path = os.path.join(id_dir, label_file)
        with open(label_path, 'r', encoding='utf-8') as f:
            label_data = json.load(f)

        # print(label_data)

        user_ID = label_data['UserInfo']['ID']
        
        sex = label_data['UserInfo']['Gender']
        age = label_data['UserInfo']['Age']
        mask = label_data['Accessory']['Mask']
        glasses = label_data['Accessory']['Glasses']
        seatbelt = label_data['ObjectInfo']['Seatbelt']['Occluded']
        ObjectInfo = label_data['ObjectInfo']
        
        cigar = label_data['ObjectInfo']['BoundingBox']['Cigar']['isVisible']
        phone = label_data['ObjectInfo']['BoundingBox']['Phone']['isVisible']

        result = [user_ID, sex, age, mask, glasses, seatbelt, cigar, phone]
        df.loc[len(df)] = result

# print(df)

df.to_csv('label_data.csv', index=False)