import plotly.graph_objects as go

# Define the nodes (the categories/stages in your flow)
# Each node needs a unique label.
nodes_labels = [
    "Website Traffic",
    "Product Page Views",
    "Add to Cart",
    "Checkout Initiated",
    "Purchase Completed",
    "Abandoned Cart",
    "Bounced",
    "Customer Support"
]

# Define the links (the flows between the nodes)
# Each link needs a source node index, a target node index, and a value (quantity of flow).
# The indices correspond to the order in the 'nodes_labels' list.
links_source = [
    0, 0,  # Website Traffic -> Product Page Views, Website Traffic -> Bounced
    1, 1,  # Product Page Views -> Add to Cart, Product Page Views -> Customer Support
    2, 2,  # Add to Cart -> Checkout Initiated, Add to Cart -> Abandoned Cart
    3      # Checkout Initiated -> Purchase Completed
]

links_target = [
    1, 6,  # Product Page Views, Bounced
    2, 7,  # Add to Cart, Customer Support
    3, 5,  # Checkout Initiated, Abandoned Cart
    4      # Purchase Completed
]

links_value = [
    10000, 2000,  # Website Traffic flows
    7000, 1000,  # Product Page Views flows
    5000, 2000,  # Add to Cart flows
    3000       # Checkout Initiated flow
]

fig = go.Figure(data=[go.Sankey(
    # Define the nodes
    node=dict(
        pad=15, # Padding between nodes
        thickness=20, # Thickness of nodes
        line=dict(color="black", width=0.5), # Node border
        label=nodes_labels,
        # color="blue" # You can set a single color for all nodes or use a list of colors
    ),
    # Define the links
    link=dict(
        source=links_source, # indices correspond to labels, e.g. nodes_labels[0] is 'Website Traffic'
        target=links_target,
        value=links_value,
        # color="rgba(0,0,0,0.2)" # You can set a single color for all links or a list of colors
    )
)])

fig.update_layout(
    title_text="Website Conversion Funnel",
    font_size=10,
    title_x=0.5, # Center the title
)

fig.show()