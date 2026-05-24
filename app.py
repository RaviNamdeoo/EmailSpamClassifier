import streamlit as st
import pickle
import string
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()

tf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('RandomForestModel.pkl','rb'))

st.title("Email Spam Classifier")

input_sms = st.text_input("Enter the message")

def process(text):
    text = text.lower()  # lower case

    text = nltk.word_tokenize(text)      # tokenize

    y = []                  # remove special characters
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()                # removes stop words and punctuation
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    
    return ' '.join(y)

if st.button('Predict'):

    # 1.preprocess
    transform_sms = process(input_sms)

    # 2.vectorize
    vector_input = tf.transform([transform_sms])

    # 3.predict
    result = model.predict(vector_input)

    # 4.display
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not spam")
