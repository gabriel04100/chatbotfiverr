#Chatbot for https://lgu.edu.pk/
# 2022 august
#
#
from model import Model
import streamlit as st




#initalize a scrapper to get  data
#my_scrapper = Scrapper('https://lgu.edu.pk/')

#streamlit interface
######################################################################################
#title
st.title('LGU ENQBOT')

#st.header('LGU ENQBOT')
st.write('Official website: https://lgu.edu.pk/')


#user input







model= Model('data.json','model.joblib')
model.construct_model()



querry = st.text_input('How can I help you : ', '')
if st.button('send'):
    if querry !="" and querry !=" " and querry !="My querry":
        st.write(model.predict(querry))


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


