import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Sample Data: Performance metrics for two players
data = {
    'Player': ['Player A'] * 5 + ['Player B'] * 5,
    'Attribute': ['Speed', 'Strength', 'Agility', 'Stamina', 'Teamwork'] * 2,
    'Score': [85, 70, 90, 75, 80, 90, 65, 80, 85, 70]
}
df = pd.DataFrame(data)

# # --- Option 1: Using Plotly Express (Simplest) ---
# fig_px = px.line_polar(df,
#                        r='Score',        # Radial axis (values)
#                        theta='Attribute',  # Angular axis (categories)
#                        color='Player',   # Separate lines/fills for each player
#                        line_close=True,  # Connect the last point to the first to close the shape
#                        title="Player Performance Comparison (Plotly Express)")

# # To fill the area under the line:
# fig_px.update_traces(fill='toself')

# fig_px.show()

# --- Option 2: Using Plotly Graph Objects (More Control) ---
fig_go = go.Figure()

# Add Player A's trace
fig_go.add_trace(go.Scatterpolar(
    r=[85, 70, 90, 75, 80, 85], # Scores, repeating the first score to close the loop
    theta=['Speed', 'Strength', 'Agility', 'Stamina', 'Teamwork', 'Speed'], # Attributes, repeating the first to close
    fill='toself',
    name='Player A',
    hovertemplate='<b>%{theta}</b>: %{r}<extra></extra>' # Custom hover info
))

# Add Player B's trace
fig_go.add_trace(go.Scatterpolar(
    r=[90, 65, 80, 85, 70, 90],
    theta=['Speed', 'Strength', 'Agility', 'Stamina', 'Teamwork', 'Speed'],
    fill='toself',
    name='Player B'
))

fig_go.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 100] # Set the range of the radial axis
        )
    ),
    showlegend=True,
    title_text="Player Performance Comparison (Plotly Graph Objects)",
    title_x=0.5 # Center the title
)

fig_go.show()