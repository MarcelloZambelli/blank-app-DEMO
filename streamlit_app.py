import streamlit as st
from custom import top_menu, bottom_head

top_menu()

my_sport = ["Soccer", "Tennis", "Baketball"]

if st.button("Sports"):
    st.write("My sports are", my_sport)


check_out = st.checkbox("Do you like football?")

if check_out:
    st.write("Great")
else:
    st.write("What a pity!")

bottom_head()
