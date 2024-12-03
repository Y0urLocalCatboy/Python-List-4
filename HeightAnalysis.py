import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp


def generate_height_data(size = 1000, mean = 170, std_dev = 10):
    for i in range(size):
         yield round(np.random.normal(mean, std_dev),2) # Rounding to 2 decimal places for better readability
height_data = list(generate_height_data())


def descriptive_statistics(height_data):
    mean = np.mean(height_data)
    median = np.median(height_data)
    std_dev = np.std(height_data)
    return round(mean,2), median, round(std_dev,2)
def visualise_histogram(height_data):
    plt.hist(height_data, bins = 90, color = 'white', edgecolor = 'red')
    plt.title('height_data')
    plt.show()
def calculate_percentiles(height_data):
    for i in range(25, 76, 25):
        yield np.percentile(height_data, i)
def identify_outliers(height_data):
    q1 = list(calculate_percentiles(height_data))[0]
    q3 = list(calculate_percentiles(height_data))[2]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in height_data if x < lower_bound or x > upper_bound]
def random_sampling(height_data, size = 50):
    return np.random.choice(height_data, size = size)
def hypothesis_testing(height_data, null_hypothesis_mean = 170):
    sample = random_sampling(height_data)
    t_statistic, p_value = ttest_1samp(sample, null_hypothesis_mean)
    if p_value < 0.05:
        print(f"Reject the null hypothesis: t-statistic = {t_statistic}, p-value = {p_value}")
    else:
        print(f"Don't reject the null hypothesis: t-statistic = {t_statistic}, p-value = {p_value}")
    return round(t_statistic,2), round(p_value,2)
def calculate_probability(data, threshold_height = 180):
    print(f"{100*len([x for x in data if x > threshold_height]) / len(height_data)}% of the population is taller than {threshold_height} cm")

print(identify_outliers(height_data))
hypothesis_testing(height_data)
print(descriptive_statistics(height_data))
calculate_probability(height_data)