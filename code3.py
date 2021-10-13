import plotly.express as px
import csv
with open("dataset2.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Size of TV", y = "\tAverage time spent watching TV in a week")
    fig.show()