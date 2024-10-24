import os
import shutil

img_path = 'C:\\lee\\CelebA_Spoof\\Data\\RGB\\Images'
label_path = 'C:\\lee\\CelebA_Spoof\\Data\\RGB\\Labels'
id_list = os.listdir(img_path)

for num, id_ in enumerate(id_list):
    print(num, len(id_list))
    id_path = os.path.join(img_path,id_)
    cons = os.listdir(id_path)
    for con in cons:
        con_path = os.path.join(id_path,con)
        file_list = os.listdir(con_path)
        for file in file_list:
            if file.split('.')[-1] == 'txt':
                tar_file = os.path.join(con_path,file)
                rep_path = os.path.join(label_path,con,id_)
                rep_file = os.path.join(rep_path,file)
                
                if not os.path.exists(rep_path):
                    os.makedirs(rep_path)
                shutil.copy(tar_file,rep_file)
            
            else:
                tar_file = os.path.join(con_path,file)
                rep_path = os.path.join(img_path,con,id_)
                rep_file = os.path.join(rep_path,file)
                
                if not os.path.exists(rep_path):
                    os.makedirs(rep_path)
                shutil.copy(tar_file,rep_file)

