import os
import cv2
import glob
import matplotlib.pyplot as plt
from PIL import Image

def file_list(file_name):
    root_dir = os.getcwd()
    # print(root_dir)
    search_file = f'{root_dir}\\*\\*\\*\\*\\{file_name}'
    print(search_file)
    root_file_list = glob.glob(search_file, recursive=True)
    root_file_list.sort()
    print('number of files :', len(root_file_list))
    return root_file_list

def img_count(root_file_list):
    img_count = {}
    for i in root_file_list:
        scene = i.split('_')[-3]
        if scene in img_count:
            img_count[scene] += 1
        else:
            img_count[scene] = 1
    print(img_count)

def plt_imshow(title='image', img=None, save_dir = None, figsize=(8 ,5)):
    plt.figure(figsize=figsize)
 
    if type(img) == list:
        if type(title) == list:
            titles = title
        else:
            titles = []
 
            for i in range(len(img)):
                titles.append(title)
 
        for i in range(len(img)):
            if len(img[i].shape) <= 2:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2RGB)
            else:
                rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
 
            plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
            plt.title(titles[i])
            plt.xticks([]), plt.yticks([])
 
        plt.show()
    else:
        if len(img.shape) < 3:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
        else:
            rgbImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
 
        plt.imshow(rgbImg)
        plt.title(title)
        plt.xticks([]), plt.yticks([])
        plt.show()