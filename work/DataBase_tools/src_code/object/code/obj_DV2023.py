import os
import pandas as pd
import xml.etree.ElementTree as ET

# <image id="0" name="01_frame_00043.jpg" width="1280" height="1024">
#     <box label="bending">
#     </box>
#     <box label="glasses" occluded="0" source="manual" xtl="214.35" ytl="515.40" xbr="642.50" ybr="726.50" z_order="0">
#     </box>
#     <box label="face" occluded="0" source="manual" xtl="247.92" ytl="568.38" xbr="636.10" ybr="942.25" z_order="0">
#     </box>
#   </image>

root_dir = 'Z:\\DataVoucher2023_driver_act\\data\\drive_act\\data\\IR\\labeldata'
ids = os.listdir(root_dir)

df = pd.DataFrame(columns = ['label','object'])
df1 = pd.DataFrame(columns = ['label','object'])

for id_ in ids:
    print(id_)
    sai_file_path = os.path.join(root_dir, id_)
    sai_file = os.listdir(sai_file_path)
    for num, file in enumerate(sai_file):
        print(num,'/',len(sai_file))
        tree = ET.parse(os.path.join(sai_file_path, file))
        root = tree.getroot()
        labels = []
        for box in root.findall('.//box'):
            # 'label' 외에 다른 속성이 없는지 확인
            if len(box.attrib) == 1 and 'label' in box.attrib:
                labels.append(box.get('label'))

        # 추출한 label 값 출력
        for object in labels:
            df1.loc[len(df1)] = [file, object]
                
    df = pd.concat([df, df1])
        
    df.to_csv(f'obj_DV2023_{id_}.csv', index=False)
    df1 = pd.DataFrame(columns = ['label','object'])
    
        
for id_ in ids:
    file_pattern = f"obj_DV2023_{id_}.csv"

    dataframes = []
    df = pd.read_csv(file_pattern)
    dataframes.append(df)

    combined_df = pd.concat(dataframes, ignore_index=True)
combined_df.to_csv("obj_DV2023.csv", index=False)
