import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

def get_pdf_text(pdf_docs):
    print("get_pdf_text: START")
    text = ""
    for pdf in pdf_docs:
        # Initilize PDF Reader Object
        pdf_reader = PdfReader(pdf)
        # For each page, add text
        for page in pdf_reader.pages:
            text += page.extract_text()
    print("get_pdf_text: END")
    return text

def main():
    load_dotenv()
    st.set_page_config(page_title="Knowbot", page_icon="🧿")

    st.header("Knowbot - Ask me, I'll know")
    st.text_input("What do you want to know?")

    with st.sidebar:
        st.subheader("Your files")
        pdf_docs = st.file_uploader("Upload PDFs here", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # Get PDF text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                # Get Text Chunks

                # Create vector store

if __name__ == '__main__':
    main()
