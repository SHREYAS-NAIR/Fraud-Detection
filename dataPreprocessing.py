from dataLoading import load_data
import pandas as pd
from imblearn.over_sampling import RandomOverSampler

def data_preprocessing():
    #Loading data
    data = pd.DataFrame(load_data())

    #To visualize outliers
    #seaborn.pairplot(data = data)
    #plt.show()

    #Changing values from scientific notation to much readable notation
    pd.set_option('display.float_format', '{:.2f}'.format)

    #Removing outliers and unwanted columns
    data = data.drop(['Unnamed: 0'], axis=1, inplace=True)
    data = data.drop(['TX_DATETIME'], axis=1)
    data = data[(data["TX_AMOUNT"]<75000)]

    #Checking imbalance in data
    tx_fraud = data['TX_FRAUD']
    print("Imbalanced data: \n",tx_fraud.value_counts())

    #Random Oversampling of majority class to balance data
    rus = RandomOverSampler(sampling_strategy="minority")
    new_balanced_data, new_tx_fraud = rus.fit_resample(data,tx_fraud)

    #Check the new balanced data
    print("Balanced data: \n",new_tx_fraud.value_counts())

    return(new_balanced_data)