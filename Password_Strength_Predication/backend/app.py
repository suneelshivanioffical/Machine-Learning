import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Load model and vectorizer
model = pickle.load(open("password_strength_predication.pkl", "rb"))
vectorizer = pickle.load(open("tfidf_vectorizer.pkl", "rb"))

# Create FastAPI app
app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Server is running!"}

class PasswordInput(BaseModel):
    password: str

@app.post("/predict")
def predict_strength(input: PasswordInput):

    # Convert password into TF-IDF features
    password_tfidf = vectorizer.transform([input.password])

    # Predict
    prediction = int(model.predict(password_tfidf)[0])

    # Convert result
    if prediction == 0:
        result = {
            "strength": "Weak Password",
            "score": 30,
            "emoji": "🔴"
        }

    elif prediction == 1:
        result = {
            "strength": "Medium Password",
            "score": 65,
            "emoji": "🟡"
        }

    else:
        result = {
            "strength": "Strong Password",
            "score": 100,
            "emoji": "🟢"
        }

    return result