import os
import shutil

# Person class training set, test set address
VOC2007_trainval = 'VOCdevkit/VOC2007/ImageSets/Main/person_trainval.txt'
VOC2007_test = 'VOCdevkit/VOC2007/ImageSets/Main/person_test.txt'

# label adress
VOC2007_label = 'VOCdevkit/VOC2007/ImageSets/Main/'

# image, annotation address
VOC2007_images = 'VOCdevkit/VOC2007/JPEGImages'
VOC2007_annotations = 'VOCdevkit/VOC2007/Annotations'

# Unusable folder to be deleted
FOLDER_TO_DELETE = ['VOCdevkit/VOC2007/SegmentationClass', 'VOCdeckit/VOC2007/SegmentationObject' , 'VOCdevkit/VOC2007/ImageSets/Layout' , 'VOCdevkit/VOC2007/ImageSets/Segmentation']

# Serial number of the picture containing the person class
train_person_index = []
test_person_index = []

# Delete useless folders
def rm_unnecessary_files():
 for file in FOLDER_TO_DELETE:
     if os.path.exists(file):
         shutil.rmtree(file)
 for file in os.listdir(VOC2007_label):
     if 'person' not in file:
         os.remove(os.path.join(VOC2007_label, file))
 print('[0] remove unnecessary files done')

def get_index(dataset_path):
    person_index = []
    with open(dataset_path, 'r') as f:
        line = f.readline()
        while line:
            if line[-3] != '-':
                index = line.split(' ')[0]
                if index not in person_index:
                    person_index.append(index)
            line = f.readline()
        f.close

    person_index.sort()
    print('[1] extract pics: %d'%(len(person_index)))
    return person_index

def write_txt(person_index, label_path):
    with open(os.path.join(VOC2007_label, label_path), 'w') as f:
        for index in person_index:
            line = index + '\n'
            f.write(line)
    f.close
    print(' write lables into txt finished')


if __name__ == '__main__':
    rm_unnecessary_files()
    train_person_index = get_index(VOC2007_trainval)
    write_txt(train_person_index, 'train.txt')

    test_person_index = get_index(VOC2007_test)
    write_txt(test_person_index, 'test.txt')

    print('[2] All is done!')