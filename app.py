import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstore import FAISS

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

def get_text_chunks(text):
    print("get_text_chunks: START")
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    chunks = text_splitter.split_text(text)
    print("get_text_chunks: END")
    return chunks

def get_vectorstore(text_chunks):
    print("get_vectorstore: START")
    # Do with Open AI
    embeddings = OpenAIEmbeddings()
    # Do with HuggingFace
    # embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    print("get_vectorstore: END")
    return vectorstore


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
                text_chunks = get_text_chunks(raw_text)
                st.write(text_chunks)

                # Create vector store
                vectorstore = get_vectorstore(text_chunks)

if __name__ == '__main__':
    main()
