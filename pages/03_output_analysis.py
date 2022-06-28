import streamlit as st
import plotly.graph_objects as go
from start import df


st.header("Output analysis")

# Add multiselection to filter out data
filtration_cols = ["IfMale"]
st.sidebar.multiselect(
        label='',
        options=filtration_cols,
        default=[],
        key='filtration',
)

# data filtration using selected options
df_to_pass = df[df[st.session_state.filtration[0]] == 1] if st.session_state.filtration != [] else df

# initialize width of bins used to plot density of the predicted scored depending on the input
bin_size = 0.1 if st.session_state.get("bin_size") is None else st.session_state.get("bin_size")

# plot distributions
fig = go.Figure(
        data=[
                go.Histogram(
                        x=df_to_pass[df_to_pass.DataPart == "Benchmark"]["y_prob"].values,
                        name="Benchmark", histnorm="percent", xbins={"size": bin_size}
                ),
                go.Histogram(
                        x=df_to_pass[df_to_pass.DataPart == "Inference"]["y_prob"].values,
                        name="Inference", histnorm="percent", xbins={"size": bin_size}
                )
        ]
)
fig.update_layout(title={"text": "Distribution of predicted scores", 'x': 0.45, 'xanchor': 'center'})
st.plotly_chart(fig, use_container_width=True)

# number input for width of bins
################################################################################################
# TODO: Use function st.number_input(label, min_value=None, value=, key=None)
#       to display a numeric input widget
################################################################################################
# Expected solution: st.number_input("Bin size", min_value=0.001, value=0.1, key="bin_size")

