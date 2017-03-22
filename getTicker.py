import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd 
import pandas_datareader as web 


# GETS OPENING PRICE, CLOSING PRICE, HIGHEST PRICE, LOWEST PRICE AND VOLUME FOR EACH TICKER 

# initalise a style of plotting from matplotlib
style.use('ggplot')


# we have a start date and end date initalised from our datetime
start = dt.datetime(2000, 1, 1)

end = dt.datetime(2017, 2, 21)



# initalise a new Datareader to specify parameters
# param1 input of ticker symbol
# param2 input of database we want to get it from
# param3,4 specifies start date and end date
df = web.DataReader('AAPL', 'yahoo', start, end)


# can save it to a CSV file by using df.to_csv
##df.to_csv('AAPL.csv')

# prints the last 5 days 
print(df.tail(5))