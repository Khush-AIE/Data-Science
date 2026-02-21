# # !pip install streamlit

import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import cv2


# def predict_tumor(pil_image):
#     model = tf.keras.models.load_model(
#         r"C:\Users\ADMIN\Downloads\DATA SCIENCE COURSE\Deep Learning\Brain Tumor Detection\Best_models.keras"
#     )

#     class_names = ['GLIOMA', 'MENINGIOMA', 'NO TUMOR', 'PITUITARY']

#     # Convert PIL image → NumPy array
#     img = np.array(pil_image)

#     # Ensure RGB
#     img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
#     img = cv2.resize(img, (224, 224))  #resize
#     img = img / 255.0               #normalize
#     img = np.expand_dims(img, axis=0)  #to make dimensions same so that all have same dimensions

#     predictions = model.predict(img)
#     pred_class = np.argmax(predictions)
#     confidence = float(np.max(predictions) * 100)

#     tumor_type = class_names[pred_class]

#     if tumor_type == 'NO TUMOR':
#         tumor_status = 'No Tumor Detected'
#     else:
#         tumor_status = 'Tumor Detected'

#     return tumor_status, tumor_type, round(confidence, 2)


import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
from PIL import Image

# --------------------------------------------------
# Page config
# --------------------------------------------------

def app():
    st.set_page_config(
        page_title="Brain Tumor MRI Detection",
        layout="centered"
    )

    st.title("🧠 Brain Tumor MRI Detection")
    st.write("Deep Learning based MRI Classification")

    # --------------------------------------------------
    # Load model ONCE (important for performance)
    # --------------------------------------------------
    @st.cache_resource
    def load_model():
        return tf.keras.models.load_model(
            r"C:\Users\ADMIN\Downloads\DATA SCIENCE COURSE\Deep Learning\Brain Tumor Detection\Best_models.keras"
        )

    model = load_model()

    # Class labels (must match training order)
    CLASS_NAMES = ['GLIOMA', 'MENINGIOMA', 'NO TUMOR', 'PITUITARY']

    # --------------------------------------------------
    # Prediction function
    # --------------------------------------------------
    def predict_tumor(pil_image):
        # Convert PIL image to NumPy array
        img = np.array(pil_image)

        # Convert RGB → BGR (OpenCV format)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        # Resize to model input size
        img = cv2.resize(img, (224, 224))

        # Normalize
        img = img / 255.0

        # Add batch dimension
        img = np.expand_dims(img, axis=0)

        # Predict
        predictions = model.predict(img)
        pred_class = np.argmax(predictions)
        confidence = float(np.max(predictions) * 100)

        tumor_type = CLASS_NAMES[pred_class]

        if tumor_type == 'NO TUMOR':
            tumor_status = "No Tumor Detected"
        else:
            tumor_status = "Tumor Detected"

        return tumor_status, tumor_type, round(confidence, 2)

    # --------------------------------------------------
    # Streamlit UI
    # --------------------------------------------------
    uploaded_file = st.file_uploader(
        "Upload MRI Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded MRI Image", use_column_width=True)

        if st.button("Predict",type='secondary'):
            with st.spinner("Analyzing MRI..."):
                tumor_status, tumor_type, confidence = predict_tumor(image)

            st.subheader("🧪 Prediction Result")
            st.success(tumor_status)
            st.write(f"**Tumor Type:** {tumor_type}")
            st.write(f"**Confidence:** {confidence}%")
