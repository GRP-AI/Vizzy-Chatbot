import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

# Load the model once and cache it
@st.cache_resource
def load_model():
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float32
        )
        pipe = pipe.to("cpu")  # Force CPU mode for Streamlit Cloud
        return pipe
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

pipe = load_model()

st.title("Vizzy Chatbot 🚀")
st.write("Enter a prompt to generate an image:")

# Prompt input
prompt = st.text_input("Prompt", "A futuristic city on Mars with domes and rovers")

# Generate image button
if st.button("Generate Image"):
    if pipe is None:
        st.error("Model not available. Please check requirements.txt and logs.")
    else:
        try:
            with st.spinner("Generating image..."):
                image = pipe(prompt).images[0]
                st.image(image, caption="Generated Image", use_column_width=True)
        except Exception as e:
            st.error(f"Image generation failed: {e}")
