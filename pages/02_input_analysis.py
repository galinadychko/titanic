import streamlit as st
import plotly.graph_objects as go
import plotly.figure_factory as ff
from start import df, df_psi

# Plot distributions of the categorical columns
st.header("Input analysis")
with st.expander("Distributions of categorical features", expanded=True):
    cols = st.columns(3)
    for st_col, col_name in zip(cols, ["Pclass_1", "Pclass_3", "IfMale"]):
        fig = go.Figure(
            data=[
                go.Histogram(x=df[df.DataPart == "Benchmark"][col_name].values, name="Benchmark", histnorm="percent"),
                go.Histogram(x=df[df.DataPart == "Inference"][col_name].values, name="Inference", histnorm="percent")

            ]
        )
        fig.update_layout(title=col_name)
        st_col.plotly_chart(fig, use_container_width=True)


with st.expander("Distributions of numeric features", expanded=False):
    cols = st.columns(3)
    for st_col, col_name in zip(cols, ["Fare", "Age"]):
        fig = ff.create_distplot(
            [df[df.DataPart == "Benchmark"][col_name].values, df[df.DataPart == "Inference"][col_name].values],
            group_labels=["Benchmark", "Inference"], show_hist=False, colors=["blue", "red"]
        )
        fig.update_layout(title=col_name)
        ################################################################################################
        # TODO: Display plotly chart
        ################################################################################################
        # Expected solution: st_col.plotly_chart(fig, use_container_width=True)

# display psi values as data frame
with st.expander("Population Stability Index", expanded=False):
    pass
    ################################################################################################
    # TODO: Instead of 'pass' display df_psi[df_psi.Feature != "y_prob"] as a data frame
    ################################################################################################
    # Expected solution:
    # st.dataframe(df_psi[df_psi.Feature != "y_prob"])
