import streamlit as st
import re
import numpy as np

print("Before importing tomotopy...")
import tomotopy as tp
print("After importing tomotopy...")

# Load the pre-trained PLDA model
plda = tp.PLDAModel.load('./plda_model.bin')

def get_topic(text):
    clean_txt = re.sub(r'[\W\d]+', ' ', text)
    clean_txt_utf8 = clean_txt.encode('utf-8').decode('utf-8')

    doc = plda.make_doc(words=clean_txt_utf8.split())
    infer_result = plda.infer(doc)

    if not infer_result or len(infer_result) == 0:
        return "No legal topic found."
    else:
        topic_probs, _ = infer_result
        max_topic_id = np.argmax(topic_probs)
        topic_label = plda.topic_label_dict[max_topic_id]
        return topic_label

def main():
    st.title("Legal Text Topic Predictor")

    text = st.text_area("Enter your legal text:")
    if st.button("Predict"):
        if text:
            topic = get_topic(text)
            st.write("Predicted Topic:", topic)
        else:
            st.write("Please enter some text.")

if __name__ == '__main__':
    main()
