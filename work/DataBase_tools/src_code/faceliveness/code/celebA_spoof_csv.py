import os
import pandas as pd
import numpy as np
import json

celebA_spoof_label = 'Z:\\celebA_spoof\\metadata\\protocol1'
con_list = os.listdir(celebA_spoof_label)

attack_label = {
    0: 'Live',
    1: 'Photo',
    2: 'Poster',
    3: 'A4',
    4: 'Face Mask',
    5: 'Upper Body Mask',
    6: 'Region Mask',
    7: 'PC',
    8: 'Pad',
    9: 'Phone',
    10: '3D Mask'
}

light_label = {
    0: 'Live',
    1: 'Normal',
    2: 'strong',
    3: 'Back',
    4: 'Dark'
}
Environment = {
    0: 'Live',
    1: 'Indoor',
    2: 'Outdoor'
}

df = pd.DataFrame(columns=['img','attack','attack_type','light_type','Environment_type'])
df1 = pd.DataFrame(columns=['img','attack','attack_type','light_type','Environment_type'])

for con in con_list:
    if con.endswith('.json'):
        file = os.path.join(celebA_spoof_label, con)
        print('start')
        with open(file, 'r') as f:
            data = json.load(f)
        num = 1
        for key,value in data.items():
            print(num,'/',len(data))
            dir = key.split('/')[-2:]
            img = dir[0] + '/' + dir[1]
            attack = key.split('/')[-2]
            attack_type = value[40]
            light = value[41]
            Environment_type = value[42]
            df1.loc[len(df1)] = {'img': img, 'attack': attack, 'attack_type': attack_label[attack_type], 'light_type': light_label[light], 'Environment_type': Environment[Environment_type]}
            num += 1

            if num % 100000 == 0:
                df = pd.concat([df, df1], axis=0)
                df.to_csv('celeb_A_spoof.csv', index=False)
                df1 = pd.DataFrame(columns=['img', 'attack', 'attack_type'])
        df = pd.concat([df, df1], axis=0)
        df.to_csv('celeb_A_spoof.csv', index=False)
