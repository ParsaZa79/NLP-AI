import streamlit as st
from transformers import pipeline

# Load the summarization pipeline with a different model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Streamlit app
st.title("Text Summarization App")

st.write("Enter the text you want to summarize:")

# Text input
input_text = st.text_area("Input Text", height=200)

# Summarize button
if st.button("Summarize"):
    if input_text:
        # Perform summarization
        summary = summarizer(input_text, max_length=150, min_length=30, do_sample=False)
        st.write("Summary:")
        st.write(summary[0]['summary_text'])
    else:
        st.write("Please enter some text to summarize.")