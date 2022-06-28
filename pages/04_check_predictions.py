import os
import pandas as pd
import streamlit as st
from config import DATA_PATH

# add header
st.header("Check predictions by ID")

# add text input
st.text_area("ID", value="", height=1, max_chars=3, key="id")

# read the initial data to search a user within it
df_full = pd.read_csv(os.path.join(DATA_PATH, "train.csv"))
df_full["PassengerId"] = df_full.PassengerId.astype(str)

# search and display features of the user with the input id value
if st.session_state.get("id"):
    pass
    ################################################################################################
    # TODO: Display user's features with the input id
    ################################################################################################
    # Expected solution: st.write(df_full[df_full.PassengerId == st.session_state.id])
