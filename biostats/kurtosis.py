import pandas as pd
from biostats.rth_moment import rth_moment

KURT_VAL = 4


def kurtosis(ds: pd.Series):
    num = rth_moment(ds, KURT_VAL)
    d = rth_moment(ds, 2)
    denom = d ** (KURT_VAL / 2)
    return num / denom
