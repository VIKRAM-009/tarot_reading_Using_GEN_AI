# -*- coding: utf-8 -*-
"""
Created on Wed Mar 12 10:07:40 2025

@author: vicky
"""
import streamlit as st
import json
import random
from PIL import Image
import os
import requests

# Hugging Face API Key
API_KEY = os.getenv("HUGGINGFACE_API_KEY")  # ✅ Secure way to load the key

if API_KEY is None:
    raise ValueError("API key not found! Make sure you set it in Streamlit secrets.")

HEADERS = {"Authorization": f"Bearer {API_KEY}"}

MODEL_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"

json_path = os.path.join(os.getcwd(), "tarot-images.json")
# Load Tarot Card Data
with open(json_path, "r", encoding="utf-8") as file:
    tarot_data = json.load(file)

cards = tarot_data["cards"]  # Extract list of tarot cards

# Set the image folder path
image_folder = os.path.join(os.getcwd(), "cards")
image_path = os.path.join(image_folder, cards["img"])
 # Make sure your images are stored in this folder

# Function to get AI-generated tarot reading using Hugging Face API
def get_ai_tarot_reading(card_name, meanings, question):
    prompt = f"""
    You are a tarot expert. The user drew the card '{card_name}'.
    The meanings are: {meanings}.
    The user asked: '{question}'.
    Provide a mystical and deep interpretation.
    """

    response = requests.post(
        "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"inputs": prompt}
    )

    if response.status_code == 200:
        return response.json()[0]["generated_text"]  # Extract AI-generated text
    else:
        return f"API Error {response.status_code}: {response.text}"



# Streamlit UI
st.markdown("""
    <style>
        body {
            background-color: #282c34;
            color: white;
            text-align: center;
        }
        .stButton>button {
            background-color: #6a0dad;
            color: white;
            font-size: 18px;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔮 Tarot Card Reading")
st.write("Ask a question and reveal your tarot reading.")

# User question input
question = st.text_input("Enter your question:", "What does the future hold for me?")

# Button to draw cards
if st.button("Check Fortune"):
    selected_cards = random.sample(cards, 3)  # Pick 3 random cards

    st.write("✨ **Your Tarot Reading:** ✨")
    
    cols = st.columns(3)  # Create 3 columns for images
    for i, card in enumerate(selected_cards):
        with cols[i]:  
            image_filename = card["img"]  # Get image filename
            image_path = os.path.join(image_folder, image_filename)

            if os.path.exists(image_path):  # Check if image exists
                img = Image.open(image_path)
                st.image(img, caption=card["name"], use_container_width=True)
                st.write(f"**Keywords:** {', '.join(card['keywords'])}")
                st.write(f"**Meaning (Light):** {', '.join(card['meanings']['light'])}")
                st.write(f"**Meaning (Shadow):** {', '.join(card['meanings']['shadow'])}")
                st.write(f"**Fortune Telling:** {', '.join(card['fortune_telling'])}")
                
                # Generate AI Tarot Reading using Hugging Face API
                ai_reading = get_ai_tarot_reading(card["name"], card["meanings"], question)
                st.write(f"**🔮 AI Interpretation:** {ai_reading}")
            else:
                st.error(f"⚠️ Image not found: {image_filename}")
