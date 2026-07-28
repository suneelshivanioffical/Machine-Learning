# 🔐 Password Strength Prediction using Machine Learning

An end-to-end Machine Learning application that predicts password strength in real-time. The system analyzes password patterns using **TF-IDF feature extraction** and an **XGBoost classification model** to classify passwords into:

- Weak Password
- Medium Password
- Strong Password

Creating strong passwords is essential for online security. This project uses Machine Learning to evaluate password complexity and provide instant feedback while users type.

The application provides:

- Real-time password strength prediction  
- Password checklist validation  
- Strength score visualization  
- ML-powered prediction API  
- Production-ready deployment architecture  


The trained ML model is deployed through a **FastAPI backend**, connected with a responsive **HTML, CSS, and JavaScript frontend**, and hosted using **Docker on Azure Web Service**.


---

## Demo

Link: https://suneelshivanioffical.github.io/Password_Strength_Predication/

![](https://github.com/suneelshivanioffical/Machine-Learning/blob/main/Password_Strength_Predication/Password_Strength_Predication_demo.gif)

---

## Dataset

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
│   ├── app.py
│   ├── password_strength_predication.pkl
│   ├── tfidf_vectorizer.pkl
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── frontend
│   ├── index.html
│   ├── style.css
│   ├── script.js  
│
├── notebook
│   └── Password_Strength_Predication.ipynb
│
├── screenshots
│
└── README.md
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


## Model Performance

| Metric | Score |
|---|---|
| Accuracy | **98%** |
| Test Samples | **133,928** |


| Password Strength | Precision | Recall | F1 Score |
|---|---:|---:|---:|
| Weak Password | 96% | 94% | 95% |
| Medium Password | 98% | 99% | 99% |
| Strong Password | 98% | 96% | 97% |

The XGBoost classifier demonstrates excellent generalisation across all three password strength classes.

- Weak Password: High precision ensures insecure passwords are detected accurately.
- Medium Password: Achieves the highest overall performance with an F1-score of 99%.
- Strong Password: Correctly identifies highly secure passwords with an F1-score of 97%.

Overall, the model achieves 98% accuracy on 133,928 unseen test samples, making it suitable for real-time password strength prediction applications.

## Learning Outcomes

This project demonstrates:

- Machine Learning Classification
- Feature Engineering with TF-IDF
- FastAPI REST API Development
- Frontend & Backend Integration
- Docker Containerization
- Azure Cloud Deployment
- Production-ready ML Application

---

**Built with ❤️ using Python, FastAPI, XGBoost, TF-IDF, Docker, and Microsoft Azure.**
