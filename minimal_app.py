import streamlit as st
import spacy

# Load a pre-trained spaCy model for Hebrew
nlp = spacy.load("he_core_news_sm")

def main():
    st.title("Legal Text Topic Predictor")

    text = st.text_area("Enter your legal text:")
    if st.button("Predict"):
        if text:
            doc = nlp(text)
            tokens = [token.text for token in doc]
            st.write("Tokens:", tokens)
        else:
            st.write("Please enter some text.")

if __name__ == '__main__':
    main()
