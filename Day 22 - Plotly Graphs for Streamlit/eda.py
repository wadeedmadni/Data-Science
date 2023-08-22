import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
import seaborn as sns
from ydata_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Title
st.markdown('''
# **EDA WebApp**
Author: [Wadeed Madni](www.github.com/wadeedmadni)
''')

# Sidebar
with st.sidebar.header("Upload your Dataset File 📄"):
    uploaded_file = st.sidebar.file_uploader("Upload your file Here: 👇🏻", type=['csv'])
    st.sidebar.markdown("[Example CSV File](https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv)")

# Profiling
if uploaded_file is not None:
    @st.cache_data
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df = load_csv()
    pr = ProfileReport(df, explorative = True)

    st.header("Input DataFrame")
    st.write(df)
    st.markdown("-------")
    st.header('**Profiling Report**')
    st_profile_report(pr)
else:
    st.info("File Not Uploaded")

    # Example Dataset
    if st.button("Use Example Dataset"):
        @st.cache_data
        def load_csv():
            url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
            a = pd.read_csv(url, index_col=0)
            return a
        df = load_csv()
        pr = ProfileReport(df, explorative = True)

        st.header("Input DataFrame")
        st.write(df)
        st.markdown("---")
        st.header('**Profiling Report**')
        st_profile_report(pr)

#adding comment to check cache
