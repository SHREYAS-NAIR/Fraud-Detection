import os
os.system("pip3 install -r requirements.txt")

import pandas as pd

def load_data():
    data = pd.read_csv("https://media.githubusercontent.com/media/SHREYASNAIR129/Fraud-Detection/master/Final_Transactions.csv")
    print(data.head())
    return data