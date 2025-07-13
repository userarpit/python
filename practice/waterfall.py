import plotly.graph_objects as go

# Sample Data
# The 'measure' array tells Plotly whether each value is a 'relative' change or a 'total'.
# 'absolute' is often used for the very first bar if it's a true starting point.
# 'relative' for intermediate changes.
# 'total' for intermediate totals or the final total.
data = {
    "Phases": [
        "Starting Balance",
        "Deposits",
        "Withdrawals",
        "Interest Earned",
        "Fees Paid",
        "Ending Balance",
    ],
    "Amount": [
        1000,
        500,
        -200,
        50,
        -30,
        0,
    ],  # Ending balance can be 0 or calculated later
    "Measure": [
        "absolute",
        "relative",
        "relative",
        "relative",
        "relative",
        "total",
    ],  # Explicitly define types
}

# The 'y' values for 'total' measures are automatically calculated by Plotly.
# So for 'Ending Balance', we can put 0, and Plotly will figure out the cumulative sum.
# Or, if your last 'Amount' is indeed the calculated total, you can use that.
# Let's use 0 for the last total to demonstrate automatic calculation.

fig = go.Figure(
    go.Waterfall(
        name="Financial Flow",
        orientation="v",  # 'v' for vertical, 'h' for horizontal
        measure=data["Measure"],
        x=data["Phases"],
        y=data["Amount"],
        textposition="outside",  # Position of the value labels
        text=[
            "$1000",
            "$500",
            "-$200",
            "$50",
            "-$30",
            "$1320",
        ],  # Custom text labels (optional, can be auto-generated)
        connector={"line": {"color": "rgb(63, 63, 63)"}},  # Connector line style
        increasing={"marker": {"color": "green"}},  # Customize increasing bar color
        decreasing={"marker": {"color": "red"}},  # Customize decreasing bar color
        totals={
            "marker": {"color": "blue", "line": {"color": "black", "width": 2}}
        },  # Customize total bars
    )
)

fig.update_layout(
    title="Monthly Account Balance Changes",
    title_x=0.5,
    showlegend=True,
    xaxis_title="Transaction Type",
    yaxis_title="Amount ($)",
    margin=dict(l=50, r=50, b=100, t=100),  # Adjust margins
)

fig.show()
