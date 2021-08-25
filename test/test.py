from unittest import TestCase
from biostats.dataset import DataSet
import os

TOTAL_SIZE = 15


class TestInitialize(TestCase):
    def test_initialize(self):
        d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")
        self.assertEqual(d1.length, TOTAL_SIZE)


if __name__ == "__main__":
    unittest.main()
