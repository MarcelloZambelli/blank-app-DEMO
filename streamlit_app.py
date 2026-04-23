import streamlit as st
import pandas as pd
from custom import top_menu, bottom_head
from numpy.random import default_rng as rng


top_menu()

df = pd.DataFrame(
    [[19.64, -155.99]],
    columns=["lat", "lon"],
)

text, map = st.columns([.35, .65])

with map:
    #st.map(df, color="#ff0000", size=2000)
    

with text:
    st.write("Qui ci vanno le parole")

bottom_head()
