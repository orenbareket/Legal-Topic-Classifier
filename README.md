Legal Topic Classifier - Flask Web App

Description:

"app.py" is the main script of this web application, serving as a Hebrew-based Legal Topic Classifier. The purpose of this application is to analyze input text written in Hebrew and determine its legal topic using a pre-trained Probabilistic Latent Dirichlet Allocation (PLDA) model. The model has undergone training on an extensive dataset of Hebrew legal texts, enabling it to assign topics to Hebrew text based on the most probable legal topic.

Upon receiving input text, the application preprocesses the text by removing any non-alphabetic characters. It then passes the text through the PLDA model to infer the topic. The model generates a probability distribution over different legal topics, and the application selects the topic with the highest probability as the final classification.

The Legal Topic Classifier web app provides both a web interface and an API endpoint, allowing easy integration with other applications. Users can input text through the web interface to receive instant topic classification results. Additionally, developers can leverage the API to integrate the classifier into their own applications and obtain topic predictions programmatically.

Overall, this Legal Topic Classifier showcases the potential of machine learning and natural language processing in the legal domain. It demonstrates how this technology can efficiently organize and analyze legal text.

Installation:

To get started with the Legal Topic Classifier, follow these steps:

Clone the Repository:
bash
Copy code
git clone https://github.com/your-username/legal-topic-classifier.git
Replace "your-username" with your actual GitHub username.

Navigate to the Project Directory:
bash
Copy code
cd legal-topic-classifier
Create and Activate Virtual Environment (Optional but Recommended):
bash
Copy code
python -m venv venv
On Windows:

bash
Copy code
venv\Scripts\activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install Required Dependencies:
bash
Copy code
pip install -r requirements.txt
Load Pre-trained Model:
Before running the application, make sure to place the "plda_model.bin" file in the project directory.

Run the Application:
bash
Copy code
python app.py
Access the Application:

Open your web browser and go to http://localhost:5000 to interact with the Legal Topic Classifier.

Note: The Legal Topic Classifier is intended for experimental purposes only.

Using the Web App:

Once the app is running, you can access it through your web browser.

Inputting Legal Text:

In the designated text area, input any day-to-day real-life scenario involving legal issues that you wish to analyze.

Getting the Predicted Legal Topic:

After entering the legal text, click on the "Submit" button to analyze the input. The Legal Topic Classifier will process the text and predict the most relevant legal topic for the input. The predicted legal topic will be displayed on the web page.

Interpreting the Result:

The app will provide you with a predicted legal topic that best fits the input text. The result might include categories like "Contract Law," "Family Law," "Property Law," etc. Note that the result is based on machine learning algorithms and may not be 100% accurate, especially for complex legal scenarios.

Experimenting and Analyzing:

Feel free to try different legal texts and explore the various predicted legal topics the app provides. Please note that the Legal Topic Classifier model used in this experiment is trained to predict the following legal topics:

Inheritance Rights
Renting ("שכירות")
Marriage and Divorce ("נישואין וגירושין")
nuisances ("מטרדים")
Discrimination ("אפליה")
Defamation ("לשון הרע") 
Medical Malpractice ("רשלנות רפואית")
Privacy ("פרטיות") 
Child Support ("מזונות ילדים")
Feel free to input legal text related to any of these topics and explore the model's predictions. Note that this is an experimental model and may not cover all possible legal scenarios accurately.

Model:

The core component of the Legal Topic Classifier is the "plda_model.bin" file, which contains the pre-trained Probabilistic Latent Dirichlet Allocation (PLDA) model. This model is the result of extensive training on a diverse dataset of legal texts in Hebrew. By leveraging the power of natural language processing and machine learning, the model can accurately identify and categorize legal topics based on the input text.

Dependencies:

Flask==2.0.1
tomotopy==0.11.1
numpy==1.19.5

Contact:

For any inquiries or feedback, please feel free to reach me at orenabareket123@gmail.com.
