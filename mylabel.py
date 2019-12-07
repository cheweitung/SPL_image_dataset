import xml.etree.ElementTree as ET
import os
from os import getcwd

#classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]
#classes = ["little shark", "yellow fish", "green butterfish", "black butterfish", "garbage fish"]
classes = ["0","1","2","3","4","5","6","7","8","9"]
#classes = []

img_folder = '/Users/che-weitung/Documents/uwm/thesis/image'
xml_folder = '/Users/che-weitung/Documents/uwm/thesis/xml_label'
out_file = 'YOLO_train.txt'

def convert_annotation(image_id, list_file, xml_path):
    in_file = open('%s/%s.xml'%(xml_path,image_id))
    tree=ET.parse(in_file)
    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        #cls = ' '.join( cls.split()[:-1] )
        if cls not in classes or int(difficult)==1:
            print('%s in classes'%(cls))
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

def make_list(path):
    imgs_ids=[]
    for dirpath, dirnames, filenames in os.walk(path, topdown=False):
        for filename in filenames:
            if filename.endswith('.jpg'): 
                imgs_ids.append(filename[:-4])
    print(imgs_ids)
    return imgs_ids

#wd = getcwd()

img_path= img_folder
print(img_path)
xml_path= xml_folder
print(xml_path)

image_ids = make_list(img_path)
list_file = open(out_file, 'w')
for image_id in image_ids:
    if os.path.isfile(xml_path+'/'+image_id+'.xml'):
        print(xml_path+'/'+image_id+'.xml')
        list_file.write('%s%s.jpg'%(img_path, image_id))
        convert_annotation(image_id, list_file, xml_path)
        list_file.write('\n')
list_file.close()


