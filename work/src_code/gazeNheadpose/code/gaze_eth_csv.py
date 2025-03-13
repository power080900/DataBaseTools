import pandas as pd
import numpy as np

eth_xgaze_label = 'Z:\\ETH_Xgaze\\data\\RGB\\labeldata\\train.label'

eth_data = pd.read_csv(eth_xgaze_label, sep=' ')

df = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])
df1 = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])

for i in range(len(eth_data)):
    if i > 900000:
    
        print(i, '/', len(eth_data))
        eth_gaze_x, eth_gaze_y = eth_data['Gaze_2D'][i].split(',')
        file = eth_data['Image'][i]
        eth_gaze_x = np.rad2deg(float(eth_gaze_x))
        eth_gaze_y = np.rad2deg(float(eth_gaze_y))
        df1.loc[len(df1)] = [file, eth_gaze_x, eth_gaze_y]
        if i % 100000 == 0:
            df = pd.concat([df,df1])
            df.to_csv('gaze_eth4.csv', index=False)
            df1 = pd.DataFrame(columns=['label','Gaze_x','Gaze_y'])
    else:
        continue
        
df.to_csv('gaze_eth4.csv', index=False)