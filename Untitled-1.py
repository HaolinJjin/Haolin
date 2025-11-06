import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

# --- 基本展示 ---
st.write("This is my first App in ISTM635")
st.title("My first app in ISTM635")

st.balloons()
st.progress(50)

with st.spinner("This is a spinner..."):
    time.sleep(2)

st.sidebar.title("This is a sidebar title")
st.sidebar.header("Employee Status")

# --- 各种交互控件 ---
st.checkbox("This is a checkbox")
st.button("This is a button")
st.radio("This is a radio", ("Option 1", "Option 2"))
st.selectbox("This is a selectbox", ("Option 1", "Option 2"))
st.multiselect("This is a multiselect", ("Option 1", "Option 2"))
st.slider("This is a slider", 0, 100, 50)
st.select_slider("This is a select slider", ("Option 1", "Option 2"))

st.header("This is a header")
st.markdown("This is a markdown")
st.latex(r"E=mc^2")

# --- Activity: Display Graphs ---
st.subheader("Activity: Display Graphs")

# 生成 5000 个随机数（均值 1，标准差 2）
rand = np.random.normal(1, 2, size=5000)

# 创建图表
fig, ax = plt.subplots()
ax.hist(rand, bins=15, color="purple")
ax.set_title("Normal Distribution (mean=1, std=2)")

# 在 Streamlit 显示图像
st.pyplot(fig)
