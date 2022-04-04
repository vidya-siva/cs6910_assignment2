# -*- coding: utf-8 -*-
"""PartA-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oNRyg8qz0XpHL27uw5DhBqlKoBUTQ4u6
"""



# Commented out IPython magic to ensure Python compatibility.
#Importing all the packages
from numpy import unique, argmax
# %tensorflow_version 2.x
import tensorflow as tf
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten, Dropout, Activation, Rescaling,BatchNormalization
from tensorflow.keras.utils import plot_model
from tensorflow.keras.preprocessing import image_dataset_from_directory
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from tensorflow.keras import layers
import timeit
from matplotlib import pyplot
import matplotlib.pyplot as plt
import numpy as np
import cv2 
import os
import random
import pickle
from PIL import Image
import pathlib,wandb


path = os.path.dirname(os.getcwd())
print(path)
model = tf.keras.models.load_model(pathlib.Path(path + '/contents/DLAssignment2PartA_best_model'))
train_dir =path + "/inaturalist_12K/train"
testDataDir = path + "/inaturalist_12K/val"

testData = tf.keras.preprocessing.image_dataset_from_directory(
                      directory = testDataDir,
                      labels = 'inferred',  
                      label_mode = 'categorical',
                      color_mode = 'rgb',
                      batch_size = 32,
                      image_size = (256, 256),
                      shuffle = False,
                      seed = 17,
                      validation_split = 0)

print('Number of Batches',len(testData))

# Evaluating the model on the test set

print('Evaluating... Sit back and relax')
result = model.evaluate(testData)
print(result)
print(model.metrics_names)

wandb.init()


print('Plotting 10X3 grid with original label and the predicted value')
# Plotting 10 * 3 grid  
labels = sorted(os.listdir(testDataDir))
print('labels : ',labels)
classCount = 0
# Choosing images from all ten classes
batches= [1, 9, 11, 15, 21, 31, 35, 41, 43, 51]
fig, ax = plt.subplots(10, 3, figsize = (15, 60))
for bc, (data, label) in enumerate(testData):
    if bc in batches:
        ax[classCount, 0].set(ylabel = '{}\n(true label)'.format(labels[classCount]))
        for i in range(3):
            predicted_lab = labels[np.argmax(model.predict(np.array(data[i,:,:,:]).reshape(1, 256, 256, 3)))]
            ax[classCount, i].imshow(np.array(data[i,:,:,:], dtype = np.int32))
            ax[classCount, i].set_title('\n\n\n\n{}\n(predicted)'.format(predicted_lab))
            ax[classCount, i].set_yticklabels([])
            ax[classCount, i].set_xticklabels([])
        classCount += 1
    bc += 1

wandb.log({'img': [wandb.Image(fig)]})

model_first_conv = tf.keras.models.Model(inputs = model.inputs, outputs = model.layers[2].output) #Taking the output of the first convolution layer
ranBatch, ranImg = np.random.randint(50), np.random.randint(12) # Random image from test dataset
print(ranBatch, ranImg)
visualizeImage = np.array((256, 256, 3))
for batch_ind, (data, _) in enumerate(testData):
    if batch_ind == ranBatch:
        visualizeImage = np.array(data[ranImg,:,:,:])

print(visualizeImage.shape)
filter_visualize = np.array(model_first_conv.predict(np.array(visualizeImage).reshape(1,256,256,3)))
print(filter_visualize.shape)
fig, ax = plt.subplots(8, 8, figsize = (40, 40))
for filter_num in range(64):
    ax[int(filter_num/8), filter_num%8].imshow(filter_visualize[0,:,:,filter_num])
    ax[int(filter_num/8), filter_num%8].set_yticklabels([])
    ax[int(filter_num/8), filter_num%8].set_xticklabels([])

wandb.log({'Original Image': [wandb.Image(visualizeImage)]})
wandb.log({'Visualized filters for first convolution layer': [wandb.Image(fig)]})
