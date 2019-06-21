# -*- coding: utf-8 -*-

import os
import shutil

ann_filepath = '/home/xi/MobileNet-YOLO/data/VOCdevkit/VOC2012/Annotations/'
img_filepath = '/home/xi/MobileNet-YOLO/data/VOCdevkit/VOC2012/JPEGImages/'
img_savepath = '/home/xi/MobileNet-YOLO/data/VOC0712/newperson2012/'
ann_savepath = '/home/xi/MobileNet-YOLO/data/VOC0712/newanotation2012/'
if not os.path.exists(img_savepath):
    os.mkdir(img_savepath)

if not os.path.exists(ann_savepath):
    os.mkdir(ann_savepath)
names = locals()
classes = ['person']

for file in os.listdir(ann_filepath):
    print(file)

    fp = open(ann_filepath + '//' + file)  # Open then Annotations file
    ann_savefile = ann_savepath + file
    fp_w = open(ann_savefile, 'w')
    lines = fp.readlines()

    ind_start = []
    ind_end = []
    lines_id_start = lines[:]

    lines_id_end = lines[:]

    classes1 = '\t\t<name>person</name>\n'
    # Find the object block in xml and record it
    while "\t<object>\n" in lines_id_start:
        a = lines_id_start.index("\t<object>\n")
        ind_start.append(a)  # ind_start是<object>的行数
        lines_id_start[a] = "delete"

    while "\t</object>\n" in lines_id_end:
        b = lines_id_end.index("\t</object>\n")
        ind_end.append(b)  # ind_end是</object>的行数
        lines_id_end[b] = "delete"

    # Store all object blocks in names
    i = 0
    for k in range(0, len(ind_start)):
        names['block%d' % k] = []
        for j in range(0, len(classes)):
            if classes[j] in lines[ind_start[i] + 1]:
                a = ind_start[i]
                for o in range(ind_end[i] - ind_start[i] + 1):
                    names['block%d' % k].append(lines[a + o])
                break
        i += 1
        # print(names['block%d' % k])

    # xml header
    string_start = lines[0:ind_start[0]]

    # xml tail
    if ((file[2:4] == '09') | (file[2:4] == '10') | (file[2:4] == '11')):
        string_end = lines[(len(lines) - 11):(len(lines))]
    else:
        string_end = [lines[len(lines) - 1]]

        # Search in the given class at the end of the xml, if it exists, write the object block information
    a = 0
    for k in range(0, len(ind_start)):
        if classes1 in names['block%d' % k]:
            a += 1
            string_start += names['block%d' % k]
    string_start += string_end
    # print(string_start)
    for c in range(0, len(string_start)):
        fp_w.write(string_start[c])
    fp_w.close()
    # If there is no module we are looking for, delete this xml, if any, copy the image
    if a == 0:
        os.remove(ann_savepath + file)
    else:
        name_img = img_filepath + os.path.splitext(file)[0] + ".jpg"
        shutil.copy(name_img, img_savepath)
    fp.close()