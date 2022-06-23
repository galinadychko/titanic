# Contents of ~/my_app/main_page.py
import streamlit as st
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--local", action='store_true', help="If local data is taken from the local folder")
args = parser.parse_args()


st.markdown("# Model Monitoring Page. " + ("Local" if args.local else "DB") + " data.")
st.sidebar.markdown("# Main page 🎈")
#
# # Contents of ~/my_app/pages/page_2.py
# import streamlit as st
#
# st.markdown("# Page 2 ❄️")
# st.sidebar.markdown("# Page 2 ❄️")
#
# # Contents of ~/my_app/pages/page_3.py
# import streamlit as st
#
# st.markdown("# Page 3 🎉")
# st.sidebar.markdown("# Page 3 🎉")
