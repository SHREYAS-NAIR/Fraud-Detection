from featureEngineering import feature_Engineering
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt

def feature_selection():
    data = pd.DataFrame(feature_Engineering())
    
    print("Feature selection based on corelation matrix")
    #Checking corelation matrix for essential features.
    corr_matrix = data.corr()
    sn.heatmap(corr_matrix, annot=True)
    plt.show()

    #Droping Columns that have very less corelation
    data = data.drop(['TRANSACTION_ID'], axis=1)
    data = data.drop(['CUSTOMER_ID'], axis=1)
    data = data.drop(['TERMINAL_ID'], axis=1)

    return data

    