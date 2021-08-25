import pandas as pd
from dataclasses import dataclass

import os


@dataclass
class DataSet:
    values: pd.DataFrame
    description: str
    length: int

    # Open file by filename string
    def __init__(self, file: str, description=None) -> None:
        for f in os.listdir(os.getcwd()):
            print(f)
        with open(file, "r") as f:
            self.values = pd.read_csv(f)
        self.description = description
