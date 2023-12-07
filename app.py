import streamlit as st
from PIL import Image
import requests
from io import BytesIO

def download_image(url):
    response = requests.get(url)
    return Image.open(BytesIO(response.content))

def main():
    st.title("Image Converter")

    # Option to upload from URL
    image_url = st.text_input("Enter image URL:")
    if image_url:
        try:
            uploaded_file = download_image(image_url)
            st.image(uploaded_file, caption="Downloaded Image.", use_column_width=True)
        except Exception as e:
            st.error(f"Error: {str(e)}")
            return
    else:
        uploaded_file = st.file_uploader("Choose a WebP image...", type="webp")

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded WebP Image.", use_column_width=True)

        # Convert WebP to PNG
        if st.button("Convert to PNG"):
            st.image(uploaded_file, caption="Converted PNG Image.", use_column_width=True, output_format="PNG")

if __name__ == "__main__":
    main()
