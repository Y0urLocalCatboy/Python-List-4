import pandas as pd
import matplotlib.pyplot as plt
import sns


def load_dataset_from_file(file_path):
    """
    Load the heart disease dataset from a CSV file.

    Parameters:
        file_path (str): Path to the CSV file containing the dataset.

    Returns:
        pd.DataFrame: Loaded dataset.
    """
    return pd.read_csv(file_path)

def gender_heart_disease(data):
    """
    Analyze whether more men or women suffer from heart diseases and calculate percentage.

    Parameters:
        data (pd.DataFrame): Heart disease dataset.
    """
    male_diseased = data[(data["Sex"] == "male") & (data["Disease"] == True)].shape[0]
    female_diseased = data[(data["Sex"] == "female") & (data["Disease"] == True)].shape[0]

    if male_diseased + female_diseased == 0:
        raise ValueError("No diseased individuals in the dataset.")

    male_percentage = (male_diseased / (male_diseased + female_diseased)) * 100
    female_percentage = (female_diseased / (male_diseased + female_diseased)) * 100

    print(f"Men with heart disease: {male_diseased} ({male_percentage:.2f}%)")
    print(f"Women with heart disease: {female_diseased} ({female_percentage:.2f}%)")
    print(f"More {'Men' if male_diseased > female_diseased else 'Women'} suffer from heart disease by "
          f"{abs(male_percentage - female_percentage):.2f}%")
def cholesterol_analysis(data):
    """
    Compare average cholesterol levels for men and women based on heart disease presence.

    Parameters:
        data (pd.DataFrame): Heart disease dataset.
    """
    avg_cholesterol = data.groupby(["Sex", "Disease"])["Serum cholesterol in mg/dl"].mean()
    print("Average Cholesterol Levels:")
    for (sex, disease), avg in avg_cholesterol.items():
        disease_status = "with disease" if disease else "without disease"
        print(f"{sex.capitalize()} {disease_status}: {avg:.2f} mg/dl")

def plot_age_histogram(data):
    """
    Plot a histogram of ages for individuals with heart diseases.

    Parameters:
        data (pd.DataFrame): Heart disease dataset.
    """
    diseased_data = data[data["Disease"] == True]
    plt.hist(diseased_data["Age"], bins=10, color='skyblue', edgecolor='black')
    plt.title("Age Distribution of Individuals with Heart Diseases")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()

def plot_max_heart_rate_boxplot(data):
    """
    Plot a boxplot of maximum heart rates grouped by heart disease presence.

    Parameters:
        data (pd.DataFrame): Heart disease dataset.
    """
    data["Disease Label"] = data["Disease"].apply(lambda x: "With Disease" if x else "Without Disease")
    data.boxplot(column="Maximum heart rate achieved", by="Disease Label", grid=False,)
    plt.title("Maximum Heart Rate by Disease Presence")
    plt.suptitle("") # To remove the automatically generated additional title
    plt.xlabel("Heart Disease")
    plt.ylabel("Maximum Heart Rate Achieved [bpm]")
    plt.show()

def plot_angina_heart_disease_bar_chart(data):
    """
    Plot a bar chart of heart disease frequency based on frequency of heart disease occurrence depending on whether
the patient has angina during the exercise test.

    Params:
        data (pd.DataFrame): Heart disease dataset.
    """
    angina_disease_data = data.groupby("Exercise induced angina")["Disease"].sum()
    angina_disease_data.plot(kind='bar', color=['green', 'red'], legend=True)
    plt.title("Heart Disease Frequency by Exercise-Induced Angina")
    plt.xlabel("Exercise-Induced Angina (0 = No, 1 = Yes)")
    plt.ylabel("Heart Disease Cases")
    plt.show()

file_path = "heart_disease_dataset.csv"
heart_data = load_dataset_from_file(file_path)

print("Task 1:")
gender_heart_disease(heart_data)

print("Task 2:")
cholesterol_analysis(heart_data)

print("Task 3: Age Histogram, The most people with heart disease are between 50 and 60 years old")
plot_age_histogram(heart_data)

print("Task 4: Max Heart Rate BoxplotPeople with heart disease tend to achieve a lower maximum heart rate during exercise compared to those without it. The median is lower, and there are more low outliers in the With Disease group. This suggests reduced cardiovascular performance")
plot_max_heart_rate_boxplot(heart_data)

print("Task 5: Angina and Heart Disease Bar Chart, Most people with heart disease didn't experience angina during exercise. But for those who did, it still counts, even though they’re fewer. So, exercise-induced angina isn’t the rule, but it might be a hint of something.")
plot_angina_heart_disease_bar_chart(heart_data)
