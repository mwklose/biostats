import pandas as pd


def range(ds: pd.Series) -> float:
    sorted_vals = ds.sort_values
    return sorted_vals[-1] - sorted_vals[0]  # Use fact that a[-1] = a[len(a) - 1]
