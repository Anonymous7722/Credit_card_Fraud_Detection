import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# loading Trined models
#amount='100'

model=pickle.load(open('dtc_model.pkl','rb'))
ss=pickle.load(open('StandardScaler.pkl','rb'))


def Fraud(Credit):
    Scam=model.predict(Credit)
    if Scam == 1:
        st.write('Fraud Transaction')
    else:
        st.write('Real Transaction')

st.title('Credit Card Fraud Detection')
st.write('This is a simple web application that uses a decision tree classifier to detect credit card fraud Detection')

st.write('Enter credit Card Details.')
number = st.text_input("Insert V1, V2, Vn Details")
amount = st.number_input("Insert Amount Details")

option = st.button('Check')

if option:
    try:
        print('try')
        number=np.array(number.split(',')).astype(float)
        print(number)
        amount=ss.transform(np.array([float(amount)]).reshape(1,-1))
        amount=amount.ravel()
        number=np.append(number,amount).reshape(1,-1)
        Fraud(number)
    except:
        st.write('There is some error with the Data')