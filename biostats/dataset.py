import pandas as pd
from dataclasses import dataclass


@dataclass
class DataSet:
    values: pd.DataFrame
    description: str

    # Open file by filename string
    def __init__(self, file: str, description=None) -> None:
        with open(file) as f:
            self.values = pd.read_csv(f)
        self.description = description
