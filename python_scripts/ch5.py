from pathlib import Path
import streamlit as st


def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text()


st.markdown(read_markdown_file("pages/Chapter5/01_Chapter5.md"), unsafe_allow_html=True)
st.divider()
st.markdown(read_markdown_file("pages/Chapter5/02_Chapter5.md"), unsafe_allow_html=True)

from streamlit_extras.switch_page_button import switch_page

c1, c2 = st.columns(2)

with c2:
  next_page = st.button("Next")
  if next_page:
    switch_page("chapter 6")

with c1:
  prev_page = st.button("Back")
  if prev_page:
    switch_page("chapter 4")