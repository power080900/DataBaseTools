import os
import json
import pandas as pd

seatbelt_images_cv = 'Z:\\seatbelt_images_cv\\data\\RGB\\rawdata'
seatbelt_images_cv_ids = os.listdir(seatbelt_images_cv)
df = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion','item'])
df1 = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion','item'])

for num, id in enumerate(seatbelt_images_cv_ids):
    print(num, '/', len(seatbelt_images_cv_ids))
    seatbelt_images_cv_path = os.path.join(seatbelt_images_cv, id)
    seatbelt_images_cv_files = os.listdir(seatbelt_images_cv_path)
    for cnt, file in enumerate(seatbelt_images_cv_files):
        age = 'Unknown'
        gender = 'Unknown'
        Lighting = 'Unknown'
        Action = 'Unknown'
        Occlusion = 'Unknown'
        item = 'seatbelt'
        df1.loc[len(df1)] = [file,age,gender,Lighting,Action,Occlusion,item]
    df = pd.concat([df,df1])
    df.to_csv('seatbelt_images_cv.csv', index=False)
    df1 = pd.DataFrame(columns=['label','age','gender','Lighting','Action','Occlusion'])
df.to_csv('seatbelt_images_cv.csv', index=False)