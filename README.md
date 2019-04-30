# Yolov3-convertor
* Convert Pascal VOC and COCO annotation xml file to yolo-darknet training file format. 
* Extract person class from Pascal VOC data set and COCO data set.
## Pascal VOC
#### Get Pascal VOC data set
 To train YOLO you will need all of the VOC data from 2007 and 2012. You can find links to the data https://pjreddie.com/projects/pascal-voc-dataset-mirror/ . Or you can run:
```
wget https://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar
wget https://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar
wget https://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar
tar xf VOCtrainval_11-May-2012.tar
tar xf VOCtrainval_06-Nov-2007.tar
tar xf VOCtest_06-Nov-2007.tar
```
 There will now be a ```VOCdevkit/subdirectory``` with all the VOC training data in it.
#### Extract person class
 In ```yolo_voc/```
run:
```
extract_person_2007.py
extract_person_2012.py
```
#### Generate labels for yolo
 Now we need to generate the label files that Darknet uses. Darknet wants a .txt file for each image with a line for each ground truth object in the image that looks like:

 ```<object-class> <x> <y> <width> <height>```

 Where x, y, width, and height are relative to the image’s width and height. To generate these file by running in ```yolo_voc/```: 
```
voc_label.py
```
 This script will generate lots of label files in ```VOCdevkit/VOC2007/labels``` and ```VOCdevkit/VOC2012/labels```. It also generates the text files like ```2007_train.txt``` list the images files for that year and image set. Darknet needs one text file with all of the images you want to train on. 

 Then you will get a directory whose structure like this:
```
└── VOCdevkit
    ├── VOC2007
    │   ├── Annotations
    │   ├── ImageSets
    │   │   └── Main
    │   ├── JPEGImages                                                 #images 
    │   ├── labels                                                     #annotations in  yolo format
    └── VOC2012
        ├── Annotations
        ├── ImageSets
        │   ├── Action
        │   └── Main
        ├── JPEGImages
        ├── labels
```
## MS COCO 2014
#### Get COCO data
 Download data set from: http://cocodataset.org/#overview
#### Install coco tools
##### For Linux:
```git clone https://github.com/cocodataset/cocoapi```
To install:
* For Matlab, add coco/MatlabApi to the Matlab path (OSX/Linux binaries provided)
* For Python, run "make" under coco/PythonAPI
##### For windows:
```git clone  https://github.com/philferriere/cocoapi```

run:
```
PythonAPI/setup.py
PythonAPI/pycocotools/coco.py
```
#### Extract person class
put ```coco_convert/extract_person.py``` to ```PythonAPI/pycocotools/``` this``` extract_person.py``` is different from the VOC one. After running this program we will get the annotations in VOC format. Then run ```coco_convert/list.py``` to get a txt file which has all of the paths of images we want to train on or validate. 
#### Generate labels for yolo
Run ```coco_convert/voc_label.py``` to convert .xml format to the labels for yolo. This program is different from the VOC one.

Directory structure of coco data set:
```

└── COCO
    ├── images                                                            #images
    │   ├── train2014
    │   ├── val2014
    └── labels                                                            #annotations in  yolo format
        ├── train2014
        ├── val2014
```
 
