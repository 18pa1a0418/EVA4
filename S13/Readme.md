
# S13

## Team Members
* B Sridevi - sridevi.b@vishnu.edu.in
* Abhinav Dayal - abhinav.dayal@vishnu.edu.in
* A. Lakshmana Rao - 18pa1a0511@vishnu.edu.in
* Sanjay Varma G - 18pa1a1211@vishnu.edu.in


## part - A
*. In the part-A we implemented yolo with OpenCV framework. For thois we need weights file,coco names file and configuration files.[This](https://github.com/Lakshman511/EVA4/blob/master/S13/S13A/Eva4_s13_A_OpenCV_Yolo.ipynb) is the link to colab notebook where we implemented yolo using opencv framework.

*. This is the image of me which was annotated by model.



![](https://github.com/Lakshman511/EVA4/blob/master/S13/S13A/download%20(1).png)


## part-B
*. [This](https://github.com/Lakshman511/YoloV3) is the link to repo where our team prepared custom dataset.

YoloV3 Simplified for training on Colab with custom dataset for one class (**GUN**)

_A Collage of Training images_
![image](https://github.com/Lakshman511/YoloV3/blob/master/train_batch0.png)

_A Collage of Testing images_
![image](https://github.com/Lakshman511/YoloV3/blob/master/test_batch0.png)

Class - gun

1. We have added a 500 images of unique object (gun) in the folder customdata after annotating the images using Annotation Tool. The structure we followed to store them is
```
data
  --customdata
    --images/
      --img001.jpg
      --img002.jpg
      --...
    --labels/
      --img001.txt
      --img002.txt
      --...
    custom.data #data file
    custom.names #class name
    customtrain.txt #list of name of the images to train our network.
    customtest.txt #list of names of the images for validation
```
2. For one class example our custom.data is [here](https://github.com/Lakshman511/YoloV3/blob/master/data/customdata/custom.data). We used 500 images for training and 100 images for testng.
2. downloaded the weights (yolov3-spp-ultralytics.pt) from the original ![source](https://drive.google.com/open?id=1LezFG5g3BCW6iYaV89B2i64cqEUZD7e0) and placed in Google Drive. 
3. Created a weights folder under YoloV3 to store weights
4. Trained for 300 epochs after configuring. (log)[https://github.com/Lakshman511/YoloV3/blob/master/results.txt)



**Results**

After training for 300 Epochs, results look awesome!

![image](https://github.com/Lakshman511/YoloV3/blob/master/output/img080.jpg)

![image](https://github.com/Lakshman511/YoloV3/blob/master/output/img082.jpg)

**Performance**

![image](https://github.com/Lakshman511/YoloV3/blob/master/results.png)
