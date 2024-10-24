import os
import pandas as pd
import base64
from PIL import Image
from io import BytesIO
import requests

dir1 = 'Z:\\MS_Celeb_1M\\data\\aligned_face_images\\FaceImageCroppedWithAlignment.tsv'
num_cols = len(pd.read_csv(dir1, sep='\t', header=None, nrows=1).columns)
df1 = pd.read_csv(dir1, sep='\t', header=None, usecols=range(num_cols-1))
print('df load done')
df2 = df1.drop_duplicates(subset=[2])
df2 = df2.sort_values(1)

TIMEOUT = 300

for index, row in df2.iterrows():
    if index % 1000 == 0:
        print(index)
    id_ = row[1]
    img_url = row[2]
    print(img_url)
    extension = img_url.split('.')[-1]
    img_save_dir1 = f'Z:\\MS_Celeb_1M\\data\\aligned_face_images\\imgs\\id_{id_:02d}'
    
    if not os.path.exists(img_save_dir1):
        os.makedirs(img_save_dir1)
    num = len(os.listdir(img_save_dir1))
    try:
        # URL에서 이미지 요청
        response = requests.get(img_url, timeout=TIMEOUT)
        response.raise_for_status()  # HTTP 오류가 발생한 경우 예외 발생
        
        # 이미지 열기
        image = Image.open(BytesIO(response.content))
        
        # 이미지 파일명 생성
        try:
            file_name = f"{img_save_dir1}\\id_{id_:02d}_{num:02d}.jpg"
            
            # 이미지 저장
            image.save(file_name)
            print(f"이미지 다운로드 및 저장 완료: {file_name}")
        except:
            file_name = f"{img_save_dir1}\\id_{id_:02d}_{num:02d}.{extension}"
        
            # 이미지 저장
            image.save(file_name)
            print(f"이미지 다운로드 및 저장 완료: {file_name}")
        
    except requests.exceptions.Timeout:
        print(f"이미지 다운로드 중 타임아웃 발생: {img_url} (5분 이내로 완료되지 않아 스킵)")
    except Exception as e:
        print(f"이미지 다운로드 중 오류 발생: {e}")

print("완료")