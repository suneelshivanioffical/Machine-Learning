# 🔐 Password Strength Prediction using Machine Learning

Weak passwords are one of the leading causes of online security breaches. Identifying password strength before it is used helps users create more secure passwords and reduces the risk of unauthorized access.

This model uses TF-IDF feature extraction with an XGBoost Classifier to predict password strength by analysing password patterns and classifying them into Weak, Medium, or Strong categories.

The model, trained on a large labelled password dataset, is deployed through a dockerized FastAPI backend, integrated with a responsive HTML, CSS, and JavaScript frontend host on Github pages, and backend hosted on Azure Web Services (Free tier).

---

## Demo

Link: https://suneelshivanioffical.github.io/Password_Strength_Predication/

![](https://github.com/suneelshivanioffical/Machine-Learning/blob/main/Password_Strength_Predication/Password_Strength_Predication_demo.gif)

---

## Dataset

```
https://github.com/suneelshivanioffical/Machine-Learning/tree/main/Password_Strength_Predication/data
```

The dataset contains 669,640 labelled passwords, where each password is assigned one of three strength categories. It is used to train a supervised machine learning model capable of predicting password strength based on character patterns and complexity.

The **password** column serves as the input feature, while the **strength** column is used as the target variable for classification.

Before training, password text data is transformed into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**, enabling the Machine Learning algorithm to identify hidden patterns and make accurate predictions.

The dataset distribution:

| Password Strength | Label |
|---|---|
| Weak Password | 0 |
| Medium Password | 1 |
| Strong Password | 2 |

## Project Structure

```
PASSWORD_STRENGTH_PREDICTION
│
├── backend
│   ├── app.py                               # FastAPI backend
│   ├── password_strength_predication.pkl    # Trained ML model
│   ├── tfidf_vectorizer.pkl                 # TF-IDF vectorizer
│   ├── Dockerfile                           # Docker configuration
│   ├── requirements.txt                     # Dependencies
│   └── .dockerignore                        # Docker ignore file
│
├── frontend
│   ├── index.html                           # Web interface
│   ├── style.css                            # UI styles
│   └── script.js                            # Frontend logic
│
├── notebook
│   └── Password_Strength_Predication.ipynb  # Model training
│
├── screenshots
│
└── README.md                                # Documentation
```
---

## Technologies

| Frontend  | Backend |
|---|---|
| HTML | FastAPI |
| CSS | Uvicorn |
| JavaScript | Pydantic |

| Machine Learning |  |
|---|---|
| Python | NumPy |
| Pandas | Scikit-learn |
| TF-IDF Vectorizer | XGBoost |
| Pickle |  |
|  |  |

| Deployment |  |
|---|---|
| Docker |  |
| Docker Hub |  |
| Azure Web Service |  |

## Model

```
TF-IDF + XGBoost Classifier
```

## Model Performance

The machine learning model was tested to evaluate how accurately it predicts password strength.

**Results**

- Accuracy: **98%**
- Test Samples: **133,928**

| Password Strength | Precision | Recall | F1 Score |
|-------------------|---------:|------:|---------:|
| Weak Password | 96% | 94% | 95% |
| Medium Password | 98% | 99% | 99% |
| Strong Password | 98% | 96% | 97% |

### What this means (Simple Explanation)

- The model correctly predicts password strength with **98% accuracy**.
- It accurately distinguishes between weak, medium, and strong passwords.
- Overall, it provides reliable real-time password strength predictions.

## Learning Outcomes

This project demonstrates:

This project demonstrates practical experience in:

- Machine Learning Classification
- Natural Language Processing (NLP)
- TF-IDF Feature Engineering
- XGBoost Classification
- FastAPI REST API Development
- Frontend & Backend Integration
- Docker Containerization
- Azure Cloud Deployment
- Production-ready ML Application

---

**Built with ❤️ using Python, FastAPI, XGBoost, TF-IDF, HTML, CSS, JavaScript, Docker, and Microsoft Azure.**
