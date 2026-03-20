import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Hugging Face Router endpoint
API_URL = "https://router.huggingface.co/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer YOUR_HF_API_TOKEN"}  # Replace with your Hugging Face token

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

st.title("Vizzy Chatbot 🚀")
st.write("Enter a prompt to generate an image:")

prompt = st.text_input("Prompt", "A futuristic city on Mars with domes and rovers")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        try:
            response = query({"inputs": prompt})
            if response.status_code == 200:
                try:
                    image = Image.open(BytesIO(response.content))
                    st.image(image, caption="Generated Image", use_column_width=True)
                except Exception:
                    st.error("Response was not an image. Details:")
                    st.text(response.text)
            else:
                st.error(f"API error {response.status_code}: {response.text}")
        except Exception as e:
            st.error(f"Image generation failed: {e}")

