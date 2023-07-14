import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'col1': [1,2,3]})
df  # 👈 Draw the dataframe

x = 10

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

st.text_input("Your a", key="aname")
st.text_input("Your b", key="bname")
st.text_input("Your c", key="cname")
st.text_input("Your d", key="dname")

# You can access the value at any point with:
st.session_state.aname
st.session_state.bname
st.session_state.cname
st.session_state.dname


if st.checkbox('Show'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

st.write(df)
st.write("hello world")

st.write(x, 'squared is', x*x)
"hello new world" #디폴트로 매직 자동으로 출력되게 돼있음
x

'x', x  # 👈 Draw the string 'x' and then the value of x

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

# Also works with most supported chart types

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)


arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20) #x축이 20개로 나뉘어짐

fig  # 👈 Draw a Matplotlib chart
