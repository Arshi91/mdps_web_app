# -*- coding: utf-8 -*-
"""
Created on Sun Mar  2 07:45:21 2025

@author: harsh
"""


import pickle
import streamlit as st
from streamlit_option_menu import option_menu




st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        background-color:#64bbf5;  Sidebar Background Color */
    }
    
   

    </style>
    """,
    unsafe_allow_html=True
)









import base64

def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()
        
    st.markdown(
        f"""
        <style>
        /* Background container */
        .background-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
        }}

        .background-container::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("data:image/jpg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            filter: blur(5px);
        }}

        .stApp {{
            background: transparent !important;
        }}

        /* Sidebar Text Color */
        [data-testid="stSidebarNav"] span {{
            color: green !important;
        }}

       

        h1 {{
            color: black !important;
            text-shadow: 2px 2px 4px white;
        }}
        </style>
        <div class="background-container"></div>
        """,
        unsafe_allow_html=True
    )







# Set the background with blur effect
set_bg("Image1.jpg")

#loading saved models
Kidney_model= pickle.load(open('kidney3.pkl','rb'))
Breast_cancer_model = pickle.load(open('breast_cancer4.pkl','rb'))
Liver_model= pickle.load(open('Liver3.pkl','rb'))

Parkinsons_model = pickle.load(open('Parkinsons_disease.pkl','rb'))


#sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Integrated Disease Prediction System',
                           [
                              
                            'Kidney Disease Prediction',
                            'Breast Cancer Prediction',
                            'Liver Disease Prediction',
                            'Parkinsons Disease Prediction'
                            ],
                           #icons=['activity','heart-pulse','person-wheelchair','person'],
                           icons=['droplet', 'heart-pulse', 'capsule', 'person-standing'],
                           default_index=0,
                           menu_icon="hospital",
                           styles={
        "container": {"padding": "5px", "background-color": "#f4fc79"},
        "icon": {"color": "white", "font-size": "20px"},
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#ffcccc"},
        "nav-link-selected": {"background-color": "red", "color": "black"},
    })

    
    
#Liver Disease prediction page

#if(selected == 'Liver Disease Prediction'):
   
    #page title
    #st.title('Liver Disease Prediction')

#if(selected == 'Breast Cancer Prediction'):
   
    #page title
    #st.title('Breast Cancer Prediction')

#if(selected == 'Kidney Disease Prediction'):
   
    #page title
    #st.title('Kidney Disease Prediction')"""
    #Age	Gender	Total_Bilirubin	Alkaline_Phosphotase	Alamine_Aminotransferase	Aspartate_Aminotransferase	Total_Protiens	Albumin	Albumin_and_Globulin_Ratio








#radius_mean perimeter_mean area_mean concave points_mean radius_worst concave points_worst


if selected == 'Kidney Disease Prediction':
    st.title('kidney Disease Prediction')
    
    col1,col2 = st.columns(2)
    with col1:
        age=st.text_input("age")
    with col2:
        bp=st.text_input(" bp")
    with col1:
        albumin=st.text_input("albumin")
    with col2:
        sugar=st.text_input("sugar")
    with col1:
        blood_glucose_level=st.text_input("blood_glucose_level")
    with col2:
        blood_urea=st.text_input(" blood_urea")
    with col1:
        Serum_Creatinine=st.text_input(" Serum_Creatinine")
    with col2:
        Hypertension=st.text_input(" Hypertension")
    with col1:
       Diabetes_Mellitus=st.text_input("Diabetes_Mellitus")
    #code for prediction
    kidney_diagnosis =''

    #creating button for prediction

    if st.button('Kidney disease Result'):
        kidney_prediction =Kidney_model.predict([[ age, bp,  albumin, sugar, blood_glucose_level, blood_urea, Serum_Creatinine,Hypertension, Diabetes_Mellitus	
    ]])
        
        if(kidney_prediction[0]==1):
            kidney_diagnosis="You are having kidney Disease"

        else:
            kidney_diagnosis="You are not  having kidney Disease"


    st.success(kidney_diagnosis)


