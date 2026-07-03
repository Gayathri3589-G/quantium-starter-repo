from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# Read formatted CSV
df = pd.read_csv("formatted_sales_data.csv")

df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div(
    style={
        "backgroundColor": "#f4f6f9",
        "padding": "30px",
        "fontFamily": "Arial"
    },
    children=[

        html.H1(
            "Soul Foods Pink Morsel Sales Dashboard",
            style={
                "textAlign": "center",
                "color": "#2c3e50"
            }
        ),

        html.H3(
            "Filter sales by region",
            style={"color": "#34495e"}
        ),

        dcc.RadioItems(
            id="region-filter",
            options=[
                {"label": "All", "value": "all"},
                {"label": "North", "value": "north"},
                {"label": "South", "value": "south"},
                {"label": "East", "value": "east"},
                {"label": "West", "value": "west"},
            ],
            value="all",
            inline=True,
            style={"marginBottom": "20px"}
        ),

        dcc.Graph(id="sales-chart")
    ]
)

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df.copy()
    else:
        filtered_df = df[df["region"] == selected_region]

    daily_sales = (
        filtered_df.groupby("date")["sales"]
        .sum()
        .reset_index()
        .sort_values("date")
    )

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        title=f"Pink Morsel Sales - {selected_region.title()}",
        markers=True
    )

    fig.update_layout(
        xaxis_title="Date",
        yaxis_title="Sales",
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    fig.add_vline(
        x="2021-01-15",
        line_dash="dash",
        annotation_text="Price Increase"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)