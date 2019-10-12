# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 06:15:37 2019

@author: ttuzki

"""

#import numpy as np
import pandas as pd
#import statsmodels.api as sm
#import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import coint



#get the stock symbol and creat a list
data = pd.DataFrame(pd.read_excel('Amarket_Adj Close.xls'))
A = data.head(0)
Amarket = []
for symbol in A:
    Amarket.append(symbol)
Amarket.remove('Date')

#fill NaN with the closed value  
#https://www.cnblogs.com/louyifei0824/p/9942430.html
data = data.fillna(method = 'bfill') 

#do the ADF test, if the variable is unstable, then differ it 
stock0 = {}
stock1 = {}
stock2 = {}

for symbol in Amarket:
    if adfuller(data[symbol])[1] < 0.05:
        stock0[symbol] = data[symbol][-62:]         #####slic
    else:
        d1_price = data[symbol].diff().dropna()
        if adfuller(d1_price)[1] < 0.05:
            stock1[symbol] = data[symbol][-62:]     #####slic
#do the cointergration
l1 = []
n = 0
stock_group = {}
for i in stock1:
    l1.append(i)
    l2 = [i]
    n = n+1
    for j in stock1:
        if j not in l1:
            con = coint(stock1[i],stock1[j])
            if con[1] < 0.01:
                l2.append(j)
                stock_group[n] = l2
    print n,l2
# refine the stock groups, delete the same groups                            
l1 = []
l2 = []
stock_group_final = {}
n = 0
for group1 in stock_group:
    if group1 not in l1:
        l1.append(group1)
        #print l1
        for group2 in stock_group:
            if group2 not in l1:  
                for symbol in stock_group[group2]:
                    if symbol in stock_group[group1] and symbol not in l2:
                        n = n+1
                        stock_group_final[n]=list(set(stock_group[group1]+stock_group[group2]))
                        l1.append(group2)
                        l2 = l2+stock_group_final[n]
                        #print l2
                        continue                    
                #print group1,group2
print stock_group_final

save = open('stock_group_final62.txt','w')      #####
save.write(str(stock_group_final))
save.close()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    