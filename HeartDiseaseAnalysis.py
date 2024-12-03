import pandas as pd
heart_disease_data = pd.read_csv('heart_disease_dataset.csv')
print(heart_disease_data.head())
print(heart_disease_data.describe())
