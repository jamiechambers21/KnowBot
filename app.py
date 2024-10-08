import streamlit as st

def main():
    st.set_page_config(page_title="Knowbot", page_icon="🧿")

    st.header("Knowbot - Ask me, I'll know")
    st.text_input("What do you want to know?")

    with st.sidebar:
        st.subheader("Your files")
        st.file_uploader("Upload PDFs here")
        st.button("Process")

if __name__ == '__main__':
    main()
