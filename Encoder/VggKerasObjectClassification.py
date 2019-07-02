#Tensorflow/Keras Libraries:
from keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
#Other Libraries:
import numpy as np
import cv2

#Import VGG  model
model = VGG16()

#Import Image:
img = load_img("TEST5.jpg", target_size = (224, 224))

#Covert image into array:
img = img_to_array(img)

#Reshape array:
img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))

#prepare for model
img = preprocess_input(img)

#Probability of object being one of the classes in the model
yhat = model.predict(img)

#Traslate Predictions
tag = decode_predictions(yhat)

#Get highest prediction
tag = tag[0][0]

#Print classification:
print(tag[1])
print(tag[2]*100)





