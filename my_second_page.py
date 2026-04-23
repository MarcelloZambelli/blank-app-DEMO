import streamlit as st
import numpy.random as npr


st.title("My Second Page")

st.title("Tabs")


data2plot = npr.rand(30, 1)


tab1, tab2 =  st.tabs(["Tab1", "Tab2"])


tab1.subheader("This is tab 1")
tab1.write("Here is within tab 1")
tab1.bar_chart(data2plot)


tab2.subheader("This is tab 2")
tab2.write("Here is within tab 2")
tab2.line_chart(data2plot)

