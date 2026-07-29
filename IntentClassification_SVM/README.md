# Intent Classification using Machine Learning

Businesses receive thousands of customer messages every day through emails, chatbots, and support systems. Automatically identifying the intent behind these messages helps organisations route requests efficiently, improve response times, and enhance customer support.

This model uses Sentence-BERT embeddings with a Linear Support Vector Machine (LinearSVC) classifier to predict the intent of customer messages, such as complaints, feedback, enquiries, and support requests with Confidence Score.

The model, trained on synthesized labelled customer intent data, is deployed as an interactive Streamlit web application.

## Demo

Link:

![]()

## Dataset

Customer Intent Classification Dataset

```
IntentClassification_SVM\data\intent_classification_dataset (1).xlsx
```

## Project Structure

```
INTENTCLASSIFICATION_SVM
│
├── data
│   └── intent_classification_dataset.xlsx      # Dataset
│
├── models
│   └── Intentsclassification.pkl               # Trained ML model
│
├── notebook
│   └── IntentClassification_SVM.ipynb          # Model Training
│
├── app.py                                      # Streamlit UI
├── style.css                                   # Custom UI styling
├── requirements.txt                            # Dependencies
└── README.md                                   # Project documentation
```

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Sentence-Transformers
- Sentence-BERT
- LinearSVC
- Streamlit UI
- Pickle

## Model

```
Sentence-BERT + LinearSVC(SVM)
```

## Model Performance

The machine learning model was tested to see how well it can classify customer messages.

Results:

- Accuracy: 99.8%
- Embedding Model: Sentence-BERT
- Classifier: LinearSVC

What this means (Simple Explanation)

- The model correctly classifies almost every customer message.
- It understands the meaning of text using Sentence-BERT embeddings.
- Overall, it provides highly accurate intent predictions for customer messages.

---

## Further Work Done

Beyond the direct deployment on Streamlit Cloud for Portfolio, the following work was also completed:

- Developed a FastAPI backend to serve the ML model.
- Containerized the backend using Docker and pushed it to Azure Container Apps.
- Deployed the Dockerized application to Azure Web Services.
- Removed Azure resources after deployment to avoid unnecessary Cloud costs.

---

## Learning Outcome

This project demonstrates practical experience in:

- Natural Language Processing (NLP)
- Sentence Embeddings
- Sentence-BERT
- Text Classification
- Support Vector Machines (LinearSVC)
- Machine Learning Pipelines
- Web Application Development
- Deployment on Streamlit Cloud for Portfolio
- FastAPI REST API Development
- Frontend & Backend Integration
- Docker Containerization
- Azure Cloud Deployment
- Production-ready NLP Application

---

**Built with ❤️ using Python, Sentence-BERT, LinearSVC, Scikit-learn, Streamlit, FastAPI, Docker, and Azure Cloud.**
