import streamlit as st
import pickle
import pandas as pd

with open("model.pkl","rb") as f:
    model=pickle.load(f)

with open("scaler.pkl","rb") as f:
    scalar=pickle.load(f)

st.set_page_config("House_Price_prediction",layout="centered")
page=st.sidebar.radio("Select one between the two:",["Intro","Prediction"])
if page=="Intro":
    st.title("Hey!!!, We are going to predict House Price")
elif page=="Prediction":
    st.title("House Price Prediction")
    MedInc=st.number_input("Enter your median income in block group:",min_value=500,max_value=100000,step=100)
    HouseAge=st.number_input("Enter your median house age in block group:",min_value=0,max_value=10,step=1)
    AveRooms=st.number_input("Enter average number of rooms per household :",min_value=1,max_value=5,step=1)    
    AveBedrms=st.number_input("Enter the average number of bedrooms per household:",min_value=1,max_value=5,step=1) 
    Population=st.number_input("Enter the block group population:",min_value=1000,max_value=20000,step=100)
    AveOccup=st.number_input("Enter average number of household members:",min_value=1,max_value=5,step=1)
    Latitude=st.number_input("Enter block group latitude:",min_value=0.0,max_value=90.0,step=0.01)
    Longitude=st.number_input("Enter block group longitude:",min_value=0.0,max_value=90.00,step=0.01)
    
    input_data=pd.DataFrame([{"MedInc":MedInc,
                              "HouseAge":HouseAge,
                              "AveRooms":AveRooms,
                              "AveBedrms":AveBedrms,
                              "Population": Population,
                              "AveOccup":AveOccup,
                              "Latitude":Latitude,
                              "Longitude": Longitude}])
    
    #scalar
    input_scaled=scalar.transform(input_data)
    
    if st.button("Predict"):
        with st.spinner("Thinking..."):
            output=model.predict(input_scaled)
            st.success("Response:")
            st.write(f"Price in lakh:{output}")
    
    
    
    
