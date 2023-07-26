from flask import Flask, render_template, request, jsonify
import tomotopy as tp
import re
import numpy as np

app = Flask(__name__, static_folder='static')

# Load the pre-trained PLDA model
plda = tp.PLDAModel.load('./plda_model.bin')


def debug_function(input_text):
    # Some debug information
    print("Debug Information:")
    print("Input Text:", input_text)

    # Process the input text and return a result
    if "hello" in input_text.lower():
        result = "The input text contains 'hello'."
    else:
        result = "The input text does not contain 'hello'."

    return result


def get_topic(text):
    clean_txt = re.sub(r'[\W\d]+', ' ', text)
    clean_txt_utf8 = clean_txt.encode('utf-8').decode('utf-8')
    print("Clean Text:", clean_txt_utf8)

    doc = plda.make_doc(words=clean_txt_utf8.split())
    infer_result = plda.infer(doc)

    if not infer_result or len(infer_result) == 0:
        return "No legal topic found."
    else:
        # Extract the topic probabilities and log-likelihood value from the tuple
        topic_probs, log_likelihood = infer_result

        max_prob = 0.0
        max_topic_id = -1
        for topic_id, prob in enumerate(topic_probs):
            if prob > max_prob:
                max_prob = prob
                max_topic_id = topic_id

        if max_topic_id < 0:
            return "No legal topic found."
        else:
            topic_label = plda.topic_label_dict[max_topic_id]
            return topic_label


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        if text:
            topic = get_topic(text)
            return render_template('index.html', topic=topic, text=text)
    return render_template('index.html', topic=None, text=None)


# Route to handle the prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        text = data.get('text')
        if text:
            topic = get_topic(text)
            return jsonify({'topic': topic})
        else:
            return jsonify({'topic': 'No legal topic found.'})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'topic': 'Error occurred during prediction.'})



if __name__ == '__main__':
    app.run(debug=True)