# Shipping Cost Prediction using Machine Learning

Businesses involved in trade often need to estimate shipping costs before a shipment is dispatched. Accurate cost prediction helps freight forwarders, logistics providers, exporters, and importers improve budgeting, pricing strategies, and operational planning. 

This model uses a Gradient Boosting Regressor to predict shipping costs based on key shipment information such as trade direction, cargo type, ports, Incoterms, vessel type, cargo volume, and transit days

The model trained on historical maritime trade data, is deployed as an interactive Streamlit web application.

## Demo

Link: 
![](https://github.com/suneelshivanioffical/Machine-Learning/blob/main/Shipping_Cost_Predication/shippingCost-ui-demo.png)

## Dataset

Pakistan Maritime Trade Dataset (2020–2026)

```
https://www.kaggle.com/datasets/hammadansari7/pakistan-maritime-trade-and-shipping-dataset
```

## Project Structure

```
SHIPPING_COST_PREDICTION
│
├── data
│   └── pakistan_maritime_trade_2020_2026.csv    # Dataset
│
├── models
│   ├── ShippingCostPredication.pkl              # Trained ml model
│   └── encoder.pkl                              # Label encoder for categorical features
│
├── notebook
│   └── Shipping Cost Predication.ipynb          # Model Training
│
├── app.py                                       # Streamlit UI
├── style.css                                    # Custom UI styling
├── requirements.txt                             # Dependencies
└── README.md                                    # Project documentation
```

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit UI
- Pickle

## Model

```
Gradient Boosting Regressor
```

## Model Performance


The machine learning model was tested to see how well it can predict shipping cost.

Results:

- R² Score: 74.2%
- Average Prediction Error (MAE): 32.85
- Root Mean Squared Error (RMSE): 39.47

What this means (Simple Explanation)

- On average, the predicted shipping cost differs from the actual cost by about 33 units.
- The model explains approximately 74% of the factors affecting shipping costs.
- Overall, it provides reliable estimates for shipping cost prediction.

---

## Learning Outcome

This project demonstrates practical experience in:

- Machine Learning Regression
- Data Preprocessing
- Feature Engineering
- Label Encoding
- Model Evaluation
- Streamlit Application Development
- Deployment on Streamlit Cloud for Portfilo
- FastAPI REST API Development
- Frontend & Backend Integration
- Docker Containerization
- Azure Cloud Deployment
- Production-ready ML Application

---

## Further Work Done

Beyond the direct deployment on Streamlit Cloud for Portfolio, the following work was also completed:

- Developed a FastAPI backend to serve the ML model.
- Containerized the backend using Docker and push to the Azure Container App Services.
- Deployed the Dockerized application to Azure Web Services.
- Removed Azure resources after deployment to avoid unnecessary cloud costs.

---

**Built with ❤️ using Python, FastAPI, Scikit-learn, Gradient Boosting Regressor, Streamlit, Docker and Azure Cloud.**
