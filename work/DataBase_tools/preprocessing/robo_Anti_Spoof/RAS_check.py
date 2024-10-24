import os
import pandas as pd
import xml.etree.ElementTree as ET

label_dir = 'Z:\\robo_Anti_Spoof\\data\\RGB\\labeldata'
img_dir = 'Z:\\robo_Anti_Spoof\\data\\RGB\\rawdata'
label_states = os.listdir(label_dir)

# 데이터 프레임 만들기
df = pd.DataFrame(columns=['label_id', 'label_name', 'img_name', 'xmin', 'ymin', 'xmax', 'ymax'])

for state in label_states:
    state_path = os.path.join(label_dir, state)
    label_ids = os.listdir(state_path)
    
    for label_id in label_ids:
        id_path = os.path.join(state_path, label_id)
        label_files = os.listdir(id_path)
        
        for label_file in label_files:
            file_path = os.path.join(id_path, label_file)
            
            tree = ET.parse(file_path)
            root = tree.getroot()
            
            objects = root.findall('object')
            file_name = root.find('filename').text
            img_path = os.path.join(img_dir, label_id, file_name)
            
            for obj in objects:
                bnd = obj.find('bndbox')
                xmin = int(bnd.find('xmin').text)
                ymin = int(bnd.find('ymin').text)
                xmax = int(bnd.find('xmax').text)
                ymax = int(bnd.find('ymax').text)
                
                save_id = f'id_{int(label_id):02d}'
                
                result = pd.DataFrame([[save_id, state, file_name, xmin, ymin, xmax, ymax]], 
                                      columns=['label_id', 'label_name', 'img_name', 'xmin', 'ymin', 'xmax', 'ymax'])
                df = pd.concat([df, result], axis=0)

df.to_csv('Z:\\robo_Anti_Spoof\\data\\RGB\\labeldata.csv', index=False)
print('Done')


            



                