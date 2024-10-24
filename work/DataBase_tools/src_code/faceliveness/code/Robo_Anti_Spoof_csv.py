import os
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

robo_spoof_path = 'Z:\\Robo_Anti_Spoof\\data\\RGB\\labeldata'
robo_cons = os.listdir(robo_spoof_path)

df = pd.DataFrame(columns=['img','attack','attack_type','light_type','Environment_type'])
df1 = pd.DataFrame(columns=['img','attack','attack_type','light_type','Environment_type'])

for con in robo_cons:
    robo_id_path = os.path.join(robo_spoof_path, con)
    robo_id_list = os.listdir(robo_id_path)
    
    for robo_id in robo_id_list:
        print(robo_id,'/', len(robo_id_list))
        robo_file_path = os.path.join(robo_id_path, robo_id)
        robo_files = os.listdir(robo_file_path)

        for file in robo_files:
            if file.endswith('.xml'):
                tree = ET.parse(os.path.join(robo_file_path, file))
                root = tree.getroot()
                
                img = filename = root.find('filename').text
                attack = con
                if attack == 'live':
                    attack_type = 'Live'
                    light_type = 'Live'
                    Environment_type = 'Live'
                else:
                    attack_type = 'Unknown'
                    light_type = 'Unknown'
                    Environment_type = 'Unknown'
                df1.loc[len(df1)] = {'img': img, 'attack': attack, 'attack_type': attack_type}
        df = pd.concat([df,df1])
        df.to_csv('robo_anti_spoof.csv', index=False)
        df1 = pd.DataFrame(columns=['img','attack','attack_type'])


    
