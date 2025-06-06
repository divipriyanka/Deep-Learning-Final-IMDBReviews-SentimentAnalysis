import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import json
import numpy as np

model = load_model("best_gru_model.h5")

with open("tokenizer.json", "r") as f:
    tokenizer_json = f.read() 
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(tokenizer_json)

MAX_SEQUENCE_LENGTH = 20

def predict_sentiment(review):
  # tokenize and pad the review
  sequence = tokenizer.texts_to_sequences([review])
  padded_sequence = pad_sequences(sequence, maxlen=200)
  prediction = model.predict(padded_sequence)
  sentiment = "positive" if prediction[0][0] > 0.5 else "negative"
  return sentiment

def main():
    st.title('Sentiment Analysis App')

    user_input = st.text_area("Enter the text you'd like to analyze for sentiment:")

    if st.button('Analyze'):
        sentiment = predict_sentiment(user_input)
        st.write(f"The sentiment of the review is: {sentiment}")
        #print(f"The sentiment of the review is: {sentiment}")
        
if __name__ == "__main__":
    main()
