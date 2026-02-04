import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

df = pd.read_csv("final_output.csv")
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

fig = px.line(
    df,
    x="Date",
    y="Sales",
    title="Pink Morsel Sales Over Time",
    labels={"Date": "Date", "Sales": "Total Sales"}
)

fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    line_color="red",
    annotation_text="Price Increase",
    annotation_position="top right"
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser", style={"textAlign": "center"}),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run_server(debug=True)
