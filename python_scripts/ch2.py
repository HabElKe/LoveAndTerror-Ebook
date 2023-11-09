from pathlib import Path
import streamlit as st


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


st.markdown(read_markdown_file("pages/Chapter2/01_Chapter2.md"), unsafe_allow_html=True)
st.divider()
st.markdown(read_markdown_file("pages/Chapter2/02_Chapter2.md"), unsafe_allow_html=True)
st.divider()
st.markdown(read_markdown_file("pages/Chapter2/03_Chapter2.md"), unsafe_allow_html=True)
st.divider()
st.markdown(read_markdown_file("pages/Chapter2/04_Chapter2.md"), unsafe_allow_html=True)