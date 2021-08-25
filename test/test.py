import unittest
from biostats.dataset import DataSet


class TestInitialize(unittest.TestCase):
    def test_initialize(self):
        d1 = DataSet("test.csv", "Initial Dataset")


if __name__ == "__main__":
    unittest.main()
