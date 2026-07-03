import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc


df = pd.read_csv("formatted_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])

daily_sales = (
    df.groupby("date")["sales"]
      .sum()
      .reset_index()
      .sort_values("date")
)

app = Dash()
fig = px.line(df, x="date", y="sales",title="Pink Morsels sales" ,labels={
        "date": "Date",
        "sales": "Sales"
    })

fig.add_vline(
    x="2021-01-15",
    line_dash="dash",
    annotation_text="Price Increase"
)

app.layout = html.Div(children=[
    html.H1(children='Soul Foods Pink Morsel Sales Analysis'),

    html.Div(children='''
       Sales trend before and after the Pink Morsel price increase.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)