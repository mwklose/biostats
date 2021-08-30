import pandas as pd
import math


def median(ds: pd.Series) -> float:
    sorted_vals = ds.sort_values
    l = len(sorted_vals)
    floor = math.floor(l / 2)
    ceiling = math.ceil(l / 2)
    return (sorted_vals[floor] + sorted_vals[ceiling]) / 2
