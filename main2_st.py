import streamlit as st
from PIL import Image
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

def main():
    st.title("Image Text Extractor")

    # Step 1: Upload the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Step 2: Extract text from the image
        if st.button("Extract Text"):
            text = pytesseract.image_to_string(image)
            st.subheader("Extracted Text")
            st.write(text)

if __name__ == "__main__":
    main()
