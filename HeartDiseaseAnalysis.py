import pandas as pd
heart_disease_data = pd.read_csv('heart_disease_dataset.csv')

male_data = heart_disease_data[heart_disease_data["Sex"] == "male"]
female_data = heart_disease_data[heart_disease_data["Sex"] == "female"]

male_diseased_data = male_data[male_data["Disease"] == True]
female_diseased_data = female_data[female_data["Disease"] == True]

male_healthy_data = male_data[male_data["Disease"] == False]
female_healthy_data = female_data[female_data["Disease"] == False]
#print(male_healthy_data.head())
if male_diseased_data.count()[1] > female_diseased_data.count()[1]:
    print("More man than women have heart disease")
elif male_diseased_data.count()[1] == female_diseased_data.count()[1]:
    print("They are equal in their heart disease")
else:
    print("More woman than men have heart disease")


print(male_healthy_data.sort_values(by="Serum cholesterol in mg/dl", ascending=False).describe())