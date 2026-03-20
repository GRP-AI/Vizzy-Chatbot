import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Hugging Face API endpoint for Stable Diffusion
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer YOUR_HF_API_TOKEN"}  # Replace with your Hugging Face token

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

st.title("Vizzy Chatbot 🚀")
st.write("Enter a prompt to generate an image:")

prompt = st.text_input("Prompt", "A futuristic city on Mars with domes and rovers")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        try:
            image_bytes = query({"inputs": prompt})
            image = Image.open(BytesIO(image_bytes))
            st.image(image, caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"Image generation failed: {e}")

