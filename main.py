import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
n_points = 50
time_steps = 10

data = {
    "x": [],
    "y": [],
    "time": [],
    "group": [],
    "size": [], 
    "label": []  
}

for t in range(time_steps):
    for group in ["A", "B"]:
        x_vals = np.random.rand(n_points) + t
        y_vals = np.random.rand(n_points) + t
        sizes = np.random.rand(n_points) * 50 + 10  
        labels = [f"Point-{i}" for i in range(len(x_vals))]

        data["x"].extend(x_vals)
        data["y"].extend(y_vals)
        data["time"].extend([t] * n_points)
        data["group"].extend([group] * n_points)
        data["size"].extend(sizes)
        data["label"].extend(labels)

df = pd.DataFrame(data)

fig = px.scatter(
    df,
    x="x",
    y="y",
    animation_frame="time",
    animation_group="label",  
    color="group",
    size="size",  
    hover_name="label", 
    title="Enhanced Animated Scatter Plot",
    labels={"x": "X-axis", "y": "Y-axis"},
    template="plotly_white"
)

fig.update_layout(
    xaxis=dict(range=[-1, time_steps + 5], title="Dynamic X-axis", gridwidth=1, gridcolor="lightgray"),
    yaxis=dict(range=[-1, time_steps + 5], title="Dynamic Y-axis", gridwidth=1, gridcolor="lightgray"),
    title_font=dict(size=24, color="darkblue", family="Arial"),
    plot_bgcolor="white",
    legend=dict(
        title="Groups",
        bgcolor="white",
        bordercolor="black",
        borderwidth=1,
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    )
)
fig.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 500  
fig.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 300 

fig.show()