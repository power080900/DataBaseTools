import os
import pandas as pd
import numpy as np

UTMULTIVIEW = 'Z:\\UTMULTIVIEW\\data\\grayscale\\labeldata\\synth'

df = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])
df1 = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])

UTMULTIVIEW_labels = os.listdir(UTMULTIVIEW)

for num, label in enumerate(UTMULTIVIEW_labels):
    if num >= 25:
        print(num, '/', len(UTMULTIVIEW_labels))
        label_path = os.path.join(UTMULTIVIEW, label)
        mpii_df = pd.read_csv(label_path, sep=' ')
        # print(mpii_df.head())
        for i in range(len(mpii_df)):
            print(i, '/', len(mpii_df))
            file = mpii_df['Image'][i]
            gaze_x, gaze_y = mpii_df['2DGaze'][i].split(',')
            gaze_x = np.rad2deg(float(gaze_x))
            gaze_y = np.rad2deg(float(gaze_y))
            
            df1.loc[len(df1)] = [file, gaze_x, gaze_y]

        df = pd.concat([df,df1])
        df.to_csv('gaze_utmulti.csv', index=False)
        df1 = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])
    else:
        continue
df.to_csv('gaze_utmulti.csv', index=False)