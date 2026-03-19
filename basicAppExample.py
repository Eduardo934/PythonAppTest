import streamlit as st
import pandas as pd

st.title("My First Streamlit App")
st.write("Hello *world!*")

df = pd.DataFrame({
'category': ['A', 'B', 'C'],
'sales': [100, 150, 200]
})

# Slider widget
number = st.slider("Pick a number", 0, 100)
st.write("You selected:", number)

# Chart
st.bar_chart(df, x="category", y="sales")