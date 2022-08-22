#Chatbot for https://lgu.edu.pk/
# 2022 august
#
#
from model import Model
import streamlit as st

import json
import random
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn import preprocessing
from sklearn.neural_network import MLPClassifier



#initalize a scrapper to get  data
#my_scrapper = Scrapper('https://lgu.edu.pk/')

#streamlit interface
######################################################################################
#title
st.title('LGU ENQBOT')

#st.header('LGU ENQBOT')
st.write('Official website: https://lgu.edu.pk/')


#user input
querry = st.text_input('How can I help you : ', 'My querry')

#robot image
st.image('bot_img.png',width=100)

#removing a button on image with css
hide_img_fs = '''
<style>
button[title="View fullscreen"]{
    visibility: hidden;}
</style>
'''
st.markdown(hide_img_fs, unsafe_allow_html=True)





model= Model('data.json','model.joblib')
model.construct_model()

if querry !="" and querry !=" " and querry !="My querry":
    st.write(model.predict(querry))




