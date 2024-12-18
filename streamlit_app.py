import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.datasets import load_wine

st.set_page_config (layout='wide')

@st.cache_data
def load_data():
    wine = load_wine()
    wine_df = pd.DataFrame(wine.data, columns=wine.feature_names)
    wine_df['WineType']= [wine.target_names[t] for t in wine.target]
    return wine_df
    
wine_df = load_data()
ingredients = wine_df.drop(columns = ['WineType']).columns
avg_wine_df = wine_df.groupby('WineType').mean().reset_index()


st.title("Wine Dataset Analysis")
st.markdown("Wine Analysis dashboard . Explore relationships between various **ingredients** used in creation of 3 different types of wine")


with st.sidebar:
    st.markdown("Scatter Chart:Explore relationships between Ingredients")
    x_axis = st.selectbox("X-Axis", ingredients)
    y_axis = st.selectbox("Y-Axis", ingredients ,index = 1)
    color_encode = st.checkbox(label='Color Encode by Wine Type')

    st.markdown("Bar Chart:Average Ingredients Per Wine Type")
    bar_multiselect = st.multiselect(label="Bar Chart Ingredients", options=ingredients, default  =['alcohol','malic_acid','ash'])

container = st.container()
chart1 , chart2 = container.columns(2)

with chart1: 
    if x_axis and y_axis:
        title = f"{x_axis.capitalize()} vs {y_axis.capitalize()}"

        # Create a scatter plot using Plotly
        fig = px.scatter(
            wine_df,
            x=x_axis,
            y=y_axis,
            color='WineType' if color_encode else None,
            title=title,
            labels={x_axis: x_axis.capitalize(), y_axis: y_axis.capitalize()},
            width=500,
            height=500
        )

        fig.update_layout(title=dict(font=dict(size=25)), margin=dict(l=50, r=50, t=70, b=50))

        st.plotly_chart(fig)



with chart2:
    if bar_multiselect:
        st.header("Average Ingredients")
        st.bar_chart (avg_wine_df, x='WineType' , y=bar_multiselect, height = 500,use_container_width=True) 




