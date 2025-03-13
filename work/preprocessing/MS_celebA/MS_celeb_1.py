import os
import pandas as pd
import requests
import cv2
import numpy as np
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

Timeout = 30

csv_file = 'C:\\lee\\work\\Database\\code\\DB_Tools\\datasets\\MS_celebA\\FaceImageCroppedWithAlignment_resave.csv'
save_dir = 'Z:\\MS_Celeb_1M\\data\\rawdata'

col_name = ['id', 'num', 'url', 'home', 'downloaded']

reader = pd.read_csv(csv_file, names=col_name, header=None, skiprows=1)
reader['downloaded'] = None

print(reader.head())

img_id = reader['id']
img_num = reader['num']
img_url = reader['url']

def download_image(i):
    img_path = os.path.join(save_dir, img_id[i])
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    
    img_save = os.path.join(img_path, f'{img_id[i]}_{str(img_num[i])}.jpg')

    try:
        nums = 1
        response = requests.get(img_url[i], timeout=Timeout)
        img = cv2.imdecode(np.frombuffer(response.content, np.uint8), cv2.IMREAD_COLOR)

        while os.path.exists(img_save):
            img_save = os.path.join(img_path, f'{img_id[i]}_{str(img_num[i])}_{str(nums)}.jpg')
            nums += 1
        
        cv2.imwrite(img_save, img)
        return i, 'Y'
    except requests.exceptions.Timeout:
        return i, 'N'
    except Exception as e:
        return i, 'N'

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(download_image, i): i for i in range(len(img_id))}
    
    for future in tqdm(as_completed(futures), total=len(futures)):
        i, status = future.result()
        reader.at[i, 'downloaded'] = status

    reader.to_csv(csv_file, index=False)
    print('Final save csv file: ', csv_file)
