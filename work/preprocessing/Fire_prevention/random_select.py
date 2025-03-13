import random
from glob import glob
import os
import shutil

img_list = glob(os.path.join(os.getcwd(),'*','*','*', '*.jpg'))

select_img = random.sample(img_list, 5000)

for img in select_img:
    label = img.replace('image', 'label').replace('jpg', 'json')
    
    rep_img = img.replace('org','select')
    rep_label = label.replace('org','select')

    rep_img_dir = os.path.dirname(rep_img)
    rep_label_dir = os.path.dirname(rep_label)

    if not os.path.exists(rep_img_dir):
        os.makedirs(rep_img_dir)
    if not os.path.exists(rep_label_dir):
        os.makedirs(rep_label_dir)
    
    shutil.copy(img, rep_img)
    shutil.copy(label, rep_label)