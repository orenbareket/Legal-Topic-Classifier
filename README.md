# Legal Topic Classifier - Streamlit Web App

## Description

"app.py" is the main script of this web application, serving as a Hebrew-based Legal Topic Classifier. This application aims to analyze input text written in Hebrew and determine its legal topic using a pre-trained Probabilistic Latent Dirichlet Allocation (PLDA) model. The model has undergone training on an extensive dataset of Hebrew legal texts, enabling it to assign topics to Hebrew texts based on the most probable legal topic.

### Transition to Streamlit

Recently, I transitioned this application from Flask to Streamlit, a powerful Python library for creating web apps for data science and machine learning. This transition simplifies the user interface and enhances user interaction.

## Usage

To get started with the Legal Topic Classifier, please visit [Legal Topic Classifier on Streamlit](https://legal-topic-classifier.streamlit.app/).

## Dependencies

- streamlit==1.26.0
- tomotopy==0.12.5
- numpy==1.24.4

## Experimenting and Analyzing

Feel free to try different legal texts and explore the various predicted legal topics the app provides. Please note that the Legal Topic Classifier model used in this experiment is trained to predict the following legal topics:

- Inheritance Rights
- Renting ("שכירות")
- Marriage and Divorce ("נישואין וגירושין")
- Nuisances ("מטרדים")
- Discrimination ("אפליה")
- Defamation ("לשון הרע")
- Medical Malpractice ("רשלנות רפואית")
- Privacy ("פרטיות")
- Child Support ("מזונות ילדים")

Note: Feel free to input legal text related to any of these topics and explore the model's predictions. This is an experimental model and may not cover all possible legal scenarios accurately. It is intended for experimental purposes only.

## Contact

If you have any questions or feedback, please feel free to reach me at [orenabareket123@gmail.com](mailto:orenabareket123@gmail.com).

Enjoy using the new and improved Legal Topic Classifier powered by Streamlit!
