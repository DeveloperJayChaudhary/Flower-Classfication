import streamlit as st 
import pandas as pd 
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediciton APP
This app predicts the Iris  flower type!
""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length',4.3,7.9,5.4)
    sepal_width = st.sidebar.slider('Sepal width',2.0,4.4,3.4)
    petal_length = st.sidebar.slider('Petal length',1.0,6.9,1.3)
    petal_width = st.sidebar.slider('Petal width',0.1,2.5,0.2)
    data={ 'sepal_length':sepal_length,
    'sepal_width':sepal_width,
    'petal_length':petal_length,
    'petal_wigth':petal_width}
    features =pd.DataFrame(data,index=[0])
    return features
    
df = user_input_features()

st.subheader("User Input Parameters")
st.write(df)
iris=load_iris()
X=iris.data
y=iris.target

clf=RandomForestClassifier()
clf.fit(X,y)

prediction=clf.predict(df)
prediction_proba=clf.predict_proba(df)

st.subheader("Class lables and their corresponding index number")
st.write(iris.target_names)

st.subheader("Prediciton")
st.write(iris.target_names[prediction])

st.subheader("Prediciton Probability")
st.write(prediction_proba)


