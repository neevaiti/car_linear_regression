# Car Price Estimation (Simplon Lille Project)

This project uses a Machine Learning model to estimate car prices based on their features. The model is based on the RandomForestRegressor from the Scikit-learn library and has been trained on a car dataset. 

## Prerequisites

To run this project, make sure you have the following libraries installed:

- Pandas

- Scikit-learn

- Streamlit


You can install these libraries using the following command: 

```
pip install pandas scikit-learn streamlit
```


## Running the Project

1. Clone this repository on your local machine.

2. Open a terminal and navigate to the project folder.

3. Run the Streamlit application using the following command:

```
streamlit run app.py
```

4. Open a web browser and navigate to the URL displayed in the console (usually `http://localhost:8501`).

5. Use the interface widgets to select the car features and click on the "Estimate Price" button to get a price estimation.


## Data

The dataset used to train the model can be found in the file `./src/car_dataset_cleaned.csv`. This file contains information about various car features, such as brand, model, fuel type, engine size, etc.


## Model

The trained RandomForestRegressor model is saved in the `model_car.pkl` file. You can load this file to make predictions on new data using Python's Pickle library.


## License

This project is released under the MIT license. See the `LICENSE` file for more information.
