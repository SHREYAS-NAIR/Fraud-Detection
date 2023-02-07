from featureSelection import feature_selection
from sklearn.model_selection import train_test_split
import pandas as pd

def data_Spliting():
    data = pd.DataFrame(feature_selection())

    print("Splitting the data.")
    # Assigning the featurs as X and trarget as y
    X= data.drop(["TX_FRAUD"],axis =1)
    y= data["TX_FRAUD"]
    x_train, x_test, y_train, y_test = train_test_split(X, y,test_size=0.25, random_state=7)
    return (x_train, x_test, y_train, y_test)