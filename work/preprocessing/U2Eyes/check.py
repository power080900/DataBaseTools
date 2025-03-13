import os
from glob import glob
import cv2
import numpy as np
import math
import xml.etree.ElementTree as ET




import math
# # 시선의 x, y, z 좌표
# x = 0
# y = 11
# z = 0
# # 시선 벡터의 크기 계산 (벡터를 정규화하기 위해 사용)
# magnitude = math.sqrt(x**2 + y**2 + z**2)
# # 시선 벡터를 정규화하여 단위 벡터 얻기
# unit_vector = (x / magnitude, y / magnitude, z / magnitude)
# # pitch와 yaw 계산
# pitch = math.asin(unit_vector[1])  # arcsin(y)
# yaw = math.atan2(unit_vector[0], unit_vector[2])  # arctan(x/z)
# # 결과 출력 (라디안을 도로 변환)
# pitch_degrees = math.degrees(pitch)
# yaw_degrees = math.degrees(yaw)
# print(f"Pitch: {pitch_degrees} degrees")
# print(f"Yaw: {yaw_degrees} degrees")
      



img_folder = 'Z:\\U2Eyes\\data\\RGB\\imagedata\\'
label_folder = 'Z:\\U2Eyes\\data\\RGB\\labeldata\\'
save_folder = 'C:\\lee\\work\\Database\\U2Eyes\\gazeimgdata'

if not os.path.exists(save_folder):
    os.makedirs(save_folder)

label_dir = glob(os.path.join(label_folder, '*\\*\\*'))
# print(label_dir)


