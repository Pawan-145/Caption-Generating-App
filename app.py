from google import genai
from PIL import Image
import streamlit as st
import os
from dotenv import load_dotenv
import time

st.set_page_config(page_title="AI Caption Generator", layout="centered")

st.title("🖼️ AI Image Caption Generator")
st.warning("Supported Image type: jpg, png, jpeg")

uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "png", "jpeg"])

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

if uploaded_file:
    with st.spinner("Uploading and processing image... 📤"):
      time.sleep(5)
      image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
    

    prompt = """
            Analyze this image and generate:

            1. Formal caption (2-3 sentences, professional)
            2. Casual caption (friendly tone)
            3. SEO caption (15-25 words with keywords)
            4. Alt-text (<125 characters, accessibility focused)

            Format clearly:

            📘 Formal:
            ...

            💬 Casual:
            ...

            📈 SEO:
            ...

            ♿ Alt-text:
            ...
            """
    with st.spinner(" Generating captions... Wait!!!"):

      response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=[prompt, image]
            )

      result = response.text 
  
    st.success("Done!")

    st.markdown("## ✨ Generated Captions")
    
    st.write(result)
     

        
