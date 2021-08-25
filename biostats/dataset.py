import pandas as pd
from dataclasses import dataclass, field


@dataclass
class DataSet:
    values: pd.DataFrame
    description: str
    length: int

    # Open file by filename string
    def __init__(self, file: str, description=None) -> None:
        with open(file, "r") as f:
            self.values = pd.read_csv(f)
        self.description = description
        self.length = self.get_length()

    def get_length(self):
        return len(self.values)

    def get_description(self):
        return self.description
