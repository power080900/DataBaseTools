import os
import json
import xml.etree.ElementTree as ET

label_dir = 'Z:\\DataVoucher2023_seatbelt\\data\\IR\\labeldata'
label_ids = os.listdir(label_dir)

for label_id in label_ids:
    id_dir = os.path.join(label_dir, label_id)
    label_files = os.listdir(id_dir)

    for label_file in label_files:
        if os.path.basename(label_file).split('.')[-1] == 'xml':
            xml_file = os.path.join(id_dir, label_file)
            
            # XML 파일을 문자열로 읽기
            with open(xml_file, 'r', encoding='utf-8') as file:
                xml_content = file.read()
            
            root = ET.fromstring(xml_content)
            polygon = root.find('.//polygon')  # 경로를 명확히 지정
            # print(polygon)
            if polygon is not None:
                points = polygon.get('points')
                points_list = points.split(';')
                points_tuple_list = [tuple(map(float, point.split(','))) for point in points_list]
                
                json_file = xml_file.replace('.jpg.xml', '.json')
                json_new_file = xml_file.replace('.jpg.xml', '_new.json')
                
                with open(json_file, 'r', encoding='utf-8') as f:
                    existing_json_data = json.load(f)
                
                # 기존 JSON 데이터에 새로운 데이터 추가
                existing_json_data["ObjectInfo"]["Seatbelt"] = {
                    "Label": polygon.get('label'),
                    "Occluded": polygon.get('occluded') == "1",
                    "Source": polygon.get('source'),
                    "Points": points_tuple_list,
                    "Z_Order": int(polygon.get('z_order'))
                }
                
                # JSON 파일 저장
                with open(json_new_file, 'w', encoding='utf-8') as f:
                    json.dump(existing_json_data, f, indent=4)
                os.remove(json_file)
                os.remove(xml_file)

                print(f'{json_file} -> {json_new_file}')




