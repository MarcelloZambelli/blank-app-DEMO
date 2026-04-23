import streamlit as st
import pandas as pd
from custom import top_menu, bottom_head
import numpy as np
import time as t

if False:
    st.title("Metrics")

    st.metric(label="Athlete's Max Velocity", value="45,5 km/h",
              delta="-" \
              "4,5 km/h")








    st.title("Dataframes (not pandas)'")


    data = {
        "name": ["Messi", "Maradona", "Pelé"],
        "goals": [750, 345, 767],
        "assists": [300, 150, 200]}

    df1 = pd.DataFrame(data)

    st.table(df1)

    st.dataframe(df1)


    goals4seasons = np.random.randint(20, size=(40, 3))
    players = ["Player A", "Player B", "Player C"]

    df2 = pd.DataFrame(goals4seasons, columns=players)

    st.dataframe(df2)

    st.title("Line Chart")

    st.line_chart(df2)

    st.title("Area chart")

    st.area_chart(df2)

    st.title("Bar Chart")

    st.bar_chart(df2)

    st.title("Scatter Plot")

    num_points = 30
    max = 100
    x = np.random.rand(num_points) * max
    y = np.random.rand(num_points) * max
    marker_size = np.random.rand(num_points) * max
    marker_col = np.random.rand(num_points, 3)

    color_tuple = [tuple(color) for color in marker_col]

    scatter_data = {
        "x_coord": x,
        "y_coord": y,
        "marker_size": marker_size,
        "color": color_tuple}

    df3 = pd.DataFrame(scatter_data)

    st.dataframe(df3)

    st.scatter_chart(df3, x="x_coord", y="y_coord",
                     size="marker_size", color="color")


    st.title("GPS Position")

    n_position = 20

    lat_range = (45.8, 45.9)
    long_range = (9.35, 9.45)

    latitude = np.random.uniform(lat_range[0], lat_range[1], n_position)
    longitude = np.random.uniform(long_range[0], long_range[1], n_position)


    gps_position = {
        "lat": latitude,
        "long": longitude}

    df4 = pd.DataFrame(gps_position)

    st.map(df4, latitude="lat", longitude="long")


    st.title("State Messages")

    st.error("Error Message")
    st.warning("Warning Message")
    st.info("Info Message")
    st.success("Success Message")

    st.title("Progress bar")

    progress_bar = st.progress(0) # progress bar object creeated and set to 0
    status_text = st.empty()

    for i in range(101):
        # anything concerning processing
        t.sleep(0.01)
        progress_bar.progress(i)
        status_text.write(f"Processing . . . {i}%")

    st.success("Processing Complete!")


    st.title("Spinner")

    with st.spinner("Loading ...", show_time=True):
        t.sleep(2)
    st.success("Waiting Complete")


    st.title("Session State")

    my_name = st.text_input("Enter your name, please")

    st.session_state["name"] = my_name

    saved_name = st.session_state["name"]

    st.write(f"Hello, {saved_name}!")

my1stpage = st.Page("my_first_page.py", title="My First Page")
my2ndpage = st.Page("my_second_page.py", title="My Second Page")

pg = st.navigation([my1stpage, my2ndpage])

st.set_page_config(page_title="My First App",
                   page_icon=":soccer:",
                   layout="wide")





# object approach
st.sidebar.selectbox("Select a player",
                     ["Messi", "Ronaldo", "Fonseca"],
                     key="player")

player = st.session_state["player"]



with st.sidebar:
    st.radio("Select player",
             ("Messi", "Ronaldo", "Fonseca"),
             key="my_player")

my_player = st.session_state["my_player"]


pg.run()




