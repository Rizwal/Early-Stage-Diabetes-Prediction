import streamlit as st
import pickle
import pandas as pd

data=pickle.load(open('data.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

def prediction(age,gender,polyuria,polydipsia,sudden_weight_loss,weakness,polyphagia,genital_thrush,visual_blurring,itching,delayed_healing,
                          irritability,partial_paresis,muscle_stiffness,alopecia,obesity):
    datatopred = pd.DataFrame({
    "Age": age,
    "Gender": gender,
    "Polyuria": polyuria,
    "Polydipsia": polydipsia,
    "sudden weight loss": sudden_weight_loss,
    "weakness": weakness,
    "Polyphagia":polyphagia,
    "Genital thrush": genital_thrush,
    "visual blurring":visual_blurring,
    "Itching":itching,
    "Irritability":delayed_healing,
    "delayed healing":irritability,
    "partial paresis":partial_paresis,
    "muscle stiffness":muscle_stiffness,
    "Alopecia":alopecia,
    "Obesity":obesity
    },index=[0])
    pred=model.predict(datatopred)
    print(pred)
    return pred

st.title("Early Diabetese Prediction")
name=st.text_input("Enter your name:")
age=st.number_input("Enter your Age:")
gender=st.selectbox("Select Gender (1 for Male ,0 for Female)",data['Gender'].unique())

html_temp = """
<div style="background-color:blue;padding:2px">
<h2 style="color:white;text-align:center;font-size:20px">If You have any of these following symptoms/conditions select 1 , else select 0 ! </h2>
</div>
"""
st.markdown(html_temp,unsafe_allow_html=True)   
    
polyuria=st.selectbox("Polyuria",data['Polyuria'].unique()) 
polydipsia=st.selectbox("Polydipsia",data['Polydipsia'].unique()) 
sudden_weight_loss=st.selectbox("Sudden weight loss",data['sudden weight loss'].unique()) 
weakness=st.selectbox("weakness",data['weakness'].unique()) 
polyphagia=st.selectbox("Polyphagia",data['Polyphagia'].unique()) 
genital_thrush=st.selectbox("Genital thrush",data['Genital thrush'].unique()) 
visual_blurring	=st.selectbox("Visual blurring",data['visual blurring'].unique()) 
itching=st.selectbox("Itching",data['Itching'].unique()) 
delayed_healing=st.selectbox("Delayed healing",data['delayed healing'].unique()) 
irritability=st.selectbox("Irritability",data['Irritability'].unique()) 
partial_paresis=st.selectbox("Partial paresis",data['partial paresis'].unique()) 
muscle_stiffness=st.selectbox("Muscle stiffness",data['muscle stiffness'].unique()) 
alopecia=st.selectbox("Alopecia",data['Alopecia'].unique()) 
obesity=st.selectbox("Obesity",data['Obesity'].unique()) 

if(st.button("You are most probably:")):
    result=prediction(age,gender,polyuria,polydipsia,sudden_weight_loss,weakness,polyphagia,genital_thrush,visual_blurring,itching,delayed_healing,
                          irritability,partial_paresis,muscle_stiffness,alopecia,obesity)
    if(result==1):
        st.write('Positive')
    
    else:
        st.write('Negative')

