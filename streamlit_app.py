# Predicting salary #

import pandas as pd
import streamlit as st

data = pd.DataFrame(data={
    'experience':[1,3,5,10],
    'gender':[1,0,0,1],
    'salary':[1000,3000,5200,9800]
})

X = data.drop('salary',axis=1)
y = data['salary']

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X,y)


xp = st.slider( 'years of experience:',0,12 )
sex = st.selectbox( 'your gender:',['Male','Female'] )

if sex == 'Male' :
    sex = 1
else :
    sex = 0

    
predict = pd.DataFrame( data={
    'experience':[xp],
    'gender':[sex]
})

if ( xp ) :
    for i in range(10) :st.text('')
    st.text( 'Your estimated salary is: {}'.format( int(model.predict(predict)[0]) ) )

