import os
import shutil
from glob import glob

root = 'Z:\\RT_GENE\\data\\RGB\\labeldata'
org_root = 'Z:\\RT_GENE\\orgdata'
label_path = glob(os.path.join(root,'*','*.label'))

for label in label_path:
    with open(label,'r') as f:
        lines = f.readlines()
    
    for i in range(1,len(lines)):
        lines[i] = lines[i].replace('DataBase','Z:').replace('\n','')
        org_face_img_dir = os.path.join(org_root,lines[i].split(' ')[0].split('\\')[-1])
        org_left_img_dir = os.path.join(org_root,lines[i].split(' ')[1].split('\\')[-1])
        org_right_img_dir = os.path.join(org_root,lines[i].split(' ')[2].split('\\')[-1])

        mv_face_img_dir = os.path.join(root.replace('label','raw'),lines[i].split(' ')[0].split('\\')[-1])
        mv_left_img_dir = os.path.join(root.replace('label','raw'),lines[i].split(' ')[1].split('\\')[-1])
        mv_right_img_dir = os.path.join(root.replace('label','raw'),lines[i].split(' ')[2].split('\\')[-1])

        print(org_face_img_dir, mv_face_img_dir)
        # print(org_left_img_dir, mv_left_img_dir)
        # print(org_right_img_dir, mv_right_img_dir)

        if not os.path.exists(os.path.dirname(mv_face_img_dir)):
            os.makedirs(os.path.dirname(mv_face_img_dir))
        if not os.path.exists(os.path.dirname(mv_left_img_dir)):
            os.makedirs(os.path.dirname(mv_left_img_dir))
        if not os.path.exists(os.path.dirname(mv_right_img_dir)):
            os.makedirs(os.path.dirname(mv_right_img_dir))
        shutil.copy(org_face_img_dir,mv_face_img_dir)
        shutil.copy(org_left_img_dir,mv_left_img_dir)
        shutil.copy(org_right_img_dir,mv_right_img_dir)
        print(f'{mv_face_img_dir} copy done')
        print(f'{mv_left_img_dir} copy done')
        print(f'{mv_right_img_dir} copy done')
