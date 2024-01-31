# **DEEPINSIGHT**

## DATA_SET
- 완료 - 특이사항 확인, 분포확인 및 MySQL 적재 완료
    - MPIIGAZE
    - Gaze360
    - GazeCapture
    - RT_GENE
    - ETH_Xgaze
    - ETH_gaze
    - GI4E
    - U2eyes
    - Eye_Gaze
    - SysntheticHumanEyes
    - RIT-Eyes
    - SYNTHESEYES
    - UNITYEYES
    - UTMULTIVIEW
    - ShanghaiTechGaze

- 진행중
    - NVgave_synthetic_dataset
      - sql 작업 진행중
    - NVgaze_real_dataset_ar
      - sql 작업 진행중
    - NVgaze_real_dataset_vr
      - sql 작업 진행중
    - TeyeD_Dikablis
      - sql 작업 진행중
    - TeyeD_GazeinTheWild
      - sql 작업 진행중
  
- 미완료
    - EYEDIAP
        - 대학소속 연구목적으로 데이터 요청 중
    - OPENEDS: OPEN EYE DATASET
        - 대학소속 연구목적으로 데이터 요청 중
    - AFLW2000
    - AIhub_EyeMovement
    - CASIA
    - coco_dataset
    - DAD
    - DataVoucher2022
    - DataVoucher2023
    - dibox
    - DIS_300VW
    - DIS_300W
    - DIS_300W_3D
    - DIS_300W_3D_FAce
    - DIS_300W_LP
    - DIS_FaceLandmark
    - DIS_shutterstock
    - dmd
    - drive_act
    - drive_act_eat
    - drivers_monitering
    - event_train
    - face_recognition
    - family_id
    - frgc
    - human_motion
    - human_pose
    - LFW_FF_GAN
    - MultiPIE
    - NIA2022
    - nir_fae
    - OBD_2
    - panasonic
    - POCT
    - preventing_drowsy_controlled
    - preventing_drowsy_realroad
    - preventing_drowsy_semicontrolled
    - seatbelt_coco
    - seatbelt_images_cv
    - shanghaiTechGaze
    - sviro
    - sviro_uncertainty
    - Vehicle_CAN_bus
    - xm2vts
    - zer01ne

## *_utils.py 소개*

### JSON_utils.py
데이터에 대한 값이 아닌 정보에 대해 확인하고 싶을때 사용
- load_json
<br>: json을 load하는 함수

- json_to_markdown
<br>: json을 markdown으로 변환하는 함수 json을 시각화하는데에 한계가 있음(정렬과 색변환정도) 데이터프레임으로 변환하자니 json의 깊이가 다 다르기 때문에 각기다른 평활화를 해주어야 하는 문제가 있어  markdown으로 변환을 진행
	
- load_json_and_convert_to_markdown
<br>: json을 load한 후 json_to_markdown함수를 이용하여 markdown으로 변환하는 함수

- print_datasets_with_head_value
<br>: 데이터셋에서 head pose값이 있는 데이테셋 출력하는 함수

- print_datasets_with_gaze_value
<br>: 데이터셋에서 gaze값이 있는 데이테셋 출력하는 함수

- print_datasets_with_landmark_value
<br>: 데이터셋에서 landmark값이 있는 데이테셋 출력하는 함수

- display_markdown
<br>: markdown 출력하는 함수

- print_datasets_volume
<br>: 데이터셋들의 volume을 출력하는 함수

- print_datasets_format
<br>: 데이터셋들의 format을 출력하는 함수

- print_datasets_resolution
<br>: 데이터셋들의 resolution을 출력하는 함수

---

### SQL_utils.py
SQL을 만들거나 SQL서버에서 파이썬환경으로 값을 가져올때 사용 
- create_table
<br>: mysql 서버 안에 테이블을 만드는 함수
- insert_dataset_values
<br>: 테이블에 값을 집어 넣는 함수
- search_SQL
<br>: 테이블에 값을 dataframe으로 변환하여 가져오는 함수
- load_img_dir
<br>: 테이블에서 img_dir값을 dataframe으로 변환하여 가져오는 함수
- load_2D_gaze_data
<br>: 테이블에서 2D_gaze값을 dataframe으로 변환하여 가져오는 함수, 분포확인과 시각화에 이용가능, 다만 데이터셋 마다 정규화 여부가 다르기 때문에 통일화가 필요함 gaze값이 degree가 아닌경우 변환이 필요함
- load_3D_gaze_data
<br>: 테이블에서 3D_gaze값을 dataframe으로 변환하여 가져오는 함수, 분포확인과 시각화에 이용가능, 3D값을 2D평면에 표현하기위한 카메라 정보가 필요, 다만 데이터셋 마다 정규화 여부와 카메라 정보값 존재 여부가 다르기 때문에 통일화및 확인이 필요함 degree가 아닌경우 변환이 필요함
- load_landmark_data
<br>: 테이블에서 landmark값을 dataframe으로 변환하여 가져오는 함수, 분포확인과 시각화에 이용가능, 다만 데이터셋 마다 정규화 여부가 다르기 때문에 통일화가 필요함.

---


### EDA_utils.py
데이터 전처리나 분포를 확인할때 사용 SQL_utils와 함수가 연결되어 값을 가져오도록 구성
- draw_heatmap
<br>: SQL_utils.py에서 불러온 load_2D_gaze_data값의 분포를 heatmap으로 확인하는 함수

- draw_jointplot
<br>: SQL_utils.py에서 불러온 load_2D_gaze_data값의 분포를 jointplot으로 확인하는 함수

- save_frame_from_video
<br>: mp4 파일을 1프레임당 정지이미지로 변환하는 함수

- image_visualization
<br>: SQL_utils.py에서 불러온 load_img_dir을 이용하여 face 이미지를 출력하여 확인하는 함수

---

## *make_.py 소개*

### makeJSON.py
- ppt에 저장하던 데이터셋의 정보들을 정리하여 json으로 정리하여 저장하는 파일

---

### makeSQL.py
- 데이터셋에서 제공하는 라벨값들과 추가 정보들을 mysql서버에 저장하는 파일

--- 

## *Eye_Gaze.json/md 소개*
- eye_gaze 기본 데이터셋 정보 정리한 파일