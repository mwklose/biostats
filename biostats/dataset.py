import pandas as pd
from dataclasses import dataclass, field
from typing import Optional

from biostats.arithmetic_mean import arithmetic_mean
from biostats.half_rank import half_rank, rank
from biostats.median import median
from biostats.percentile import percentile
from biostats.range import range
from biostats.sample_variance import (
    population_variance,
    population_standard_deviation,
    sample_variance,
    sample_standard_deviation,
)


@dataclass
class DataSet:
    file: str
    description: Optional[str] = None
    values: pd.DataFrame = field(init=False)

    @property
    def length(self) -> int:
        return len(self.values)

    @property
    def colnames(self) -> list:
        return list(self.values.columns)

    # Overrides of default functionality
    def __getitem__(self, key):
        return values[key]

    def __len__(self):
        return len(self.values)

    def __post_init__(self):
        with open(self.file, "r") as f:
            self.values = pd.read_csv(f)

    # -------------------------------------------------------
    # Functions available, listed in alphabetical order.
    # -------------------------------------------------------
    # Arithmetic mean of dataset.
    def arithmetic_mean(self, col: str) -> float:
        if not col in self.colnames:
            raise Warning("Column not in DataSet")
        return arithmetic_mean(self.values[col])

    # Get half rank where i is floor of what half rank wanted.
    def half_rank(self, col: str, i: int) -> float:
        return half_rank(self.values[col], i)

    def median(self, col: str) -> float:
        return median(self.values[col])

    def mode(self, col: str) -> float:
        return self.values[col].mode()

    def percentile(self, col: str, p: float) -> float:
        return percentile(self.values[col], p)

    def population_standard_deviation(self, col: str) -> float:
        return population_standard_deviation(self.values[col])

    def population_variance(self, col: str) -> float:
        return population_variance(self.values[col])

    def range(self, col: str) -> float:
        return range(self.values[col])

    def rank(self, col: str, i: int) -> float:
        return rank(self.values[col], i)

    def sample_standard_deviation(self, col: str) -> float:
        return sample_standard_deviation(self.values[col])

    def sample_variance(self, col: str) -> float:
        return sample_variance(self.values[col])
