# test commit
import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression, LogisticRegression
import numpy as np
import random
import math

init_notebook_mode(connected=True)

f = open("averageConsumerPriceIndex.txt","r")

constant = .0834
series_id =[]
year = []
value = []
timeinterval = []
newList = []
count = 0


for line in f:
    for data in line.split():
        name = str(data)

        if(count%4 == 0):
            series_id.append(data)

        elif(count%4 == 1):
            newvar = data
            year.append(data)

        elif(count%4 == 2):
            timeinterval.append(data)
            newList.append(float(newvar) + (float((data.split("M"))[1])*constant))

        elif(count%4 == 3):
            value.append(data)

        count = count + 1


yearCount = 2019.0

newList1 = []
value1 = []

while (yearCount < 2030):
    X_predict = [[yearCount]]
    y_predict = model.predict(X_predict)

    newList.append(yearCount)
    value.append(str(float(y_predict)))
    yearCount = yearCount + constant

x = []
y = []
for i in newList:
    x.append(float(i))

for i in value:
    y.append(float(i))

#x = newList
#y = value

logy = []
xy = []
x2 = []

for i in y:
    logy.append(math.log(float(i)))
    xy.append(float(i)*float(x[y.index(i)]))
    x2.append(float(x[y.index(i)]*float(x[y.index(i)])))


# Declare Constants



sumx = sum(x)
sumy = sum(y)
sumxy = sum(xy)
sumx2 = sum(x2)
n = len(x)


m = ((n*sumxy)-(sumx*sumy))/((n*sumx2)-(sumx2*sumx2))
g = ((sumx2*sumy)-(sumxy*sumx))/((n*sumx2)-(sumx2*sumx2))

a = 10 ** m
b = 10 ** g

y_list = []
for i in x:
    y_list.append(a * (b ** i))



trace = {'type': 'scatter', 'x':(x), 'y': (y_list)}

plotly.offline.plot({'data': [trace]})
