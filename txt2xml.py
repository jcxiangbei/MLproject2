# encoding = utf-8
import os
import numpy as np
import codecs
import cv2
cover={
    "带电芯充电宝":"ele",
    "不带电芯充电宝":"not",
}

def read_txt(label_path):
    file = open(label_path, 'r', encoding='utf-8')
    label_lines = file.readlines()
    label = []
    for line in label_lines:
        xx=line[:-1].split(" ")
        label.append(xx)

        #one_line = float(line.strip().split('\n')[0])
        #label.extend([one_line])
    return label


def covert_xml(label, xml_path, img_name, img_path):
    # 获得图片信息
    img = cv2.imread(img_path)
    height, width, depth = img.shape


    xml = codecs.open(xml_path, 'w', encoding='utf-8')
    xml.write('<annotation>\n')
    xml.write('\t<folder>' + 'VOC2007' + '</folder>\n')
    xml.write('\t<filename>' + img_name + '</filename>\n')
    xml.write('\t<source>\n')
    xml.write('\t\t<database>The VOC 2007 Database</database>\n')
    xml.write('\t\t<annotation>Pascal VOC2007</annotation>\n')
    xml.write('\t\t<image>flickr</image>\n')
    xml.write('\t\t<flickrid>NULL</flickrid>\n')
    xml.write('\t</source>\n')
    xml.write('\t<owner>\n')
    xml.write('\t\t<flickrid>NULL</flickrid>\n')
    xml.write('\t\t<name>faster</name>\n')
    xml.write('\t</owner>\n')
    xml.write('\t<size>\n')
    xml.write('\t\t<width>' + str(width) + '</width>\n')
    xml.write('\t\t<height>' + str(height) + '</height>\n')
    xml.write('\t\t<depth>' + str(depth) + '</depth>\n')
    xml.write('\t</size>\n')
    xml.write('\t\t<segmented>0</segmented>\n')
    for i in label:
        if(i[1]=="带电芯充电宝" or i[1]=="不带电芯充电宝"):
            xml.write('\t<object>\n')
            xml.write('\t\t<name>' + cover[i[1]] + '</name>\n')
            xml.write('\t\t<pose>Unspecified</pose>\n')
            xml.write('\t\t<truncated>0</truncated>\n')
            xml.write('\t\t<difficult>0</difficult>\n')
            xml.write('\t\t<bndbox>\n')
            xml.write('\t\t\t<xmin>' + str(i[2]) + '</xmin>\n')
            xml.write('\t\t\t<ymin>' + str(i[3]) + '</ymin>\n')
            xml.write('\t\t\t<xmax>' + str(i[4]) + '</xmax>\n')
            xml.write('\t\t\t<ymax>' + str(i[5]) + '</ymax>\n')
            xml.write('\t\t</bndbox>\n')
            xml.write('\t</object>\n')

    xml.write('</annotation>')


labels_file_path = "F:\\VOCdevkit\\VOC2007\\Annotations"
labels_name = os.listdir(labels_file_path)
with open("F:\\VOCdevkit\\VOC2007\\ImageSets\\Main\\trainval.txt","a") as ff:
    for i in labels_name:
        ff.write(i.split(".")[0]+"\n")



if __name__ == '_main__':
    labels_file_path = "F:\\coreless_3000\\Annotation"
    imgs_file_path = "F:\\coreless_3000\\Image"

    xmls_file_path = "F:\\coreless_3000\\xmls"
    if not os.path.exists(xmls_file_path):
        os.mkdir(xmls_file_path)

    labels_name = os.listdir(labels_file_path)
    for label_name in labels_name:
        label_path = os.path.join(labels_file_path, label_name)
        label = read_txt(label_path)

        xml_name = label_name[:24] + '.xml'
        xml_path = os.path.join(xmls_file_path, xml_name)

        img_name = label_name[:24] + '.jpg'
        img_path = os.path.join(imgs_file_path, img_name)

        covert_xml(label, xml_path, img_name, img_path)
        print(img_name)