from PIL.Image import Image
import numpy as np
import tensorflow as tf
import requests
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Model
from tensorflow.keras.applications import imagenet_utils
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import random
import matplotlib.pyplot as plt
from io import BytesIO

class MobileNetImplementation:

    def __init__(self) -> None:
        self.mobile = tf.keras.applications.mobilenet.MobileNet()

    def prepare_image(self, pil_image):
        img_array = image.img_to_array(pil_image)
        img_array_expanded_dims = np.expand_dims(img_array, axis=0)
        return tf.keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)

    def pil_from_url(self,url):
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        image.resize(224,224)
        return image
    
    def predict_image(self,url):
        image = self.pil_from_url(url)
        processed_image = self.prepare_image(image)
        predictions = self.mobile.predict(processed_image)
        results = imagenet_utils.decode_predictions(predictions)
        return results