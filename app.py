import numpy as np
import pandas as pd
import pickle as pk
import streamlit as st
import base64
import sklearn as sk
from streamlit.components.v1 import html

loaded_model = pk.load(open("trained_model_forest.sav","rb"))
scaled_data = pk.load(open("scaled_data.sav","rb"))

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.vecteezy.com/system/resources/previews/006/712/977/original/abstract-health-medical-science-healthcare-icon-digital-technology-doctor-concept-modern-innovation-treatment-medicine-on-hi-tech-future-blue-background-for-wallpaper-template-web-design-vector.jpg");
background-size: cover;
background-position: top left;
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

def Fee_predict(n):
    Degree = ['99%','B.Sc.','B.Sc.-','BA','BAMS','BASLP','BDS','BHMS','BMS(H)','BNYS','BPTh/BPT','BSAM','BSMS','BSc','BSc.',
              'BUMS','BVMS','Bachelor','CCT','Certificate','Certification','DDV','DDVL','DGO','DHMS','DM','DNB','DNHE','DO','DOMS','DPM','DUMS','DVD','Diploma','Doctor',
              'Doctorate','FCPS','FCPS-','FNB','FRCP','FRCS','Fellow','Fellowship','G.A.M.S','GHMS','LCEH','M.','M.D.',
              'M.Phil','M.Phil-','M.Phil.','M.Sc','M.Sc-','M.Sc.','M.V.Sc','MA','MASLP','MBBS','MBS','MCh','MD','MDS','MDS-',
              'MNAMS','MPTh/MPT','MPhil','MRCOG(UK)','MRCP','MRCS','MS','MSc','MSc.','Master','Masters','Member','P.G','PG','PGD',
              'Ph.','Ph.D.','PhD','Post','Professional','PsyD']
    City = ['Bangalore', 'Delhi', 'Mumbai']
    Speciality = ['Ayurveda','Bariatric Surgeon','Cardiologist','Dentist','Dermatologist','Dietitian','Endodontist','Gastroenterologist',
                  'General Surgeon','Gynecologist','Homoeopath','Infertility Specialist','Internal Medicine','Neurologist',
                  'Obstetrician','Oncologist''Ophthalmologist','Orthopedist','Otorhinolaryngologist','Pain Specialist',
                  'Pediatrician','Periodontist','Physiotherapist','Prosthodontist','Psychiatrist','Pulmonologist','Radiologist',
                  'Rheumatologist','Therapist','Urologist']
    for i in range(len(n)):
        if type(n[i]) == str:
            if n[i] in City:
                n[i]=City.index(n[i])
            elif n[i] in Degree:
                n[i] = Degree.index(n[i])
            elif n[i] in Speciality:
                n[i] = Speciality.index(n[i])
    arr = np.asarray(n)
    arr = arr.reshape(1, -1)
    arr = scaled_data.transform(arr)
    prediction = loaded_model.predict(arr)

    return (f"Fee: {round(prediction[0], 2)}")
  
def main():

    # giving a title    
    # _left, mid, _right = st.columns(3)
    # with mid:
    #    st.image("output-onlinegiftools.gif")
    st.markdown("<h1 style='text-align: center; color: White;'>Doctor Fee Prediction</h1>", unsafe_allow_html=True)        
    # getting the input data from user    
    result = 0
    Degree = ['B.Sc.','B.Sc.-','BA','BAMS','BASLP','BDS','BHMS','BMS(H)','BNYS','BPTh/BPT','BSAM','BSMS','BSc','BSc.',
              'BUMS','BVMS','Bachelor','CCT','Certificate','Certification','DDV','DDVL','DGO','DHMS','DM','DNB','DNHE','DO','DOMS','DPM','DUMS','DVD','Diploma','Doctor',
              'Doctorate','FCPS','FCPS-','FNB','FRCP','FRCS','Fellow','Fellowship','G.A.M.S','GHMS','LCEH','M.','M.D.',
              'M.Phil','M.Phil-','M.Phil.','M.Sc','M.Sc-','M.Sc.','M.V.Sc','MA','MASLP','MBBS','MBS','MCh','MD','MDS','MDS-',
              'MNAMS','MPTh/MPT','MPhil','MRCOG(UK)','MRCP','MRCS','MS','MSc','MSc.','Master','Masters','Member','P.G','PG','PGD',
              'Ph.','Ph.D.','PhD','Post','Professional','PsyD']
    City = ['Bangalore', 'Delhi', 'Mumbai']
    Speciality = ['Ayurveda','Bariatric Surgeon','Cardiologist','Dentist','Dermatologist','Dietitian','Endodontist','Gastroenterologist',
                  'General Surgeon','Gynecologist','Homoeopath','Infertility Specialist','Internal Medicine','Neurologist',
                  'Obstetrician','Oncologist''Ophthalmologist','Orthopedist','Otorhinolaryngologist','Pain Specialist',
                  'Pediatrician','Periodontist','Physiotherapist','Prosthodontist','Psychiatrist','Pulmonologist','Radiologist',
                  'Rheumatologist','Therapist','Urologist']

    DP_Score = st.number_input("Enter DP_Score (please enter value in this range[85-100])",min_value = 85, max_value = 100)
    NPV_Value = st.number_input("Enter NPV Value (please enter value in this range[1-400])",min_value = 1, max_value = 400)
    City_name = st.selectbox("Select the City",City)
    Years_of_Experience = st.number_input("Enter Years_of_Experience (please enter value in this range[0-45])",min_value = 0, max_value = 45)
    Speciality_name = st.selectbox("Select the Speciality",Speciality)
    Degree_number = st.number_input("Enter Degree_number (please enter value in this range[1-5])",min_value = 1, max_value = 5)
    Degree_name = st.selectbox("Select the Degree_name",Degree)
    
    # creating a button for prediction
    if st.button("Predict"):
        result = Fee_predict([DP_Score,NPV_Value,City_name,Years_of_Experience,Speciality_name,Degree_number,Degree_name])
        markdown_text = f"<h2 style='color:white;'><b>{result}</b>!</h2>"
        st.markdown(markdown_text, unsafe_allow_html=True)
        
if __name__ == "__main__":
    main()
