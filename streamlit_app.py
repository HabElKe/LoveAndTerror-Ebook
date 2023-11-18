import streamlit as st
from st_pages import Page, Section, add_page_title, show_pages
import streamlit_book as stb
#import warnings

#warnings.filterwarnings('ignore')

# Streamlit webpage properties & layout
st.set_page_config(page_title="Love & Terror",
                   page_icon="🖤", 
                   #layout="wide",
                  )


show_pages(
    [
        Page("streamlit_app.py", "Love & Terror", ""),
        Page("python_scripts/preface.py", "Preface", ""),
        Page("python_scripts/ch1.py", "Chapter 1", ""),
        Page("python_scripts/ch2.py", "Chapter 2", ""),
        Page("python_scripts/ch3.py", "Chapter 3", ""),
        Page("python_scripts/ch4.py", "Chapter 4", ""),
        Page("python_scripts/ch5.py", "Chapter 5", ""),
        Page("python_scripts/ch6.py", "Chapter 6", ""),
        Page("python_scripts/ch7.py", "Chapter 7", ""),
        Page("python_scripts/ch8.py", "Chapter 8", ""),
        Page("python_scripts/ch9.py", "Chapter 9", ""),
        Page("python_scripts/ch10.py", "Chapter 10", ""),
        Page("python_scripts/ch11.py", "Chapter 11", ""),
    ]
)


from PIL import Image

image = Image.open('Terror&Love-Book Cover.png')
st.image(image)

from streamlit_extras.switch_page_button import switch_page
next_page = st.button("Next")
if next_page:
  switch_page("preface")
