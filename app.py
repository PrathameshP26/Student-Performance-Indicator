import pickle
import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData,PredictionPipeline

st.title('Student Performance Indicator :student:')
results=None

def predict():
    Data = CustomData(gender,race_ethinicity,parental_level_of_ed,lunch,test_prep_course,reading_score,writing_score)

    pred_df=Data.get_data_as_dataframe()
    print(pred_df)

    predict_pipeline=PredictionPipeline()
    results=predict_pipeline.predict(pred_df)
    return results

with st.form("Student form"):
    st.subheader("fill these details:")
    gender=st.radio(
        label="**Gender**:",
        options=["male","female"],
        index=None,
        horizontal=True
    )
    
    lunch=st.radio(
        label="**Lunch**:",
        options=['standard','free/reduced'],
        index=None,
        horizontal=True
    )

    test_prep_course=st.radio(
        label="**Test Preparation Course**:",
        options=['none','completed'],
        index=None,
        horizontal=True
    )

    race_ethinicity=st.selectbox(
        "**Race/Ethinicity**:",
        ('group A','group B','group C','group D','group E')
    )

    parental_level_of_ed = st.selectbox(
        "**Parental level of Education**:",
        ("bachelor's degree",'some college',"master's degree" ,"associate's degree"
 'high school','some high school')
    )
    
    reading_score = st.number_input("**Reading Score**:",placeholder="Type the Score",min_value=0.00,max_value=100.00,value=None)
    
    writing_score = st.number_input("**Writing Score**:",placeholder="Type the Score",min_value=0.00,max_value=100.00,value=None)

    submit_button=st.form_submit_button(label="Submit")

    st.divider()

    st.write("***Math Score Prediction***:")

    if submit_button:
        results=predict()

    if results:
        score=str(results[0])
        st.write(score)
        
        

