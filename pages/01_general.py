import os
import streamlit as st
from IPython.display import SVG, display_svg
from config import IMG_PATH



# display(SVG(filename=os.path.join(IMG_PATH, 'lnu.svg')))
st.image(display_svg(SVG(filename=os.path.join(IMG_PATH, 'lnu.svg'))))