for labels in label_dir[:10]:
    label1, label2 = glob(os.path.join(labels, '*.xml'))

    # print(label1, label2)

    with open(label1,'r') as f:
        tree1 = ET.parse(f)
        root1 = tree1.getroot()

    with open(label2,'r') as f:
        tree2 = ET.parse(f)
        root2 = tree2.getroot()
    
    HeadposeDef = root1.iter('HeadposeDef')
    POILeft = root2.iter('POILeft')
    POIRight = root2.iter('POIRight')

    # head pose annotation
    
    for num, (headpose_def, POI_left, POI_right) in enumerate(zip(HeadposeDef, POILeft, POIRight)):
        image_path = os.path.dirname(label2.replace('labeldata','imagedata'))
        image_file = f'{num+1:02d}.png'
        image_dir = os.path.join(image_path,image_file)
        img = cv2.imread(image_dir)

        poi_left = root2.find('POILeft')
        poi_right = root2.find('POIRight')

        poi_left_poi_def = poi_left.find('POIDef')
        poi_right_poi_def = poi_right.find('POIDef')

        
        rotation = headpose_def.find('Rotation')
        position = headpose_def.find('Position')
        look_at_point = headpose_def.find('LookAtPoint')
    
        # Rotation, Position, LookAtPoint 태그 내의 x, y, z 값을 추출
        rotation_x = float(rotation.find('x').text)
        rotation_y = float(rotation.find('y').text)
        rotation_z = float(rotation.find('z').text)
        
        position_x = position.find('x').text
        position_y = position.find('y').text
        position_z = position.find('z').text

        look_x = look_at_point.find('x').text
        look_y = look_at_point.find('y').text
        look_z = look_at_point.find('z').text

        magnitude = math.sqrt(rotation_x**2 + rotation_y**2 + rotation_z**2)

        unit_vector = rotation_x/magnitude, rotation_y/magnitude, rotation_z/magnitude

        pitch = math.asin(unit_vector[1])  # arcsin(y)
        yaw = math.atan2(unit_vector[0], unit_vector[2])  # arctan(x/z)

        pitch_degrees = math.degrees(pitch)
        yaw_degrees = math.degrees(yaw)

        print(f'pitch : {pitch_degrees}, yaw : {yaw_degrees}')

        height, width = img.shape[:2]

        center_x = width // 2
        center_y = height // 2

        arrow_length = 80

        # end_x3 = int(center_x + arrow_length * np.sin(rotation_x)* np.cos(rotation_y))
        # end_y3 = int(center_y - arrow_length * np.sin(rotation_y))
        end_x2 = int(center_x + arrow_length * np.sin(yaw))
        end_y2 = int(center_y - arrow_length * np.sin(pitch))


        
        # cv2.arrowedLine(img, (center_x, center_y), (end_x3, end_y3), (0, 0, 255), 2)
        cv2.arrowedLine(img, (center_x, center_y), (end_x2, end_y2), (0, 255, 0), 2)

        poi_left = root2.find('POILeft')
        poi_right = root2.find('POIRight')

        poi_left_poi_def = poi_left.find('POIDef')
        poi_right_poi_def = poi_right.find('POIDef')

        

        for i in poi_left_poi_def:
            points_left = poi_left_poi_def.find(f'{i.tag}')
            points_right = poi_right_poi_def.find(f'{i.tag}')

            # print(points_left.tag)

            if points_left.tag in ['Caruncle','InteriorMargin','Iris','Pupil']:
                for k in points_left:
                    p2_left = points_left.find(k.tag)
                    p2_right = points_right.find(k.tag)
                    p3_left = points_left.find(k.tag)
                    p3_right = points_right.find(k.tag)

                    if '2D' in p2_left.tag or '2D' in p2_right.tag:
                        v2_lefts = p2_left.findall('Vector2')
                        v2_rights = p2_right.findall('Vector2')
                        for v2_left,v2_right in zip(v2_lefts,v2_rights):
                            v2_left_x = float(v2_left.find('x').text)
                            v2_left_y = float(v2_left.find('y').text)
                            v2_right_x = float(v2_right.find('x').text)
                            v2_right_y = float(v2_right.find('y').text)


                            cv2.circle(img, (int(v2_left_x), int(v2_left_y)), 2, (0, 0, 255), -1)
                            cv2.circle(img, (int(v2_right_x), int(v2_right_y)), 2, (0, 0, 255), -1)
                            
                    else :
                        v3_lefts = p3_left.findall('Vector3')
                        v3_rights = p3_right.findall('Vector3')
                        for v3_left,v3_right in zip(v3_lefts,v3_rights):
                            v3_left_x = float(v3_left.find('x').text)
                            v3_left_y = float(v3_left.find('y').text)
                            v3_left_z = float(v3_left.find('z').text)
                            v3_right_x = float(v3_right.find('x').text)
                            v3_right_y = float(v3_right.find('y').text)
                            v3_right_z = float(v3_right.find('z').text)
                            
            elif '2D' in points_left.tag or '2D' in points_right.tag:
                if points_left.tag == 'IrisCenter2D':
                    # Iris_center_left = points_left.find('IrisCenter2D')
                    # Iris_center_right = points_right.find('IrisCenter2D')
                    Iris_center_left_x = float(points_left.find('x').text)
                    Iris_center_left_y = float(points_left.find('y').text)
                    Iris_center_right_x = float(points_right.find('x').text)
                    Iris_center_right_y = float(points_right.find('y').text)
                elif points_left.tag == 'PupilCenter2D':
                    # pupil_center_left = points_left.find('PupilCenter2D')
                    # pupil_center_right = points_right.find('PupilCenter2D')
                    pupil_center_left_x = float(points_left.find('x').text)
                    pupil_center_left_y = float(points_left.find('y').text)
                    pupil_center_right_x = float(points_right.find('x').text)
                    pupil_center_right_y = float(points_right.find('y').text)
                elif points_left.tag == 'GlobeCenter2D':
                    # globe_center_left = points_left.find('GlobeCenter2D')
                    # globe_center_right = points_right.find('GlobeCenter2D')
                    globe_center_left_x = float(points_left.find('x').text)
                    globe_center_left_y = float(points_left.find('y').text)
                    globe_center_right_x = float(points_right.find('x').text)
                    globe_center_right_y = float(points_right.find('y').text)

                    gaze_vector_x_right = globe_center_right_x - pupil_center_right_x
                    gaze_vector_y_right = globe_center_right_y - pupil_center_right_y
                    gaze_vector_x_left = globe_center_left_x - pupil_center_left_x
                    gaze_vector_y_left = globe_center_left_y - pupil_center_left_y

                    gaze_vector_right = (gaze_vector_x_right, gaze_vector_y_right)
                    gaze_vector_left = (gaze_vector_x_left, gaze_vector_y_left)
                    
                    gaze_angle_right = math.atan2(gaze_vector_right[1], gaze_vector_right[0])
                    gaze_angle_left = math.atan2(gaze_vector_left[1], gaze_vector_left[0])

                    gaze_angle_right = math.degrees(gaze_angle_right)
                    gaze_angle_left = math.degrees(gaze_angle_left)

                    print(f'gaze_angle_right : {gaze_angle_right}, gaze_angle_left : {gaze_angle_left}')

                    cv2.arrowedLine(img, (int(globe_center_right_x), int(globe_center_right_y)), (int(pupil_center_right_x), int(pupil_center_right_y)), (255, 0, 0), 2)
                    cv2.arrowedLine(img, (int(globe_center_left_x), int(globe_center_left_y)), (int(pupil_center_left_x), int(pupil_center_left_y)), (255, 0, 0), 2)
                    
                    
                # for k in points_left:
                #     points_left_x = float(points_left.find('x').text)
                #     points_left_y = float(points_left.find('y').text)
                #     points_right_x = float(points_right.find('x').text)
                #     points_right_y = float(points_right.find('y').text)
                    
                #     cv2.circle(img, (int(points_left_x), int(points_left_y)), 2, (0, 0, 255), -1)
                #     cv2.circle(img, (int(points_right_x), int(points_right_y)), 2, (0, 0, 255), -1)

            elif '3D' in points_left.tag or '3D' in points_right.tag:
                print(points_left.tag, points_right.tag)
                # for k in points_right:
                #     points_left_x = float(points_left.find('x').text)
                #     points_left_y = float(points_left.find('y').text)
                #     points_left_z = float(points_left.find('z').text)
                #     points_right_x = float(points_right.find('x').text)
                #     points_right_y = float(points_right.find('y').text)
                #     points_right_z = float(points_right.find('z').text)


        

        img = cv2.resize(img, (1280, 960))
        cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    
