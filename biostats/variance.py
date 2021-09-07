import pandas as pd
from biostats.arithmetic_mean import arithmetic_mean


def population_variance(ds: pd.Series) -> float:
    mu = arithmetic_mean(ds)
    mus = pd.Series([mu] * len(ds))
    diff = ds.subtract(mus)
    return sum(diff.pow(2)) / len(ds)


def population_standard_deviation(ds: pd.Series) -> float:
    return population_variance(ds) ** 0.5


def sample_variance(ds: pd.Series) -> float:
    l = len(ds)
    return l * population_variance(ds) / (l - 1)


def sample_standard_deviation(ds: pd.Series) -> float:
    return sample_variance(ds) ** 0.5
