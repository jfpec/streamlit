import streamlit as st
import numpy as np
import pandas as pd
import math

st.title("Uber pick up test")

DATA_SOURCE = "https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
@st.cache
def download_data():
    return (pd.read_csv(DATA_SOURCE)
            .rename(columns={"Lat": "lat", "Lon": "lon"})
            )
df = download_data()
page_size = 1000
total_pages = math.ceil(len(df)/page_size)
starting_value = 0
slider = st.slider("Select the page", 1, total_pages)
st.write("page selected", slider, "with limits ", (((slider-1)*page_size), (slider*page_size)-1))
df = df.loc[((slider-1)*page_size):(slider*page_size)-1]
df
st.map(df)