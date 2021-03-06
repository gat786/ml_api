from PIL import Image
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
        try:
            image = Image.open(BytesIO(response.content))
            image = image.resize([224,224])
            return image
        except:
            return False
    
    def predict_image(self,url):
        image = self.pil_from_url(url)
        if image:
            processed_image = self.prepare_image(image)
            predictions = self.mobile.predict(processed_image)
            results = imagenet_utils.decode_predictions(predictions)
            return_dict = []
            for prediction in results[0]:
                prediction_data = {
                    "confidence": float(prediction[2]),
                    "found_item": prediction[1]
                }
                return_dict.append(prediction_data)
            return {"result":return_dict}