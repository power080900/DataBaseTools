import numpy    as np   
import pandas as pd



df = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])

gaze_360 = 'Z:\\Gaze360_normalized\\data\\RGB\\labeldata\\train.label'

gaze_360_data = pd.read_csv(gaze_360, sep=' ')

df = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])

for i in range(len(gaze_360_data)):
    print(i, '/', len(gaze_360_data))
    gaze_x, gaze_y = gaze_360_data['Gaze_2D'][i].split(',')
    gaze_x = np.rad2deg(float(gaze_x))
    gaze_y = np.rad2deg(float(gaze_y))
    file = gaze_360_data['Image'][i]
    df.loc[len(df)] = [file, gaze_x, gaze_y]

    if i % 100000 == 0:
        df.to_csv('gaze_360.csv', index=False)

df.to_csv('gaze_360.csv', index=False)