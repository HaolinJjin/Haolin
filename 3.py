import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(
    np.random.randn(10, 2), columns=['Product A', 'Product B']
)

# --- 地图数据 ---
df2 = pd.DataFrame(
    np.random.randn(500, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(df2)


print(df)
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)