if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction')
    col1,col2= st.columns(2)
    with col1:
        radius_mean=st.text_input("radius_mean")
    with col2:
       perimeter_mean=st.text_input(" perimeter_mean")
    with col1:
        area_mean=st.text_input("area_mean")
    with col2:
        concave_points_mean=st.text_input("concave_points_mean")
    with col1:
        radius_worst=st.text_input("radius_worst")
    with col2:
        concave_points_worst=st.text_input("concave_points_worst")
        
    #code for prediction
    Breastcancer_diagnosis =''

    #creating button for prediction

    if st.button('Breast disease Result'):
        Breast_prediction =Breast_cancer_model.predict([[ radius_mean, perimeter_mean, area_mean, concave_points_mean, radius_worst, concave_points_worst

    ]])
        
        if(Breast_prediction[0]==0):
            Breastcancer_diagnosis="You are not having Breast Cancer Disease"
        else:
            Breastcancer_diagnosis="You are having Breast cancer Disease"
    st.success(Breastcancer_diagnosis)

    #st.markdown("<h1>Breast Cancer Prediction</h1>", unsafe_allow_html=True)



if selected == 'Liver Disease Prediction':
    st.title('Liver disease prediction')

    #st.markdown("<h1>Liver Disease Prediction</h1>", unsafe_allow_html=True)

    col1,col2,col3 = st.columns(3)
    with col1:
        Age=st.text_input("Age")
    with col2:
        Gender=st.text_input("Gender")
    with col3:
        Total_Bilirubin=st.text_input("Total_Bilirubin")
    with col1:
        Alkaline_Phosphotase=st.text_input("Alkaline_Phosphotase")
    with col2:
        Alamine_Aminotransferase=st.text_input("Alamine_Aminotransferase")
    with col3:
        Aspartate_Aminotransferase=st.text_input("Aspartate_Aminotransferase")
    with col1:
        Total_Protiens=st.text_input("Total_Protiens")
    with col2:
        Albumin=st.text_input("Albumin")
    with col3:
        Albumin_and_Globulin_Ratio=st.text_input("Albumin_and_Globulin_Ratio")


#code for prediction   
    liver_diagnosis =''
#creating button for prediction
    if st.button('Liver disease Result'):
        liver_prediction =Liver_model.predict([[ Age,	Gender	,Total_Bilirubin,	Alkaline_Phosphotase,	Alamine_Aminotransferase,	Aspartate_Aminotransferase,	Total_Protiens,	Albumin,Albumin_and_Globulin_Ratio
    ]])
        
        if(liver_prediction[0]==1):
            liver_diagnosis="You are having Liver Disease"
        else:
            liver_diagnosis="You are not  having Liver Disease"
    st.success(liver_diagnosis)

    
#age bp al su bgr bu sc htn dm

    #st.markdown("<h1>Kidney Disease Prediction</h1>", unsafe_allow_html=True)
    
#MDVP:Fo(Hz)








if selected == 'Parkinsons Disease Prediction':
    st.title('Parkinsons Disease Prediction')
    
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        Fo=st.text_input("MDVP:Fo(Hz)")
    with col2:
        Fhi=st.text_input(" MDVP:Fhi(Hz)")
    with col3:
        Flo =st.text_input("MDVP:Flo(Hz)")
    with col4:
        MDVP_jitter=st.text_input("MDVP:Jitter(%)")
    with col1:
        RAP = st.text_input("MDVP:RAP")
    with col2:
        Shimmer=st.text_input("MDVP:Shimmer")
    with col3:
       Shimmer_db=st.text_input("MDVP:Shimmer(dB)")
    with col4:
        Shimmer_APQ5=st.text_input("Shimmer:APQ5")
    with col1:
       NHR=st.text_input("NHR")
    with col2:
       HNR=st.text_input("HNR")
    with col3:
       RPDE=st.text_input("RPDE")
    with col4:
       DFA=st.text_input("DFA")
    with col1:
        spread1=st.text_input("spread1")
    with col2:
        spread2=st.text_input("spread2")
    with col3:
       D2=st.text_input("D2")
    with col4:
        PPE=st.text_input("PPE")
    #code for prediction
    Parkinsons_diagnosis =''

    #creating button for prediction

    if st.button('Parkinsons disease Result'):
        Parkinsons_prediction =Parkinsons_model.predict([[Fo,Fhi,Flo,MDVP_jitter,RAP,Shimmer,Shimmer_db,Shimmer_APQ5,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
    
        
        if(Parkinsons_prediction[0]==1):
           Parkinsons_diagnosis="You are having parkinsons Disease"

        else:
            Parkinsons_diagnosis="You are not  having parkinsons Disease"
    st.success(Parkinsons_diagnosis)
