import pandas as pd
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class DataSet:
    file: str
    description: Optional[str] = None
    values: pd.DataFrame = field(init=False)

    @property
    def length(self) -> int:
        return len(self.values)

    @property
    def arithmetic_mean(self, col) -> float:
        return values[col].mean()

    def __post_init__(self):
        with open(self.file, "r") as f:
            self.values = pd.read_csv(f)

    def nth_moment(self, n):
        pass
