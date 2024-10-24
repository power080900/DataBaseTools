import os
from glob import glob
import shutil

label_folder = 'Z:\\U2Eyes\\data\\RGB\\labeldata\\*\\*\\*'
img_list = glob(os.path.join(label_folder,'*.png'))

for i in img_list:
    os.remove(i)