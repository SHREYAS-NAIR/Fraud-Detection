import pandas as pd

def load_data():
    data = pd.read_csv("./Final_Transactions.csv")
    return data