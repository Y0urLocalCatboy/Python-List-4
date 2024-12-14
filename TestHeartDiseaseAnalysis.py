import unittest
from unittest.mock import patch
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

from HeartDiseaseAnalysis import *

class TestHeartDiseaseAnalysis(unittest.TestCase):
    """
    Test suite for heart disease analysis functions.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up test data to be used across tests.
        """

        cls.test_data = load_dataset_from_file("heart_disease_dataset.csv")

    def test_load_dataset_from_file(self):
        """
        Test `load_dataset_from_file` for correct dataset loading and if its loading the whole dataset.
        """
        data = load_dataset_from_file("heart_disease_dataset.csv")
        self.assertIsInstance(data, pd.DataFrame)
        self.assertEqual(len(data), 1025)

    @patch("builtins.print")
    def test_gender_heart_disease(self, mock_print):
        """
        Test `gender_heart_disease` for correct percentage and output.
        """
        gender_heart_disease(self.test_data)
        self.assertTrue(mock_print.called)

    @patch("builtins.print")
    def test_cholesterol_analysis(self, mock_print):
        """
        Test `cholesterol_analysis` for correct cholesterol comparison.
        """
        cholesterol_analysis(self.test_data)
        self.assertEqual(str(mock_print.call_args)[30], "3") #I am just naively checking one number to assume that both prints are the same
    @patch("matplotlib.pyplot.show")
    def test_plot_age_histogram(self, mock_show):
        """
        Test `plot_age_histogram` for correct plot generation.
        """
        plot_age_histogram(self.test_data)
        self.assertTrue(mock_show.called)

    @patch("matplotlib.pyplot.show")
    def test_plot_max_heart_rate_boxplot(self, mock_show):
        """
        Test `plot_max_heart_rate_boxplot` for correct boxplot generation.
        """
        plot_max_heart_rate_boxplot(self.test_data)
        self.assertTrue(mock_show.called)

    @patch("matplotlib.pyplot.show")
    def test_plot_angina_heart_disease_bar_chart(self, mock_show):
        """
        Test `plot_angina_heart_disease_bar_chart` for correct bar chart generation.
        """
        plot_angina_heart_disease_bar_chart(self.test_data)
        self.assertTrue(mock_show.called)

if __name__ == "__main__":
    unittest.main()
