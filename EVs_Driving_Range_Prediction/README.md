## EVs Driving Range Prediction - Regression

Electric vehicle (EV) buyers often want to know: "How far can an electric vehicle travel on a single charge based on its battery capacity?"

As the demand for electric vehicles continues to grow, accurately estimating driving range has become increasingly important for manufacturers and consumers alike. This project develops a Simple Linear Regression model that predicts an electric vehicle's driving range using its battery capacity as the primary feature.

## Dataset

Electric Vehicle Specs Dataset (2025)

```
https://www.kaggle.com/datasets/urvishahir/electric-vehicle-specifications-dataset-2025
```
## Technologies

- Python
- Pandas
- NumPy
- Scikit-Learn
- Pickle

## Model

Linear Regression

## Model Performance

The machine learning model was tested to see how well it can predict the driving range of electric vehicles.

Results:

- Average prediction error: about 37 km
- Model accuracy (R² Score): 77%
- Mean Squared Error: 2405.01 

### What this means (Simple Explanation)

- The prediction can be about **37 km above or below** the actual driving range.
- The model understands about **77% of the pattern** between battery size and driving range.
- This means the model can make good predictions using only the battery size.
- In most cases, a bigger battery means the vehicle can travel farther, and the model learned this relationship from the data.

#### Thanks for following through.

------------------------------------------------------------------------------------------------------------------

