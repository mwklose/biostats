import pandas as pd
import numpy as np
from biostats.arithmetic_mean import arithmetic_mean


def rth_moment(ds: pd.Series, r: int) -> float:
    n = len(ds)
    ybar = arithmetic_mean(ds)
    ybars = pd.Series([ybar] * n)
    diff = ds.subtract(ybars)
    diff.pow(r)
    return diff.sum() / n
