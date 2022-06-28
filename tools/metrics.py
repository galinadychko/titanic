import numpy as np
import pandas as pd


def count_bins_in_numeric_col(col_benchmark: pd.Series,
                              col_input: pd.Series,
                              q: int, zero_offset: float) -> pd.DataFrame:
    """
    Split numeric benchmark column into quartiles and use them to split another input column.
    Compute percentage of occurrences of each bin.
    :param col_benchmark:   pd.Series, column from benchmark
    :param col_input:       pd.Series, column from inference
    :param q:               int, number of quantiles used to make a split
    :param zero_offset:     float, a value to replace 0 and NaNs in occurrences
    :return:                pd.DataFrame with columns: {"quantile", "n_benchmark", "n"}
    """
    benchmark_bins, bins_unique = pd.qcut(col_benchmark, q=q, duplicates="drop", retbins=True)
    col_bins = pd.cut(col_input, bins=bins_unique)
    df_bins = pd.DataFrame.from_dict(
        {
            "benchmark": benchmark_bins,
            "new": col_bins
        }
    )
    df_bins_counts_b = df_bins.groupby("benchmark").new.count().reset_index(name="n_benchmark").rename(
        columns={"benchmark": "quantile"})
    df_bins_counts_n = df_bins.groupby("new").benchmark.count().reset_index(name="n").rename(
        columns={"new": "quantile"})

    df_bins_counts = pd.merge(df_bins_counts_b, df_bins_counts_n, on="quantile", how="left")
    df_bins_counts["n"] = df_bins_counts["n"] / df_bins_counts["n"].sum()
    df_bins_counts["n_benchmark"] = df_bins_counts["n_benchmark"] / df_bins_counts["n_benchmark"].sum()

    df_bins_counts.n.replace({0: zero_offset}, inplace=True)
    df_bins_counts.n_benchmark.replace({0: zero_offset}, inplace=True)
    df_bins_counts.n.fillna(zero_offset, inplace=True)
    df_bins_counts.sort_values("quantile", inplace=True)

    return df_bins_counts


def count_bins_in_categorical_col(col_benchmark: pd.Series, col_input: pd.Series, zero_offset: float):
    """
    Compute occurrences of each unique value
    :param col_benchmark:   pd.Series, column from benchmark
    :param col_input:       pd.Series, column from inference
    :param zero_offset:     float, a value to replace 0 and NaNs in occurrences
    :return:                pd.DataFrame with columns: {"values", "n_benchmark", "n"}
    """
    df_counts_1 = col_benchmark.value_counts(normalize=True).reset_index(name="n_benchmark").rename(
        columns={"index": "values"})
    df_counts_2 = col_input.value_counts(normalize=True).reset_index(name="n").rename(columns={"index": "values"})
    df_bins_counts = pd.merge(df_counts_1, df_counts_2, how="inner", on="values")

    df_bins_counts.n.replace({0: zero_offset}, inplace=True)
    df_bins_counts.n_benchmark.replace({0: zero_offset}, inplace=True)
    df_bins_counts.n.fillna(zero_offset, inplace=True)
    df_bins_counts.sort_values("values", inplace=True)

    return df_bins_counts


def psi(col_benchmark: pd.Series, col_input: pd.Series, input_type: str, q: int = 10, zero_offset: float = 0.001):
    """
    Split the input data if needed, compute occurrences, compute psi value based
    :param col_benchmark:   pd.Series, column from benchmark
    :param col_input:       pd.Series, column from inference
    :param input_type:      str, if an input columns are "numeric" or "categorical"
    :param q:               int, number of quantiles used to split numeric data
    :param zero_offset:     float, a value to replace 0 and NaNs in occurrences
    :return:                pd.DataFrame, with psi value per bin/unique categorical value
    """
    if input_type == "numeric":
        df_counts = count_bins_in_numeric_col(
            col_benchmark=col_benchmark, col_input=col_input, q=q, zero_offset=zero_offset
        )
    elif input_type == "categorical":
        df_counts = count_bins_in_categorical_col(
            col_benchmark=col_benchmark, col_input=col_input, q=q, zero_offset=zero_offset
        )
    else:
        raise NotImplementedError

    df_counts["dff"] = df_counts["n_benchmark"] - df_counts["n"]
    df_counts["log"] = np.log(df_counts["n_benchmark"] / df_counts["n"])
    df_counts["psi"] = df_counts["dff"] * df_counts["log"]
    return df_counts
