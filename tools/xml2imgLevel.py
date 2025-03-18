import xml.etree.ElementTree as ET
import os
from collections import Counter

CLASS_NAME = ("__background__ ", "wbc", "rbc", "platelets")

def xml2imgLevel(xml_file):
    anno = ET.parse(xml_file).getroot()
    classes = []
    for obj in anno.iter("object"):
        name = obj.find("name").text.lower().strip()
        index = CLASS_NAME.index(name)
        classes.append(index)
    counts = Counter(classes)
    sorted_elements = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    txt_file =sorted_elements[0] + " " + sorted_elements[1] + " " + sorted_elements[2]  + " " + sorted_elements[3] + " " + sorted_elements[4]
    return txt_file

if __name__ == "__main__":
    xml_dir = r"D:/1_project\jianzhi\BBCD\BBCD\VOCdevkit2007\VOC2007/Annotations/"
    xml_namelist = os.listdir(xml_dir)
    save_path = r"D:/1_project\jianzhi\BBCD\BBCD\VOCdevkit2007\VOC2007/muti_scene_label/"
    for xml_name in xml_namelist:
        xml_file = os.path.join(xml_dir, xml_name)
        txt_file = xml2imgLevel(xml_file)
        txt_save_path = save_path + xml_name[:-4] + ".txt"
        open(txt_save_path, "w").write(txt_file)
        print(txt_save_path)
