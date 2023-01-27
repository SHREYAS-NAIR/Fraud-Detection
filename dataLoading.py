import os
import pandas as pd

os.system("pip3 install pandas") #-r requirements.txt

def load_data():
    data = pd.read_csv("./Final_Transactions.csv")
    return data