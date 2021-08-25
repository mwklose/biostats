import unittest
from biostats.dataset import DataSet
import os


class TestInitialize(unittest.TestCase):
    def test_initialize(self):
        d1 = DataSet(os.path.abspath("files/test.csv"), "Initial Dataset")


if __name__ == "__main__":
    unittest.main()
