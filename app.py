import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

# Cache the model so it loads only once
@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1-base",  # lighter model than v1-5
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")  # Streamlit Cloud runs on CPU
    return pipe

pipe = load_model()

st.title("Vizzy Chatbot 🚀")
st.write("Enter a prompt to generate an image:")

prompt = st.text_input("Prompt", "A futuristic city on Mars with domes and rovers")

if st.button("Generate Image"):
    with st.spinner("Generating image... (may take ~30s on CPU)"):
        try:
            image = pipe(prompt).images[0]
            st.image(image, caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"Image generation failed: {e}")

              
