# -*- coding: utf-8 -*-
"""CNN-YOLO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jlsvAcwRQTUcTiI19qSwBOCktrpWNrYg
"""

!pip install imageai
!pip install tensorflow==2.8.0

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow 
from imageai.Detection.Custom import CustomObjectDetection, CustomVideoObjectDetection
from imageai.Detection import ObjectDetection,VideoObjectDetection
import os

# execution_path = os.getcwd()
#@markdown Mention the path of the directory.
#@markdown  Make sure yolo.h5 is available in this directory. 
execution_path = '/content/drive/MyDrive' #@param {type:'string'}


def imageDetection():
  detector = ObjectDetection()
  detector.setModelTypeAsYOLOv3()
  detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
  detector.loadModel()
  # detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "traffic-light.jpg"), output_image_path=os.path.join(execution_path , "image2new.jpg"), minimum_percentage_probability=30)
  custom_objects = detector.CustomObjects(car=True, motorcycle=True,bus=True,  truck=True,person=True,  bicycle=True)
  detections = detector.detectCustomObjectsFromImage(custom_objects=custom_objects, input_image=os.path.join(execution_path , "traffic-light.jpg"), output_image_path=os.path.join(execution_path , "image3custom.jpg"), minimum_percentage_probability=30)
  for eachObject in detections:
      print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
      print("--------------------------------")

def videoDection():
  detector = VideoObjectDetection()
  detector.setModelTypeAsYOLOv3()
  detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
  detector.loadModel()

  video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "Traffic-20581.mp4"),
                                  output_file_path=os.path.join(execution_path, "traffic_detected")
                                  , frames_per_second=20, log_progress=True)
  print(video_path)

