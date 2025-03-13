import os
import pandas as pd


sviro_uncertainty = 'Z:\\sviro_uncertainty\\data\\IR\\labeldata'
sviro_uncertainty_ids = os.listdir(sviro_uncertainty)

df = pd.DataFrame(columns=['label', 'object'])
df1 = pd.DataFrame(columns=['label', 'object'])

for num, id in enumerate(sviro_uncertainty_ids):
    if 'object' in id:
        print(num, '/', len(sviro_uncertainty_ids))
        sviro_uncertainty_path = os.path.join(sviro_uncertainty, id)
        sviro_uncertainty_files = os.listdir(sviro_uncertainty_path)
        for cnt, file in enumerate(sviro_uncertainty_files):
            print(cnt, '/', len(sviro_uncertainty_files))
            file_path = os.path.join(sviro_uncertainty_path, file)
            data = pd.read_csv(file_path)
            objects = data.loc[data['label'] == 'EverydayObject']['label_id']
            for object in objects:
                # print(object)
                df1.loc[len(df1)] = [file, object]
        df = pd.concat([df,df1])
        df.to_csv('obj_sviro_uncertainty.csv', index=False)
        df1 = pd.DataFrame(columns=['label', 'object'])

df.to_csv('obj_sviro_uncertainty.csv', index=False)
