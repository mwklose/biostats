from unittest import TestCase
from biostats.dataset import DataSet
import os

TOTAL_SIZE = 15


class TestInitialize(TestCase):
    def test_initialize(self):
        # Initialize with description
        d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")
        self.assertEqual(d1.length, TOTAL_SIZE)
        self.assertEqual(d1.description, "Initial Dataset")

        # Initialize without description
        d2 = DataSet("files/test.csv")
        self.assertEqual(d2.length, TOTAL_SIZE)
        self.assertIsNone(d2.description)

    def test_means(self):
        d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")

        # Arithmetic Mean
        s = 0
        for v in d1.values["Total Number"]:
            s += v

        self.assertEqual(
            s / len(d1.values["Total Number"]), d1.arithmetic_mean("Total Number")
        )

    def test_percentiles(self):
        d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")
        d1.median("Total Number")
        d1.mode("Total Number")
        d1.percentile("Total Number", 0.5)
        d1.interquartile_range("Total Number")
        d1.range("Total Number")

    def test_ranks(self):
        d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")
        d1.half_rank("Total Number", 3)
        d1.rank("Total Number", 3)

    def test_variances(self):
        d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")
        d1.population_variance("Total Number")
        d1.population_standard_deviation("Total Number")
        d1.sample_standard_deviation("Total Number")
        d1.sample_variance("Total Number")


if __name__ == "__main__":
    unittest.main()
