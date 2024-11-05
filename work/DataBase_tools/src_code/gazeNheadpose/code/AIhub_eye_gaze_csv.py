import os
import pandas as pd

df = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])

aihub_eye = 'Z:\\AIhub_EyeMovement\\data\\IR\\labeldata\\'
aihub_eye_ids = os.listdir(aihub_eye)

for num, id_ in enumerate(aihub_eye_ids):
    print(num,'/',len(aihub_eye_ids))
    aihub_eye_path = os.path.join(aihub_eye, id_)
    aihub_eye_file = os.listdir(aihub_eye_path)
    for file in aihub_eye_file:
        ext = file.split('.')[-1]
        if ext == 'csv':
            file_path = os.path.join(aihub_eye_path, file)
            aihub_eye_data = pd.read_csv(file_path, index_col=0)
            # print(aihub_eye_data)
            gaze_x = aihub_eye_data['x']*1024
            gaze_y = aihub_eye_data['y']*1024
            print(gaze_x, gaze_y)
            # print(type(gaze_x), type(gaze_y))
            df.loc[len(df)] = [file, gaze_x, gaze_y]

    df.to_csv('gaze_aihub_eye.csv', index=False)