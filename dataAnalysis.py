from dataLoading import load_data
import pandas as pd

def data_Analysis():
    data=pd.DataFrame(load_data())
    
    print("Analysing Data")

    #Changing values from scientific notation to much readable notation
    print("Improving data readability")
    pd.set_option('display.float_format', '{:.2f}'.format)

    #First look at the data
    print("Thease are the first 5 rows of data set.")
    print(data.head())

    #Data types
    print("Observing the data types in the dataset.")
    print(data.info())

    #Data set description
    print("Description of the dataset.")
    print(data.describe())

    #Data set null values observation
    print("Sum of null values in the dataset.")
    print(data.isnull().sum())

    #Duplicates in the dataset
    print("Duplicates in the data are: ",data.duplicated().sum())

    #Checking imbalance in data
    tx_fraud = data['TX_FRAUD']
    print("Imbalanced data: \n",tx_fraud.value_counts())