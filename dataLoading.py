import os
os.system("pip3 install -r requirements.txt")

import pandas as pd

def load_data():
    data = pd.read_csv("./Final_Transactions.csv")
    print(data.head())
    print(data.columns)
    return data

load_data()