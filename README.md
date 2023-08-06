# Telecom Churn Prediction Project

This project aims to predict customer churn in a telecom company using machine learning techniques. It includes two main parts: Exploratory Data Analysis (EDA) and Model Building. The project is designed to facilitate prediction for a single customer or a batch of customers by providing a CSV file for the batch.

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python (version 3.8)
- Streamlit (version 1.14.0)
- Pandas (version 1.4.3)
- Scikit-learn (version 1.0.2)

You can install the required dependencies using the following command:


## How to Run

To run the application, execute the following command in the terminal:

`streamlit run churnlytical.py`


This command will start the Streamlit application and open it in your default web browser(localhost:8501).

## Project Structure

The project is structured as follows:

- `churnlytical.py`: This is the main application file where Streamlit code is implemented to run the application.
- `Telco_churn_Analysis_EDA.ipynb`: This Jupyter Notebook contains Exploratory Data Analysis (EDA) of the telecom churn dataset.
- `Telco_churn_Analysis_Model_Building.ipynb`: This Jupyter Notebook contains the code for building and training the churn prediction models.

## How to Use

1. **EDA**: To explore the Exploratory Data Analysis (EDA) of the telecom churn dataset, refer to the `Telco_churn_Analysis_EDA.ipynb` notebook.

2. **Model Building**: To build and train the churn prediction models, refer to the `Telco_churn_Analysis_Model_Building.ipynb` notebook.

3. **Prediction**:
   - To predict churn for a single customer, use the Streamlit application (`churnlytical.py`). Input the customer's information, and the application will provide the churn prediction.
   - To predict churn for a batch of customers, prepare a CSV file in the format of the `sample.csv` provided. The CSV file should contain the customer information. Then, use the Streamlit application (`churnlytical.py`) to upload the CSV file and get the churn predictions for the batch.

## Dataset

The dataset used for this project can be found [here](https://github.com/menon123/Telecom-Churn-Predictor/blob/main/WA_Fn-UseC_-Telco-Customer-Churn.csv), and it contains the necessary information for training and testing the churn prediction models.


---
By following these instructions, you will be able to run the telecom churn prediction application and explore the provided Jupyter Notebooks for EDA and model building. The application will enable you to predict churn for individual customers or process a batch of customers using a CSV file.

