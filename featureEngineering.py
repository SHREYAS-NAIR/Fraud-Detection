from dataPreprocessing import data_preprocessing
from dataVisualization import data_Visualization
import pandas as pd

def feature_Engineering():
    #Visualizing data
    data_Visualization()

    data = pd.DataFrame(data_preprocessing())

    print("Feature Engineering.")
    #Removing outliers and unwanted columns
    print("Removing outliers and unwanted columns")
    data = data.drop(['Unnamed: 0'], axis=1)
    data = data.drop(['TX_DATETIME'], axis=1)
    data = data[(data["TX_AMOUNT"]<75000)]
    
    return data