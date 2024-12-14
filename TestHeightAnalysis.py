import sys
import unittest
from unittest.mock import patch
from HeightAnalysis import *

class TestHeightAnalysis(unittest.TestCase):
    """
    Test suite for validating the functionality of the HeightAnalysis module.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class-level test data used across multiple tests.

        Parameters:
        cls.test_data: List[float]
            A list of generated height data with mean=170 and std_dev=10, size=1000.
        """
        cls.test_data = list(generate_height_data(size=1000, mean=170, std_dev=10))

    def test_generate_height_data(self):
        """
        Test the `generate_height_data` function for correct data generation.

        Asserts:
        - Generated data size matches the requested size.
        - All generated data points are of type float.

        Parameters:
        size: int
            Number of height data points to generate.
        mean: float
            Mean of the generated data.
        std_dev: float
            Standard deviation of the generated data.
        """
        data = list(generate_height_data(size=100, mean=180, std_dev=5))
        self.assertEqual(len(data), 100)
        self.assertTrue(all(isinstance(x, float) for x in data))

    def test_descriptive_statistics(self):
        """
        Test the `descriptive_statistics` function for accurate statistical calculations.

        Asserts:
        - Calculated mean matches NumPy's mean.
        - Calculated median matches NumPy's median.
        - Calculated standard deviation matches NumPy's std.

        Parameters:
        data: List[float]
            List of height data for statistical analysis.
        """
        mean, median, std_dev = descriptive_statistics(self.test_data)
        self.assertAlmostEqual(mean, np.mean(self.test_data), places=2)
        self.assertEqual(median, np.median(self.test_data))
        self.assertAlmostEqual(std_dev, np.std(self.test_data), places=2)

    def test_calculate_percentiles(self):
        """
        Test the `calculate_percentiles` function for accurate percentile calculation.

        Asserts:
        - Correct calculation of the 25th, 50th, and 75th percentiles.

        Parameters:
        data: List[float]
            List of height data for percentile calculation.
        """
        percentiles = list(calculate_percentiles(self.test_data))
        self.assertEqual(len(percentiles), 3)
        self.assertAlmostEqual(percentiles[0], np.percentile(self.test_data, 25), places=2)
        self.assertAlmostEqual(percentiles[1], np.percentile(self.test_data, 50), places=2)
        self.assertAlmostEqual(percentiles[2], np.percentile(self.test_data, 75), places=2)

    def test_identify_outliers(self):
        """
        Test the `identify_outliers` function for correct outlier identification.

        Asserts:
        - Detected outliers match manually calculated outliers using IQR.

        Parameters:
        data: List[float]
            List of height data to identify outliers.
        """
        outliers = identify_outliers(self.test_data)
        q1 = np.percentile(self.test_data, 25)
        q3 = np.percentile(self.test_data, 75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        expected_outliers = [x for x in self.test_data if x < lower_bound or x > upper_bound]
        self.assertEqual(outliers, expected_outliers)

    def test_random_sampling(self):
        """
        Test the `random_sampling` function for correct sample generation.

        Asserts:
        - Sample size matches the requested size.
        - All sampled data points exist in the original dataset.

        Parameters:
        data: List[float]
            Original dataset to sample from.
        size: int
            Number of data points in the sample.
        """
        sample = random_sampling(self.test_data, size=100)
        self.assertEqual(len(sample), 100)
        self.assertTrue(all(x in self.test_data for x in sample))

    @patch('builtins.print')
    def test_hypothesis_testing(self, mock_print):
        """
        Test the `hypothesis_testing` function for correct output.

        Asserts:
        - Output of the hypothesis test is printed correctly.

        Parameters:
        data: List[float]
            Dataset to test against the null hypothesis.
        null_hypothesis_mean: float
            Mean value of the null hypothesis to test against.
        """
        hypothesis_testing(self.test_data, null_hypothesis_mean=170)
        self.assertEqual(str(mock_print.call_args)[6], "D")

    def test_calculate_probability(self):
        """
        Test the `calculate_probability` function for accurate probability calculation.

        Asserts:
        - Calculated probability matches manual computation.

        Parameters:
        data: List[float]
            Dataset to calculate probability from.
        threshold_height: float
            Threshold height to calculate probability for.
        """
        threshold_height = 180
        probability = 100 * len([x for x in self.test_data if x > threshold_height]) / len(self.test_data)
        self.assertAlmostEqual(
            probability,
            100 * len([x for x in self.test_data if x > threshold_height]) / len(self.test_data),
            places=2
        )

if __name__ == "__main__":
    unittest.main()
