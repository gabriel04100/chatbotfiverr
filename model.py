from importlib.resources import path
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
from joblib import dump, load


class Model:
    def __init__(self,data_path,model_path=""):
        self.model_path=model_path
        self.path=data_path
        self.stemmer=PorterStemmer()
        self.le = preprocessing.LabelEncoder()
        self.X_train=[]
        self.y_train =[]
        self.tags=[]
        self.tags_labelled=[]
        self.df=[]
        with open(self.path,'r') as file:
            self.data=json.load(file)

        #setting up training tags
        for item in self.data['intents']:
            if item['tag'] not in self.tags:
                    self.tags.append(item['tag'])

        #setting up training entries
        for item in self.data['intents']:
            for  X in item['patterns']:
                #preprocessing, split entry in list then stemming
                X = word_tokenize(X)
                X=[self.stemmer.stem(item) for item in X]
                X = ' '.join(X)
                self.X_train.append(X)
                self.y_train.append(item['tag'])

        #preprocess training data
        self.le.fit(self.tags)
        self.tags_labelled=self.le.transform(self.y_train)
        self.df=pd.DataFrame(self.data['intents'])
    

    def construct_model(self):
        if self.model_path !="":
            try:
                self.model_pipeline=load(self.model_path)
            except Exception as e:
                print(e)
                self.model_pipeline= make_pipeline(TfidfVectorizer(),MLPClassifier(max_iter=3000))
                self.model_pipeline.fit(self.X_train,self.tags_labelled)
                dump(self.model_pipeline, 'model.joblib')




    #function for prediction
    def predict(self,entry):
        stemmer=PorterStemmer()
        entry=word_tokenize(entry)
        entry=[stemmer.stem(item) for item in entry]
        entry = ' '.join(entry)
        entry= [entry]
        test=self.le.inverse_transform(self.model_pipeline.predict(entry))
        return random.choice(self.df[self.df['tag']==test[0]].responses.tolist()[0])
