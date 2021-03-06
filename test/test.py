import os
from unittest import TestCase
from biostats.dataset import DataSet
from biostats.distribution import Distribution
import biostats.normal_distribution as nd

from scipy.stats import norm

TOTAL_SIZE = 15

import warnings

warnings.filterwarnings("ignore", category=RuntimeWarning)


class TestMeasures(TestCase):
    def setUp(self):
        self.d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")

    def test_initialize(self):
        # Initialize with description
        self.assertEqual(self.d1.length, TOTAL_SIZE)
        self.assertEqual(self.d1.description, "Initial Dataset")

        # Initialize without description
        d2 = DataSet("files/test.csv")
        self.assertEqual(d2.length, TOTAL_SIZE)
        self.assertIsNone(d2.description)

    def test_means(self):
        # Arithmetic Mean
        s = 0
        for v in self.d1.values["Total Number"]:
            s += v

        self.assertEqual(
            s / len(self.d1.values["Total Number"]),
            self.d1.arithmetic_mean("Total Number"),
        )

    def test_percentiles(self):
        self.d1.median("Total Number")
        self.d1.mode("Total Number")
        self.d1.percentile("Total Number", 0.5)
        self.d1.interquartile_range("Total Number")
        self.d1.range("Total Number")

    def test_ranks(self):
        self.d1.half_rank("Total Number", 3)
        self.d1.rank("Total Number", 3)

    def test_variances(self):
        self.assertAlmostEqual(self.d1.population_variance("Total Number"), 6.6666667)
        self.assertAlmostEqual(
            self.d1.population_standard_deviation("Total Number"), 2.5819889
        )
        self.assertAlmostEqual(
            self.d1.sample_standard_deviation("Total Number"), 2.6726124
        )
        self.assertAlmostEqual(self.d1.sample_variance("Total Number"), 7.1428571)

    def test_skewness(self):
        self.assertAlmostEqual(self.d1.skewness("Total Number"), -0.388557, places=5)

    def test_kurtosis(self):
        self.assertAlmostEqual(self.d1.kurtosis("Total Number"), -0.684923, places=5)

    def test_moments(self):
        self.d1.rth_moment("Total Number", 2)
        self.d1.rth_moment("Total Number", 3)
        self.d1.rth_moment("Total Number", 4)
        self.d1.rth_moment("Total Number", 5)


class TestNormal(TestCase):
    def setUp(self):
        self.d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")

    def test_normal_pdf(self):
        # test basic PDF
        self.assertEqual(nd.NormalDistribution.pdf(0), norm.pdf(0))

        # Test basic CDF
        self.assertEqual(nd.NormalDistribution.cdf(0), norm.cdf(0))


if __name__ == "__main__":
    unittest.main()
