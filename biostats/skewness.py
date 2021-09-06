import pandas as pd
from biostats.rth_moment import rth_moment

SKEW_VAL = 3


def skewness(ds: pd.Series):
    num = rth_moment(ds, SKEW_VAL)
    d = rth_moment(ds, 2)
    denom = d ** (SKEW_VAL / 2)
    return num / denom
