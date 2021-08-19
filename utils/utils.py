import re
import unidecode
import base64
import streamlit as st


def remove_accents(txt):
    """Accents removal"""
    txt = unidecode.unidecode(txt)
    return txt.lower()


def preprocess_dic(txt):
    """Preprocess dictionary words before uploading them (make words accent insensitive)"""
    return remove_accents(txt)


def preprocess_text(txt):
    """Preprocess target text, eliminate unwanted characters"""
    custom_replace = {
        '\n': ' ',
        '\t': ' '
    }
    for c, c_r in custom_replace.items():
        txt = txt.replace(c, c_r)

    txt = remove_accents(txt)
    txt = re.sub('[^a-zA-Z]', ' ', txt)
    return ' '.join(txt.split())


def insensitive_replace(text: str, sub_text: str, replace: str):
    """Replace each occurrence of sub_text in the text regardless of upper/lower cases

    :param text: target text
    :param sub_text: substring
    :param replace: replacement string
    :return: text with replaced sub_text
    """
    txt = re.compile(re.escape(sub_text), re.IGNORECASE)
    return txt.sub(replace, text)


def download_zip_file(txt_files):
    for t in txt_files:
        content = t.get_anonymized_content().encode()
        b64 = base64.b64encode(content).decode()
        href = f'<a href="data:file/content;base64,{b64}" download="{t.get_file_name()}">Download {t.get_file_name()}</a>'
        st.markdown(href, unsafe_allow_html=True)
