import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    ice_cream_sales = []
    temperature = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row['Ice-cream Sales']))
    return{
        "x" : temperature,
        "y" : ice_cream_sales
    }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between temperature vs ice_cream_sales: ", correlation[0,1])

def setup():
    data_path = "dataset1.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()