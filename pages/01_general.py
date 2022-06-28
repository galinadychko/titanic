import streamlit as st
import plotly.express as px
from sklearn.metrics import accuracy_score, precision_score, recall_score
from start import df, df_metrics, df_pr_rec, df_fp_tp


# set header
st.header("General Metrics")

# set a slider for threshold selection
st.sidebar.slider(label="Threshold", min_value=0., max_value=1., value=0.5, step=0.1, key="threshold")

################################################################################################
# TODO: Replace a step of the slider from 0.1 to 0.001
################################################################################################
# Expected solution:
# st.sidebar.slider(label="Threshold", min_value=0., max_value=1., value=0.5, step=0.001, key="threshold")

# make computations of the metrics which dependent on threshold value
metrics_func_list = [accuracy_score, precision_score, recall_score]
metrics_name_list = ["Accuracy", "Precision", "Recall"]


for metric_func, metric_name in zip(metrics_func_list, metrics_name_list):
    benchmark_val = metric_func(
        df[df.DataPart == "Benchmark"]["Survived"],
        (df[df.DataPart == "Benchmark"]["y_prob"] >= st.session_state.threshold).astype(int)
    )
    inf_val = metric_func(
        df[df.DataPart == "Inference"]["Survived"],
        (df[df.DataPart == "Inference"]["y_prob"] >= st.session_state.threshold).astype(int)
    )
    chng_val = (inf_val - benchmark_val) * 100 / benchmark_val

    df_metrics.loc[df_metrics.Metrics == metric_name, "Inference"] = round(inf_val, 3)
    df_metrics.loc[df_metrics.Metrics == metric_name, "% change"] = round(chng_val, 3)


# columns for metrics
cols = st.columns(5)
metrics = df_metrics.Metrics.values

for col, metric in zip(cols, metrics):
    subsample = df_metrics[df_metrics.Metrics == metric].reset_index(drop=True)
    col.metric(metric, subsample.loc[0, "Inference"], delta=subsample.loc[0, "% change"], delta_color="normal")

# columns for plots
cols_plots = st.columns(2)

pr_recall_fig = px.line(
    df_pr_rec, x="Recall", y="Precision", title='Precision Recall Curve', color="Data"
)
cols_plots[0].plotly_chart(pr_recall_fig, use_container_width=True)


################################################################################################
# TODO: Create line plot for displaying 'False Positive Ratio' on x, 'True Positive Ratio' on y,
#       and add it to the app
################################################################################################
# Expected solution:
# roc_fig = px.line(
#     df_fp_tp, x="False Positive Ratio", y="True Positive Ratio", title='ROC', color="Data"
# )
# cols_plots[1].plotly_chart(roc_fig, use_container_width=True)

