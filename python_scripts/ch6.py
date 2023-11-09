from pathlib import Path
import streamlit as st


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


st.markdown(read_markdown_file("pages/Chapter6/01_Chapter6.md"), unsafe_allow_html=True)
st.divider()
st.markdown(read_markdown_file("pages/Chapter6/02_Chapter6.md"), unsafe_allow_html=True)