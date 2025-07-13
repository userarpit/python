import plotly.graph_objects as go
import plotly as px

# Sample Data
labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
values = [4500, 2500, 1053, 500]

fig = go.Figure(
    data=[
        go.Pie(
            labels=labels,
            values=values,
            hole=0.3,  # Makes it a donut chart
            hoverinfo="label+percent",  # Show label and percentage on hover
            textinfo="value",
            marker=dict(colors=px.colors.sequential.Plasma)
        )
    ]
)

fig.update_layout(title_text="Donut Chart Example",title_x=0.5,showlegend=True)

fig.show()
