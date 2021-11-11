

import streamlit as st
import numpy as np
import pandas as pd
import time

st.title("This is may first streamlit")

x = st.slider("select x")
st.write(x, "squere is", x*x)

"""
### Progresbar
"""

progress_bar_label = st.empty()
progress_bar = st.progress(0)
progress_bar2 = st.progress(0)

for i in range(100):
    progress_bar.progress(i)
    time.sleep(0.1)

for i in range(100):
    progress_bar2.progress(i)
    time.sleep(0.1)

option_side = st.sidebar.selectbox("seleccione", ["Uno", "dos", "tres"])
st.sidebar.write("Su selección es:",)