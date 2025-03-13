import os
import pandas as pd
import xml.etree.ElementTree as ET

root_dir = 'Z:\\smoking_face\\data\\RGB\\labeldata'
ids = os.listdir(root_dir)

df = pd.DataFrame(columns = ['label','object'])
df1 = pd.DataFrame(columns = ['label','object'])

for id_ in ids:
    print(id_)
    sai_file_path = os.path.join(root_dir, id_)
    sai_file = os.listdir(sai_file_path)
    for num, file in enumerate(sai_file):
        print(num,'/',len(sai_file))
        object = 'smoking'

        # 추출한 label 값 출력
        
        df1.loc[len(df1)] = [file, object]
                
    df = pd.concat([df, df1])
        
    df.to_csv(f'obj_smoking_face.csv', index=False)
    df1 = pd.DataFrame(columns = ['label','object'])
