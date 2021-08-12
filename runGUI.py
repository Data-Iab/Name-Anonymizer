import streamlit as st
from name_identifier.name_identifier import NameIdentifier
from file_handler.file_loader import STLoader
from anonymizers.anonymizer import Anonymizer
from utils.utils import download_zip_file


def main():
    st.title('Medical reports anonymizer')
    files_name = st.file_uploader("", accept_multiple_files=True)
    name_identifier = NameIdentifier()
    loader = STLoader(uploaded=files_name)
    anonymizer = Anonymizer()
    text_list = []

    if st.button('Anonymize'):
        text_list = loader.load_files()
        text_list = name_identifier.find_entities(text_list)
        text_list = anonymizer.anonymize(text_list)

    download_zip_file(text_list)


if __name__ == '__main__':
    main()
