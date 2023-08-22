import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

header = st.container() 

with header:
    st.title("Streamlit x Plotly")

    st.header("Dashboard Using Plotly Graphs")
    st.text("Ploty has another language called Dash by which dashboards can be created")


df = px.data.gapminder()
df_1 = df.copy()
st.write(df)

st.write(df.columns)

# Data summary
st.write(df.describe())


st.header("Graph By Year")

# Data Preposessing
option_year = df['year'].unique().tolist()
year = st.selectbox("Choose Year:", option_year, 0)
df = df[df['year']== year] # fetching details of the selected year from df

# Visualizatoin
fig_1 = px.scatter(df, x = 'gdpPercap', y = 'lifeExp', size = 'pop', color = 'country', hover_name = 'country',
                 log_x = True, size_max = 55, range_x = [100, 100000], range_y = [20, 90],
                 labels=dict(gdpPercap="GDP per Capita", lifeExp="Life Expectency"),
                 )
st.write(fig_1)


# Animated Visualizatoin

st.header("Animated Visualization")
fig = px.scatter(df_1, x = 'gdpPercap', y = 'lifeExp', size = 'pop', color = 'country', hover_name = 'country',
                 log_x = True, size_max = 55, range_x = [100, 100000], range_y = [20, 90],
                 labels=dict(gdpPercap="GDP per Capita", lifeExp="Life Expectency"),
                 animation_frame = 'year', animation_group = 'country',
                 )
# Delay animation frames per second, default is 500
fig.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 1000

st.write(fig)


