Legal Topic Classifier - Flask Web App

Description
app.py" is the main script of my web application, which serves as a Hebrew-based Legal Topic Classifier. The purpose of this application is to analyze input text written in Hebrew and determine its legal topic based on a pre-trained Probabilistic Latent Dirichlet Allocation (PLDA) model. The model has been trained on a large dataset of Hebrew legal texts and is capable of assigning topics to Hebrew text based on the most probable legal topic.

Upon receiving input text, the application preprocesses the text by removing any non-alphabetic characters and then passes it through the PLDA model to infer the topic. The model outputs a probability distribution over different legal topics, and the application selects the topic with the highest probability as the final classification.

The Legal Topic Classifier web app offers both a web interface and an API endpoint for easy integration with other applications. Users can input text through the web interface to receive instant topic classification results. Additionally, developers can leverage the API to integrate the classifier into their own applications and obtain topic predictions programmatically.

Overall, this Legal Topic Classifier demonstrates the potential of utilizing machine learning and natural language processing in the legal domain. It demonstrates how this technology can be used as an efficient tool for organizing and analyzing legal text.

Installation
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

Note: The Legal Topic Classifier is intended for experimental purposes only and may require further refinement for production use.

Usage
Explain how to use the Legal Topic Classifier web app. Provide instructions on how to access the web app, how to input legal text, and how to get the predicted legal topic.

Model
If relevant, you can provide more information about the PLDA model used for classification. You can mention how it was trained, what data it was trained on, and any other relevant details about the model.

Dependencies
Flask==2.0.1
tomotopy==0.11.1
numpy==1.19.5
License
Include the license information for your project. Specify the type of license (e.g., MIT License, Apache License) and include a copy of the license in the repository.

Contact
feel free to reach me at orenabareket123@gmail.com

Acknowledgments
If you have received help or used any resources in your project, you can acknowledge them in this section.
