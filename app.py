import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

# Load model once (CPU-friendly)
@st.cache_resource
def load_model():
    return StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32
    )

pipe = load_model()

st.title("Vizzy Chatbot 🚀")
st.write("Enter a prompt to generate an image:")

# Prompt input
user_prompt = st.text_input("Prompt", "A futuristic city on Mars with domes and rovers")

if st.button("Generate Image"):
    with st.spinner("Generating image..."):
        image = pipe(user_prompt).images[0]
        st.image(image, caption="Generated Image", use_column_width=True)


