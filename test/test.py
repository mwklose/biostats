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

    def test_mean(self):
        d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")

        s = 0
        for v in d1.values["Total Number"]:
            s += v

        self.assertEqual(
            s / len(d1.values["Total Number"]), d1.arithmetic_mean("Total Number")
        )


if __name__ == "__main__":
    unittest.main()
