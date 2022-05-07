# **Real Time Produce Detection and Classification**

This project is the final project for ECGR 4106 Real Time Machine Learning  
The overall goal is to use our knowledge that we gain from the class and implement it into a project.

The objective of this project is to be able to differentiate between different types of produce  
be able to count the number of each type of produce in the basket.   
  
A camera sitting above the basket will be used to feed a model in real-time.  
Then the number of each class will be counted and displayed in the console.  

<p align="center" style="margin-bottom: 0px">
  <img height="300" src="https://raw.githubusercontent.com/nguyjd/real-time-produce-detection-and-classification/main/Results/testingbox.jpg" alt="The box" align="center">
</p>
<p align="center" >Figure 1: The Testing Setup.</p>



## Team Members
- Jonathon Nguyen (Project Manager)
- Jarrett Long

## Environment
This model was trained on windows 10 on a NVIDIA RTX 3080

## How to use our project

Download Weights  
- [Best Weights](https://drive.google.com/file/d/1fhP-F6HGzC1DUOgnTkaoikrXi3hS-R8N/view?usp=sharing)
- [Starting Weights](https://drive.google.com/file/d/1-3MSlHcd1KvawyIfK3KjkZa3d-5HoOct/view?usp=sharing)
- [Weights from 0 to 3000](https://drive.google.com/file/d/1Q3I4_RMS_kyZ2c-qze2U2zYUV7e651hm/view?usp=sharing)
  
If you want to train with the dataset we compliled from the begining.
- Download Starting Weights and place it in the darknet folder.
- Go into the darknet folder
- Double click the start_training.bat file.

If you want to train with the dataset we compliled from the from the weights that we made.
- Download "Weights from 0 to 3000" and place it in the darknet folder.
- Go into the darknet folder
- Open a powershell terminal
- run "darknet.exe detector train data/obj.data yolov4.cfg 'path-to-weights'"

If you want to use the real time portion of the project.
- Move the weights that you want into the root folder.
- Run the python file 'webcam-yolov4.py'
- NOTE: you will need to change the weights it loads on line 14

## Project Results

<p align="center" style="margin-bottom: 0px">
  <img height="400" src="https://raw.githubusercontent.com/nguyjd/real-time-produce-detection-and-classification/main/Results/banana.png" alt="banana" align="center">
</p>
<p align="center" >Figure 2: Single Produce Detection.</p>

<p align="center" style="margin-bottom: 0px">
  <img height="400" src="https://raw.githubusercontent.com/nguyjd/real-time-produce-detection-and-classification/main/Results/All.png" alt="Basket fruit" align="center">
</p>
<p align="center" >Figure 3: Multiple Produce Detection.</p>

<p align="center" style="margin-bottom: 0px">
  <img height="400" src="https://raw.githubusercontent.com/nguyjd/real-time-produce-detection-and-classification/main/mAPGraph.png" alt="banana" align="center">
</p>
<p align="center" >Figure 4: mAP @ 50% IoU.</p>

## Citations
Horea Muresan, Mihai Oltean, Fruit recognition from images using deep learning, Acta Univ. Sapientiae, Informatica Vol. 10, Issue 1, pp. 26-42, 2018.  
Alexey Bochkovskiy, Chien-Yao Wang and Hong-Yuan Mark LiaoS, YOLOv4: Optimal Speed and Accuracy of Object Detection, 2020.  
Alexey Bochkovskiy (2016) Yolo-Mark[Source code] https://github.com/AlexeyAB/Yolo_mark  

- The main dataset: Fruits 360 https://paperswithcode.com/dataset/fruits-360-1
- Network: Yolov4 with darknet https://github.com/AlexeyAB/darknet
- Labeling Tool: https://github.com/AlexeyAB/Yolo_mark  
