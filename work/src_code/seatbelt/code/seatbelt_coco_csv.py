import os
import pandas as pd
import json

seatbelt_coco = "Z:\\seatbelt_coco\\data\\RGB\\labeldata"
seatbelt_coco_ids = os.listdir(seatbelt_coco)

category_list = {
    0:"seatbelt_none",
    1:"gloves",
    2:"helmet",
    3:"seatbelt_seatbelt",
    4:"vest"}

df = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion','item'])
df1 = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion','item'])
df_image = pd.DataFrame(columns= ['file_name','id'])

for id_ in seatbelt_coco_ids:
    seatbelt_coco_path = os.path.join(seatbelt_coco, id_)
    seatbelt_coco_files = os.listdir(seatbelt_coco_path)
    for cnt, file in enumerate(seatbelt_coco_files):
        print(cnt, '/', len(seatbelt_coco_files))
        file_path = os.path.join(seatbelt_coco_path, file)
        with open(file_path, 'r',encoding='UTF-8') as f:
            data = json.load(f)
        images = data['images']
        annotations = data['annotations']

        for i in range(len(images)):
            image_id = images[i]['id']
            file_name = images[i]['file_name']
            df_image.loc[len(df_image)] = [file_name, image_id]

        for j in range(len(annotations)):
            print(j, '/', len(annotations))
            category_id = annotations[j]['category_id']
            segmentation = annotations[j]['segmentation']
            image_id = annotations[j]['image_id']
            file_name = df_image.loc[df_image['id'] == image_id, 'file_name'].values[0]
            category = category_list[category_id]
            age = 'unknow'
            gender = 'unknow'
            lighting = 'unknown'
            action = 'unknown'
            occlusion = 'unknown'
            item = category
            df1.loc[len(df1)] = [file_name, age,gender,lighting,action,occlusion,item]
    df = pd.concat([df,df1])
    df.to_csv('seatbelt_coco.csv', index=False)
    df1 = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion','item'])
df.to_csv('seatbelt_coco.csv', index=False)

        
        
            
