import streamlit as st

import helpers as hp

st.set_page_config(layout="wide")
st.header("Hello")

recipies = hp.getRecipies()
#st.dataframe(recipies)
#st.table(recipies)
st.markdown(recipies.to_html(), unsafe_allow_html=True)


