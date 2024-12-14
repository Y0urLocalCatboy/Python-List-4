import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp

def generate_height_data(size=1000, mean=170, std_dev=10):
    """
    Generates a dataset of heights based on a normal distribution.

    Parameters:
    size (int): The number of data points to generate. (Default 1000)
    mean (float): The mean value of the distribution. (Default 170)
    std_dev (float): The standard deviation of the distribution. (Default 10)

    Yields:
    float: A randomly generated height value rounded to two decimal places (for the sake of readability).

    Returns: A list of randomly generated height values rouden to two decimal places.
    """
    for i in range(size):
        yield round(np.random.normal(mean, std_dev), 2)  # Rounding to 2 decimal places for better readability

height_data = list(generate_height_data())

def descriptive_statistics(height_data):
    """
    Creates descriptive statistics for a given dataset of heights.

    Parameters:
    height_data (list of floats): The dataset of height values.

    Returns:
    tuple: A tuple containing the mean (rounded to two decimal places), median, and standard deviation (rounded to two decimal places) of the data.
    """
    mean = np.mean(height_data)
    median = np.median(height_data)
    std_dev = np.std(height_data)
    return round(mean, 2), median, round(std_dev, 2)

def visualise_histogram(height_data):
    """
    Visualizes the distribution of height data as a histogram.

    Parameters:
    height_data (list of float): The dataset of height values.

    Returns:
    None (but creates a histogram).
    """
    plt.hist(height_data, bins=90, color='white', edgecolor='red')
    plt.title('height_data')
    plt.show()

def calculate_percentiles(height_data):
    """
    Calculates specified percentiles of the height data.

    Parameters:
    height_data (list of float): The dataset of height values.

    Yields:
    float: The value at each calculated percentile.

    Returns:
    A list of floats, values at each percentile.
    """
    for i in range(25, 76, 25): # Why up to 76? Because it's 25 50 75
        yield round(np.percentile(height_data, i),2)

def identify_outliers(height_data):
    """
    Identifies outliers in the dataset using the IQR method.

    Parameters:
    height_data (list of float): The dataset of height values.

    Returns:
    list of float: A list of outlier values.
    """
    q1 = list(calculate_percentiles(height_data))[0]
    q3 = list(calculate_percentiles(height_data))[2]
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    return [x for x in height_data if x < lower_bound or x > upper_bound]

def random_sampling(height_data, size=50):
    """
    Selects a random sample from the height data.

    Parameters:
    height_data (list of float): The dataset of height values.
    size (int): The number of samples to select. Default is 50.

    Returns:
    numpy.ndarray: An array of randomly selected height values.
    """
    return np.random.choice(height_data, size=size)

def hypothesis_testing(height_data, null_hypothesis_mean=170):
    """
    Performs hypothesis testing on a random sample of the height data.

    Parameters:
    height_data (list of float): The dataset of height values.
    null_hypothesis_mean (float): The mean value for the null hypothesis. Default is 170.

    Returns:
    tuple: A tuple containing the t-statistic (rounded to two decimal places) and the p-value (rounded to two decimal places).
    """
    sample = random_sampling(height_data)
    t_statistic, p_value = ttest_1samp(sample, null_hypothesis_mean)
    if p_value < 0.05:
        print(f"Reject the null hypothesis: t-statistic = {t_statistic}, p-value = {p_value}")
    else:
        print(f"Don't reject the null hypothesis: t-statistic = {t_statistic}, p-value = {p_value}")
    return round(t_statistic, 2), round(p_value, 2)

def calculate_probability(data, threshold_height=180):
    """
    Calculates the probability of a height being above a given threshold.

    Parameters:
    data (list of float): The dataset of height values.
    threshold_height (float): The threshold height to calculate the probability for. (Default 180)

    """
    print(f"{100 * len([x for x in data if x > threshold_height]) / len(height_data)}% of the population is taller than {threshold_height} cm")

print(identify_outliers(height_data))
hypothesis_testing(height_data)
print(descriptive_statistics(height_data))
calculate_probability(height_data)
