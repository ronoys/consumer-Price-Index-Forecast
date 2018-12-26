import plotly
from plotly.offline import iplot, init_notebook_mode
from plotly import tools
import plotly.graph_objs as go
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
            goteem = data
            year.append(data)
            
        elif(count%4 == 2):
            timeinterval.append(data)         
            newList.append(float(goteem) + (float((data.split("M"))[1])*constant))
                       
        elif(count%4 == 3):
            value.append(data)

        count = count + 1


trace = {'type': 'scatter', 'x':(newList), 'y': (value)}


plotly.offline.plot({'data': [trace]})  





