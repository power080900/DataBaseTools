import os
import json
import cv2
import pandas as pd

def draw_landmark(image, landmarks, color=(0, 255, 0)):
    for point in landmarks:
        x = int(point['screen_space_pos'][0] * image.shape[1])
        y = int(point['screen_space_pos'][1] * image.shape[0])
        cv2.circle(image, (x, y), 2, color, -1)

root_dir = 'Z:\\SAI\\data\\IR\\labeldata'
img_root_dir = 'Z:\\SAI\\data\\IR\\rawdata'
save_dir = 'C:\\Lee\\work\\Database\\code\\DB_Tools\\datasets\\SAI\\face_check'
id_list = os.listdir(root_dir)
df = pd.DataFrame(columns=['id', 'label', 'point_cnt'])

for id in id_list:
    print()
    print(id)
    label_path = os.path.join(root_dir, id)
    label_list = os.listdir(label_path)
    for num, label in enumerate(label_list):
        total_num = len(label_list)
        progressbar = "".join(["\033[41m%s\033[0m" % '   '] * int(num / total_num * 20))
        progressbar = "\r" + progressbar + f" {num}|{total_num}"
        print(progressbar, end="", flush=True)
        label_file = os.path.join(label_path, label)
        with open(label_file, 'r') as f:
            data = json.load(f)

        image_path = os.path.join(img_root_dir, id, label.replace('.json', '.png').replace('.info', '.rgb'))
        image = cv2.imread(image_path)

        save_file = os.path.join(save_dir, id, label.replace('.json', '.png').replace('.info', '.facelmk'))
        if not os.path.exists(os.path.dirname(save_file)):
            os.makedirs(os.path.dirname(save_file))

        facelmk = data['landmarks']['ibug68']
        point_cnt = len(facelmk)
        if point_cnt != 68:
            print(label_file)
            
        else:
            draw_landmark(image, facelmk)
            cv2.imwrite(save_file, image)
        
#         df.loc[len(df)] = [id, label, point_cnt]


# df.to_csv('face_check.csv', index=False)
# print('Done')
