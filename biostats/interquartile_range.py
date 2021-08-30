import pandas as pd
from biostats.percentile import percentile


def interquartile_range(ds: pd.Series):
    p25 = percentile(ds, 0.25)
    p75 = percentile(ds, 0.75)
    return p75 - p25
