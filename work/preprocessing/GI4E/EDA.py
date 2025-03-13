import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
import xml.etree.ElementTree as ET
from glob import glob
from PIL import Image, ImageDraw, ImageFont

data_path = glob(os.path.join(os.getcwd(), "*", "*", "*", "*.xml"))

for path in data_path[:2]:
    dirs = os.path.dirname(path)
    file_name = os.path.basename(path)
    tree = ET.parse(path)
    root = tree.getroot()
    
    

    # head pose
    if file_name == 'many_headpose.xml':
        print()
    #     def_values = root.findall(".//HeadposeDef")
    #     for num, defs in enumerate(def_values):
    #         ro_value = defs.find('Rotation')
    #         ro_x = float(ro_value.find("x").text)
    #         ro_y = float(ro_value.find("y").text)
    #         ro_z = float(ro_value.find("z").text)

    #         po_value = defs.find('Position')
    #         po_x = float(po_value.find("x").text)
    #         po_y = float(po_value.find("y").text)
    #         po_z = float(po_value.find("z").text)

    #         Lo_value = defs.find('LookAtPoint')
    #         Lo_x = float(Lo_value.find("x").text)
    #         Lo_y = float(Lo_value.find("y").text)
    #         Lo_z = float(Lo_value.find("z").text)
                        
    # poi
    elif file_name == 'many_poi_data.xml':
        P_L = root.findall('.//POILeft')
        P_R = root.findall('.//POIRight')

        for i in P_L.attrib:
            print(i)
        
        for i in P_R.attrib:
            print(i)