import pandas as pd


def arithmetic_mean(ds: pd.Series) -> float:
    sum = ds.sum()
    length = len(ds)
    return sum / length
