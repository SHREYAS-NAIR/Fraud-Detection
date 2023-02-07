import seaborn
import matplotlib.pyplot as plt
import pandas as pd
from dataPreprocessing import data_preprocessing

def data_Visualization():
    data = pd.DataFrame(data_preprocessing())

    print("Visualizing the data.")
    #To visualize outliers
    seaborn.pairplot(data = data)
    plt.show()
