import streamlit as st
import numpy as np
import pickle

st.title('Diamonds Checker')

list_of_colors= ('D','E','F','G','H','I','J')
Color=st.selectbox("Select the diamond's color:", list_of_colors)

list_of_clarity= ('I1','IF','SI1','SI2','VS1','VS2','VVS1','VVS2')
Clarity=st.selectbox("Select the diamond's clarity:", list_of_clarity)

carat = st.text_input("Type the diamond's carat (weight): ",0)
depth = st.text_input("Type the diamond's depth: ",0)
table = st.text_input("Type the diamond's table: ",0)

price = st.text_input("Type the diamond's price: ",0)
x = st.text_input("Type the diamond's x (length): ",0)

y = st.text_input("Type the diamond's y (width): ",0)
z = st.text_input("Type the diamond's z (depth): ",0)

colors=[]
clarity=[]
for c in list_of_colors:
    if c==Color:
        colors.append(1)
    else:
        colors.append(0)

for c in list_of_clarity:
    if c==Clarity:
        clarity.append(1)
    else:
        clarity.append(0)

pickle_in = open('predictor.pkl', 'rb')
predictor = pickle.load(pickle_in)

pickle_in = open('scaler.pkl', 'rb')
scaler = pickle.load(pickle_in)

scaled=scaler.transform([[carat,depth,table,price,x,y,z]])
data = np.hstack((scaled,[colors],[clarity])) 

pred_btn = st.button("Predict Diamond's Cut")

if pred_btn:
    result= predictor.predict(data)
    result= result[0]
    if result==1:
        st.title('The predicted diamond cut is Ideal')
    if result==2:
        st.title('The predicted diamond cut is Premium')
    if result==3:
        st.title('The predicted diamond cut is Very Good')
    if result==4:
        st.title('The predicted diamond cut is Good')
    if result==5:
        st.title('The predicted diamond cut is Fair')