from pathlib import Path
import streamlit as st


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


st.markdown(read_markdown_file("pages/Chapter5/01_Chapter5.md"), unsafe_allow_html=True)
st.divider()
st.markdown(read_markdown_file("pages/Chapter5/02_Chapter5.md"), unsafe_allow_html=True)