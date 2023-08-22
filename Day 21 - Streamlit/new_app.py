import streamlit as st
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score

# Make Containers

header = st.container()
datasets = st.container()
features = st.container()
model_training = st.container()

with header:
    st.title("Data Analysis on Titanic Dataset 🚢")
    st.text("Titanic dataset is publically available")

with datasets:
    st.header("Dataset can be easily found on the internet")
    df = sns.load_dataset("titanic")
    df = df.dropna()
    st.write(df.head(10))

    # Creating a Bar-Chart

    # Sex/Gender
    st.subheader("Number of Male and Female Passenger on-board")
    st.bar_chart(df["sex"].value_counts())

    # Class Types
    st.subheader("Passengers with class type")
    st.bar_chart(df["pclass"].value_counts())

    # Age
    st.subheader("Number of Passengers by Age")
    st.bar_chart(df["age"].sample(20))

with features:
    st.header("The features of Titanic Dataset")
    st.markdown("**1. First feature will be:**")
    st.write(df.columns)


with model_training:
    st.header("Data Analysis of Dataset")
        
    # Getting Features
    input, display = st.columns(2)

    # 1st Column will have Selection Points
    max_depth = input.slider("How many people did you know?", min_value= 10, max_value= 100, value= 20, step= 5)


    # n_estimators
    n_estimators = input.selectbox("How many trees should be there in Random Forest Classifier?", options= [100, 200, 300, 400,'No Limit'])

    # Features Input from User

    input_feature = input.text_input("Which feature should be used?")

    # ML Model
    model = RandomForestRegressor(max_depth= max_depth, n_estimators= n_estimators)
    X = df[[input_feature]].values
    y = df[['fare']]
    model.fit(X, y)
    pred = model.predict(y)


    st.header("Accuracy Scores")

    # Scores
    st.write("MAE")
    st.write(mean_absolute_error(y, pred))

    st.write("MSE")
    st.write(mean_squared_error(y, pred))

    st.write("R2")
    st.write(r2_score(y, pred))



