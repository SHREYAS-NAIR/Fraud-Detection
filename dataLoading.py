import pandas as pd

def load_data():
    data = pd.read_csv("https://media.githubusercontent.com/media/SHREYASNAIR129/Fraud-Detection/master/Final_Transactions.csv")
    return data