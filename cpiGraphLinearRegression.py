import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

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


newListArray = np.asarray(newList)
valueArray = np.asarray(value)

newListArray2D = np.reshape(newListArray,(-1,1))
valueArray2D = np.reshape(valueArray,(-1,1))



model = LinearRegression()
model.fit(newListArray2D, valueArray2D)

yearCount = 2019.0

while (yearCount < 2030):
    X_predict = [[yearCount]]
    y_predict = model.predict(X_predict)
    newList.append(yearCount)
    value.append(str(float(y_predict)))
    yearCount = yearCount + constant
    

trace = {'type': 'scatter', 'x':(newList), 'y': (value)}

plotly.offline.plot({'data': [trace]})


