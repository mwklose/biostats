import pandas as pd
import math


def percentile(ds: pd.Series, p: float) -> float:
    n = len(ds)
    floor = math.floor(n * p + p)
    ceiling = math.ceil(n * p + p)
    sorted_vals = ds.sort_values()
    return (sorted_vals[floor] + sorted_vals[ceiling]) / 2


# TODO: function where you give value, it returns its percentile?
