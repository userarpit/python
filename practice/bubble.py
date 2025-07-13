# import matplotlib.pyplot as plt
# import numpy as np

# x = np.random.rand(40)
# y = np.random.rand(40)
# z = np.random.rand(40) * 1000

# plt.scatter(x, y, s=z, alpha=0.5, c=z, cmap='viridis')
# plt.title('Bubble Chart Example')
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# plt.colorbar(label='Bubble Size')
# plt.show()


# # print(x)


import plotly.express as px
import pandas as pd

# Sample data
data = {
    'x': [1, 3, 4, 6, 8],
    'y': [10, 25, 40, 35, 50],
    'size': [100, 300, 500, 200, 400],
    'color': ['red', 'blue', 'green', 'yellow', 'orange'],
    'label': ['A', 'B', 'C', 'D', 'E']
}
df = pd.DataFrame(data)

fig = px.scatter(df, x='x', y='y', size='size', color='color', hover_data=['label'], title='Bubble Chart with Plotly Express')
fig.update_layout(
    title_x=0.5,
    xaxis_title='Integer',
    yaxis_title='Values'
)
fig.show()