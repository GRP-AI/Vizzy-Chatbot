import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5",
        torch_dtype=torch.float32
    )
    pipe = pipe.to("cpu")  # Ensure CPU compatibility
    return pipe

pipe = load_model()

st.title("Vizzy Chatbot 🚀")
st.write("Enter a prompt to generate an image:")

prompt = st.text_input("Prompt", "A futuristic city on Mars with domes and rovers")

if st.button("Generate Image"):
    with st.spinner("Generating..."):
        image = pipe(prompt).images[0]
        st.image(image, caption="Generated Image", use_column_width=True)



