import pandas as p
import plotly.express as px
from dash import Dash, html, dcc

df1 = p.read_csv("data/daily_sales_data_0.csv")
df2 = p.read_csv("data/daily_sales_data_1.csv")
df3 = p.read_csv("data/daily_sales_data_2.csv")

df = p.concat([df1,df2,df3],ignore_index=True)


df = df[df["product"] == "pink morsel"]
df["price"] = (
    df["price"]
    .replace("[$,]", "", regex=True)
    .astype(float)
)
df["sales"] = df["price"]*df["quantity"]

df = df[["sales","region","date"]]
print(df.head(10))

df["date"] = p.to_datetime(df["date"])

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