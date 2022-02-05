import streamlit as st

import helpers as hp

st.header("Hello")

recipies = hp.getRecipies()
st.table(recipies)
