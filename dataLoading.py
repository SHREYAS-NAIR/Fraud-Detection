from installingRequirements import installing_requirements
import pandas as pd

def load_data():
    installing_requirements()
    print("Loading data.")
    data = pd.read_csv("https://media.githubusercontent.com/media/SHREYASNAIR129/Fraud-Detection/master/Final_Transactions.csv")
    return data