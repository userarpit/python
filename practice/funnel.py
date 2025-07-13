import plotly.express as px
import pandas as pd

data = {
    'Stage': ['Applications Sent', 'Phone Interview', 'Technical Interview', 'Onsite Interview', 'Offers Received', 'Offers Accepted'],
    'Job Applications': [500, 348, 92, 56, 10, 1]
}

df = pd.DataFrame(data)
fig = px.funnel(df, x='Job Applications', y='Stage', title='Job Application Funnel')
fig.update_layout(
    title_x=0.5,
    xaxis_title='Number of Applications',
    yaxis_title='Stages of Job Application Process'
)
fig.show()