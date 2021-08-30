import pandas as pd


def rank(ds: pd.Series, i: int) -> float:
    if i >= len(ds) or i < 0:
        raise Warning("Index out of bounds on rank")
    return ds.sort_values[i]


# i is floor of half_rank
def half_rank(ds: pd.Series, i: int) -> float:
    if i >= len(ds) or i < 0:
        raise Warning("Index out of bounds on half_rank")

    sorted_vals = ds.sort_values
    return (sorted_vals[i] + sorted_vals[i + 1]) / 2
