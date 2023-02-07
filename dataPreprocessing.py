from dataLoading import load_data
from dataAnalysis import data_Analysis
from imblearn.over_sampling import RandomOverSampler
import pandas as pd
import matplotlib.pyplot as plt


def data_preprocessing():
    #Analysing data before processing it.
    data_Analysis()

    #Loading data
    data = pd.DataFrame(load_data())
    
    print("Preprocessing the data.")
    #Droping null values
    print("Droping null values")
    data.dropna()
    print("Null values dropped")
    print(data.isnull().sum())

    #Dropping duplicate values
    print("Droping Duplicate values")
    data.drop_duplicates()
    print("Duplicates dropped")

    #Random Oversampling of majority class to balance data
    print("Oversampling to balance data")
    tx_fraud = data['TX_FRAUD']
    rus = RandomOverSampler(sampling_strategy="minority")
    new_balanced_data, new_tx_fraud = rus.fit_resample(data,tx_fraud)

    #Check the new balanced data
    print("Balanced data: \n",new_tx_fraud.value_counts())

    return(new_balanced_data)