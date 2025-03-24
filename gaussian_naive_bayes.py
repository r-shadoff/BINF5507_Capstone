import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report

# Example: Generate sample continuous data
df = pd.read_csv("/Users/rachel/Desktop/binf5507git/BINF5507/Capstone/Iris_Data.csv")
df.head()



