import pandas as p

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
