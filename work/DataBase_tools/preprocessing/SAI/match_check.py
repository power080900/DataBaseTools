import os
import pandas as pd

label_root_dir = 'Z:\\SAI\\data\\IR\\labeldata'
img_root_dir = 'Z:\\SAI\\data\\IR\\rawdata'
id_list = os.listdir(label_root_dir)
match_df = pd.DataFrame(columns=['id', 'label', 'match'])


for id in id_list:
    print()
    print(id)
    num = 1
    label_id_path = os.path.join(label_root_dir, id)
    img_id_path = os.path.join(img_root_dir, id)
    label_list = os.listdir(label_id_path)
    img_list = os.listdir(img_id_path)

    for label in label_list:
        processor_bar = "".join(["\033[41m%s\033[0m" % '   '] * int(num / len(label_list) * 20))
        processor_bar = "\r" + processor_bar + f" {num}|{len(label_list)}"
        print(processor_bar, end="", flush=True)

        label_file = os.path.join(label_id_path, label)
        img_file = os.path.join(img_id_path, label.replace('.json', '.png').replace('.info','.rgb'))
        

        if not os.path.exists(img_file):
            print(img_file)
            matchs = 'No'
        
        else:
            num += 1
            matchs = 'Yes'

        df = [label_file,img_file, matchs]
        match_df.loc[len(match_df)] = df

    match_df.to_csv(f'match{id}.csv', index=False)

        
            

