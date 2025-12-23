# !pip install streamlit

import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

model = load_model("C:/Users/ADMIN/Downloads/DATA SCIENCE COURSE/Deep Learning/Brain Tumor Detection/Best_models.keras")

class_names = ["glioma","meningioma","no tumor","pituitary"]

st.title("....Brain Tumor MRI Identification....")


file = st.file_uploader("Upload an image to classify the MRI for brain..",
                        type=["jpg","jpeg","png"])

if file:
    image = Image.open(file).convert("RGB")
    st.image(image,caption="Uploaded MRI",use_container_width=True)

    image = image.resize((224,224))
    img_array = np.array(image)/255
    img_array = np.expand_dims(img_array,axis=0)

    prediction = model.predict(img_array)
    predicted_index = np.argmax(prediction)
    predicted_class = class_names[predicted_index]

    if predicted_class == "no tumor":
        st.success("No Tumor :)")
    else:
        st.error(f"Tumor detected:{predicted_class}")