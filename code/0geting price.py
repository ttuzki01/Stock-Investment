# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 20:35:23 2019

@author: ttuzki
"""

import pandas as pd
import numpy as np
import pandas_datareader as web
import datetime


# get all stocks' code in A market and put them in to list 'A'
data = pd.DataFrame(pd.read_excel('rawA.xlsx'))
A = np.array(data['z1'])
print A

# look at stock prices over the past year, starting at January 1, 2017
start = datetime.datetime(2017,1,1)
end = datetime.date.today()

# get stock data, from yahoo finance within the dates specified
stocks = {}
n = 0
for i in A:
    n = n+1
    stock = web.DataReader(i, "yahoo", start, end)
    stock = stock['Adj Close']
    stocks[i] = stock #add every stock into dict'stocks'
    stocks = pd.DataFrame(stocks) #transfer dict into DataFrame
    stocks.to_csv('Amarket_Adj Close.csv')
    print stocks.head(2)



    














