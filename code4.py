import plotly.express as px
import numpy as np
import csv

def getDataSource(data_path):
    numberofhrswatched = []
    size_of_tv = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            numberofhrswatched.append(float(row["\tAverage time spent watching TV in a week"]))
    return{
        "x" : size_of_tv,
        "y" : numberofhrswatched
    }

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"],datasource["y"])
    print("correlation between size of TV vs no. of hours watched is : ", correlation[0,1])

def setup():
    data_path = "dataset2.csv"
    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()