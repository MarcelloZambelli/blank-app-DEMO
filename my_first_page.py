import streamlit as st
import numpy as np


st.title("My First Page")

player = st.session_state["player"]
my_player = st.session_state["my_player"]

st.write(f"Your selected player {player}")
st.write(f"My player is {my_player}")


data2plot = np.random.rand(30, 1)

st.title("Columns")



col1, col2 = st.columns([60, 40])



with col1:
    st.header("Column 1")
    st.line_chart(data2plot)
    exp = st.expander("My player")
    exp.write("This is an expander that contains the player selection")
    exp.write(f"You selected {my_player}")
with col2:
    st.header("Column 2")
    st.line_chart(data2plot)










