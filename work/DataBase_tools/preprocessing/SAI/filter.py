import os
import pandas as pd
import shutil

csv_path = 'C:\\lee\\work\\Database\\code\\DB_Tools\\datasets\\SAI\\save'
csv_files = os.listdir(csv_path)

for csv_file in csv_files:
    csv_ = os.path.join(csv_path, csv_file)
    
    df = pd.DataFrame()

    df = pd.read_csv(csv_)
    gesture_list = ['vehicle_default', 
                    'vehicle_pointing_vertical_surface',
                    'vehicle_counting_in_5',
                    'vehicle_counting_in_1',
                    'vehicle_counting_out_4',
                    'vehicle_counting_in_2',
                    'vehicle_counting_in_3',
                    'vehicle_counting_out_2',
                    'vehicle_counting_out_3',
                    'vehicle_counting_out_1',
                    'vehicle_counting_in_4',
                    'vehicle_counting_out_5']

    df1 = df[(df['gesture'].isin(gesture_list)) & (df['lens_color'] == 'default') & (df['transparency'] >= 0.7) & (df['metalness'] >= 0)]

    for i in range(len(df1)):
        # print(f'{i+1}/{len(df1)}', end='\r', flush=True)
        label_file = df1.iloc[i]['label_file']
        img_path = df1.iloc[i]['img_path']

        rep_label_file = label_file.replace('IR','DY\\no_sunglasees\\')
        rep_img_path = img_path.replace('IR','DY\\no_sunglasees\\')

        print(rep_label_file)
        print(rep_img_path)
        if not os.path.exists(os.path.dirname(rep_label_file)):
            os.makedirs(os.path.dirname(rep_label_file))
        if not os.path.exists(os.path.dirname(rep_img_path)):
            os.makedirs(os.path.dirname(rep_img_path))

        shutil.copy(label_file, rep_label_file)
        shutil.copy(img_path, rep_img_path)
        

    df2 = df[(df['gesture'].isin(gesture_list)) & (df['lens_color'] != 'default')]

    for i in range(len(df2)):
        # print(f'{i+1}/{len(df1)}', end='\r', flush=True)
        label_file = df2.iloc[i]['label_file']
        img_path = df2.iloc[i]['img_path']

        rep_label_file = label_file.replace('IR','DY\\sunglasees\\')
        rep_img_path = img_path.replace('IR','DY\\sunglasees\\')

        print(rep_label_file)
        print(rep_img_path)
        if not os.path.exists(os.path.dirname(rep_label_file)):
            os.makedirs(os.path.dirname(rep_label_file))
        if not os.path.exists(os.path.dirname(rep_img_path)):
            os.makedirs(os.path.dirname(rep_img_path))

        shutil.copy(label_file, rep_label_file)
        shutil.copy(img_path, rep_img_path)
        




            
            
