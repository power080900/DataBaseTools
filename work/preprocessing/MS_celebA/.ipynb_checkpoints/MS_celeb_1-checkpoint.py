import os
import pandas as pd
from PIL import Image
from io import BytesIO
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

CHUNK_SIZE = 10000  # 청크 크기 설정
TIMEOUT = 300
SAVE_INTERVAL = 1000  # 주기적으로 저장할 행 수
THREAD_COUNT = 10  # 병렬로 실행할 스레드 수

dir1 = 'Z:\\MS_Celeb_1M\\data\\aligned_face_images\\FaceImageCroppedWithAlignment.tsv'
num_cols = len(pd.read_csv(dir1, sep='\t', header=None, nrows=1).columns)
df1 = pd.read_csv(dir1, sep='\t', header=None, usecols=range(num_cols-1), chunksize=CHUNK_SIZE)
print('df load done')

def download_image(row):
    index, data = row
    id_ = data[0]
    img_url = data[2]
    img_save_dir1 = f'Z:\\MS_Celeb_1M\\data\\aligned_face_images\\imgs\\id_{id_}'
    
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
        file_name = f"{img_save_dir1}\\id_{id_}_{num}.jpg"
        image.save(file_name)
        return index, file_name

    except requests.exceptions.Timeout:
        return index, 'None'
    except Exception as e:
        return index, 'None'

def process_chunk(chunk, chunk_index):
    chunk['downloaded_name'] = None

    with ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
        futures = {executor.submit(download_image, row): row for row in chunk.iterrows()}
        
        for i, future in tqdm(enumerate(as_completed(futures)), total=len(futures)):
            index, file_name = future.result()
            chunk.at[index, 'downloaded_name'] = file_name

            if (i + 1) % SAVE_INTERVAL == 0:
                save_path = f'Z:\\MS_Celeb_1M\\data\\aligned_face_images\\temp\\FaceImageCroppedWithAlignment_with_downloaded_names_resave_chunk_{chunk_index}.csv'
                chunk.to_csv(save_path, index=False)
                print(f"중간 저장 완료: {save_path}")

    return chunk

# 임시 저장 디렉토리 생성
temp_dir = 'Z:\\MS_Celeb_1M\\data\\aligned_face_images\\temp'
if not os.path.exists(temp_dir):
    os.makedirs(temp_dir)

# 청크 단위로 데이터 로드 및 처리
all_chunks = []

for chunk_index, chunk in enumerate(df1):
    chunk = chunk.drop_duplicates(subset=[2])
    chunk = chunk.sort_values(0)
    processed_chunk = process_chunk(chunk, chunk_index)

    temp_path = f'{temp_dir}\\FaceImageCroppedWithAlignment_with_downloaded_names_temp_chunk_{chunk_index}.csv'
    processed_chunk.to_csv(temp_path, index=False)
    print(f"청크 {chunk_index} 임시 저장 완료: {temp_path}")
    all_chunks.append(temp_path)

# 모든 청크 파일을 하나의 최종 파일로 결합
final_save_path = 'Z:\\MS_Celeb_1M\\data\\aligned_face_images\\FaceImageCroppedWithAlignment_with_downloaded_names_final.csv'

with open(final_save_path, 'w') as final_file:
    for i, chunk_file in enumerate(all_chunks):
        with open(chunk_file, 'r') as f:
            if i != 0:
                # 첫번째 청크 파일 이후로는 헤더 제거
                next(f)
            final_file.write(f.read())

print(f"최종 저장 완료: {final_save_path}")

# 임시 파일 삭제
for chunk_file in all_chunks:
    os.remove(chunk_file)
print("임시 파일 삭제 완료")