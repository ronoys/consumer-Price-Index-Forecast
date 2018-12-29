# consumerPriceIndexForecast
Creating and using a regression model using Python to forecast changes to the Consumer Price Index

The data used is publicly available data from the U.S. Bureau of Labor Statistics, and is published on Data.gov. The dataset includes the value of the Price Index from 1995 until 2018 in one month increments. 

Initially I used the sklearn module to create a linear regression model. This was just to use as a baseline, and is not appropriate for data, as it does not account for expected fluctuations and just mirrors the general trend over time. 

I also plan to use an exponential regression and experiment with any other type of regression models. I will judge the accuracy of each model based on which version has the lowest r^2 value. 
