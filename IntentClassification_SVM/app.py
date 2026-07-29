import os
import streamlit as st
import pickle
import numpy as np
from sentence_transformers import SentenceTransformer


# -----------------------------
# Base Directory
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# -----------------------------
# Load Sentence Transformer
# -----------------------------
embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# -----------------------------
# Load Classifier Model
# -----------------------------
classifier_path = os.path.join(
    BASE_DIR,
    "models",
    "Intentsclassification.pkl"
)


classifier = pickle.load(
    open(classifier_path, "rb")
)


# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Intent Prediction",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# Load CSS
# -----------------------------
css_path = os.path.join(
    BASE_DIR,
    "style.css"
)


with open(css_path, encoding="utf-8") as f:
    css = f.read()


st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)


# -----------------------------
# Title
# -----------------------------
st.title("🤖 Intent Prediction")

st.write(
    "Enter customer message to predict the intent."
)


# -----------------------------
# Input
# -----------------------------
user_input = st.text_area(
    "Customer Message",
    height=200,
    placeholder="Example: I want to check my order status"
)


# -----------------------------
# Cards + Button
# -----------------------------
col1, col2, col3, col4 = st.columns([3,1,1,1])


with col1:

    predict = st.button(
        "Predict Intent"
    )


with col2:

    st.markdown("""
    <div class="mini-card">
        <div class="card-title">99.8%</div>
        <div class="card-subtitle">
            Model Accuracy
        </div>
    </div>
    """, unsafe_allow_html=True)



with col3:

    st.markdown("""
    <div class="mini-card">
        <div class="card-title">
            Sentence-BERT
        </div>
        <div class="card-subtitle">
            Embedding Model
        </div>
    </div>
    """, unsafe_allow_html=True)



with col4:

    st.markdown("""
    <div class="mini-card">
        <div class="card-title">
            LinearSVC
        </div>
        <div class="card-subtitle">
            Classifier
        </div>
    </div>
    """, unsafe_allow_html=True)



# -----------------------------
# Prediction
# -----------------------------
if predict:

    if user_input.strip() == "":
        
        st.warning(
            "Please enter a customer message."
        )

    else:

        # Convert text into embeddings
        embedding = embedding_model.encode(
            [user_input]
        )


        # Predict intent
        prediction = classifier.predict(
            embedding
        )[0]


        # Confidence score
        scores = classifier.decision_function(
            embedding
        )[0]


        exp_scores = np.exp(
            scores - np.max(scores)
        )


        probabilities = (
            exp_scores / np.sum(exp_scores)
        )


        confidence = (
            probabilities[np.argmax(probabilities)]
            * 100
        )


        st.success(
            f"Predicted Intent: {prediction}"
        )


        st.info(
            f"Confidence Score: {confidence:.2f}%"
        )