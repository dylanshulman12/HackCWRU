import tensorflow as tf
import numpy as np
import json 
from PIL import Image 
import os

'''
Input: File Name for Image (String)
Output: Dictionary containing information about plastic type, confidence level, 
array containing probabilities of the others (JSON)
'''
def plastic_model_predict(image_path):
    model = tf.keras.models.load_model("plastic_classifier_model.keras")

    with open("class_names_plastics.json", "r") as f: 
        class_names = json.load(f)

    image = Image.open(image_path).convert("RGB")
    image = image.resize((200, 200))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)

    logits = model.predict(image)[0]
    predictions = tf.nn.softmax(logits).numpy()

    class_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    PLASTICS_THRESHOLD = 0.45

    if confidence > PLASTICS_THRESHOLD:
        data = {
            "predicted_class": class_names[class_index],
            "confidence": confidence,
            "probabilities": {
                class_names[i]: float(predictions[i])
                for i in range(len(class_names))
            }
        }
        
    else:
        data = {
            "predicted_class": "We're not sure, but it might be " + class_names[class_index],
            "confidence": confidence,
            "probabilities": {
                class_names[i]: float(predictions[i])
                for i in range(len(class_names))
            }
        }
    
    return data
# json with what it is, confidence, weights 

'''
Input: File Name for Image (String)
Output: Dictionary containing information about material, confidence level, 
array containing probabilities of the others (JSON)
'''
def material_model_predict(image_path):
    model = tf.keras.models.load_model("material_classifier_model.keras")

    with open("class_names_materials.json", "r") as f: 
        class_names = json.load(f)

    image = Image.open(image_path).convert("RGB")
    image = image.resize((200, 200))
    image = np.array(image)
    image = np.expand_dims(image, axis=0)

    logits = model.predict(image)[0]
    predictions = tf.nn.softmax(logits).numpy()

    class_index = int(np.argmax(predictions))
    confidence = float(np.max(predictions))

    MATERIALS_THRESHOLD = 0.45

    if confidence > MATERIALS_THRESHOLD:
        data = {
            "predicted_class": class_names[class_index],
            "confidence": confidence,
            "probabilities": {
                class_names[i]: float(predictions[i])
                for i in range(len(class_names))
            }
        }
    else:
         data = {
            "predicted_class": "We're not sure, but we think it might be " + class_names[class_index],
            "confidence": confidence,
            "probabilities": {
                class_names[i]: float(predictions[i])
                for i in range(len(class_names))
            }
        }
        

    return data    






