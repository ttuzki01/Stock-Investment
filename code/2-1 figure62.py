# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:19:20 2019

@author: liuyemeng
"""


f = open('stock_group_final62.txt','r')     #####
stock_group_final = f.read()
stock_group_final = eval(stock_group_final)
f.close()
print stock_group_final[1]


import pandas as pd
#import statsmodels.api as sm
#import seaborn as sns
#from statsmodels.tsa.stattools import adfuller
#from statsmodels.tsa.stattools import coint



#get the stock symbol and creat a list
data = pd.DataFrame(pd.read_excel('Amarket_Adj Close.xls'))
#fill NaN with the closed value  
#https://www.cnblogs.com/louyifei0824/p/9942430.html
data = data.fillna(method = 'bfill') 


#print the figure
import pylab as pl
for stock_group in stock_group_final:
    print stock_group_final[stock_group]
    for symbol in stock_group_final[stock_group]:
        pl.plot(data['Date'][-62:] ,data[symbol][-62:] )   #####
    pl.show()



    
    