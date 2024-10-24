import numpy as np
import zipfile
import cv2 
import os
import sys
sys.path.append("../")
import data_processing_core as dpc

root = "Z:\\UTMULTIVIEW\\org_data\\UT"
out_root = "Z:\\UTMULTIVIEW\\data"
scale =True

def ImageProcessing_UT():
    persons = os.listdir(root)
    persons.sort()

    for person in persons:
        im_root = os.path.join(root, person, "synth")
        im_outpath = os.path.join(out_root, "rawdata", person, "synth")
        label_outpath = os.path.join(out_root, "labeldata", 'synth', f"{person}.label")

        if not os.path.exists(im_outpath):
            os.makedirs(im_outpath)
        if not os.path.exists(os.path.join(out_root, "labeldata", 'synth')):
            os.makedirs(os.path.join(out_root, "labeldata", 'synth'))

        header = os.path.join(person, 'synth')
        print(f"Start Processing {person}_synth")
        ImageProcessing_Person(im_root, im_outpath, label_outpath, header)

        im_root = os.path.join(root, person, "test")
        im_outpath = os.path.join(out_root, "rawdata", person, "test")
        label_outpath = os.path.join(out_root, "labeldata", 'test', f"{person}.label")

        if not os.path.exists(im_outpath):
            os.makedirs(im_outpath)
        if not os.path.exists(os.path.join(out_root, "labeldata", 'test')):
            os.makedirs(os.path.join(out_root, "labeldata", 'test'))

        header = os.path.join(person, 'test')
        print(f"Start Processing {person}_test")
        ImageProcessing_Person(im_root, im_outpath, label_outpath, header)



def ImageProcessing_Person(root, im_outpath, label_outpath, header):
    files = os.listdir(root)
    image_zips = [name for name in files if "zip" in name]
    label_csvs = [name for name in files if "csv" in name]
    image_zips.sort()
    label_csvs.sort()

    outfile = open(label_outpath, 'w')
    outfile.write("Image Origin WhichEye 3DGaze 3DHead 2DGaze 2DHead\n")
   
    for image_zip in image_zips:
        name = image_zip.split(".")[0]
        first_num, which_eye = name.split("_")

        if which_eye == 'right':
            continue

        first_num = int(first_num)

        image_datas = zipfile.ZipFile(os.path.join(root, image_zip))
        image_names = image_datas.namelist()
        image_names.sort()

        with open(os.path.join(root, name + ".csv")) as infile:

            annotations = infile.readlines()

        for image_name in image_names:

            second_num = int(image_name.split(".")[0])
            datas = image_datas.read(image_name)

            order = (first_num + (which_eye=="right")) * 144 + second_num + 1

            progressbar = "".join(["\033[41m%s\033[0m" % '   '] * int(order/(144*160) * 20))
            progressbar = "\r" + progressbar + f" {order}|{144*160}"
            print(progressbar, end = "", flush=True)

            annotation = annotations[second_num].strip().split(",")
            gaze = np.array(annotation[0:3]).astype("float")
            head = np.array(annotation[3:6]).astype("float")

                 
            with open(os.path.join(out_root, f"temp.jpg"), 'wb') as out:
                out.write(datas)

            img = cv2.imread(os.path.join(out_root, "temp.jpg"))

            if which_eye == "right":
                img = cv2.flip(img, 1)
                gaze = dpc.GazeFlip(gaze)
                head = dpc.HeadFlip(head)

            cv2.imwrite(os.path.join(im_outpath, f"{order}.jpg"), img)
            gaze_2d = dpc.GazeTo2d(gaze)
            head_2d = dpc.HeadTo2d(head)
        
            save_name = os.path.join(header, f"{order}.jpg")
            save_origin = f"{first_num}_{second_num}.bmp"
            save_flag = which_eye
            save_gaze = ",".join(gaze.astype("str"))
            save_head = ",".join(head.astype("str"))
            save_gaze2d = ",".join(gaze_2d.astype("str"))
            save_head2d = ",".join(head_2d.astype("str"))

            save_str = " ".join([save_name, save_origin, save_flag, save_gaze, save_head, save_gaze2d, save_head2d])
        
            outfile.write(save_str + "\n")
    print("")
    outfile.close()

def AnnoDecode(anno_info):
	annotation = np.array(anno_info.strip().split(" ")).astype("float32")
	out = {}
	out["left_left_corner"] = annotation[0:2]
	out["left_right_corner"] = annotation[6:8]
	out["right_left_corner"] = annotation[12:14]
	out["right_right_corner"] = annotation[18:20]
	out["headrotvectors"] = annotation[29:32]
	out["headtransvectors"] = annotation[32:35]
	out["rightcenter"] = annotation[35:38]
	out["leftcenter"] = annotation[38:41]
	out["target"] = annotation[26:29]
	return out


if __name__ == "__main__":
    ImageProcessing_UT()
