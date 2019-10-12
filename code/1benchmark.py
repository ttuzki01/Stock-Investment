# -*- coding: utf-8 -*-
import xlrd

#表格格式准备

#读取表格
rawA = xlrd.open_workbook("rawA.xlsx")
rawA = rawA.sheet_by_name('Sheet1') #读rawA中的sheet1
#op = xlrd.open_workbook("operating.xlsx")
#opw = copy(op)
#opw_buy =  opw.get_sheet(0) #写
#op_buy = op.sheet_by_name('buy') #读

#EPS
stock_list = []
rawA_nrows = rawA.nrows 
for i in range(1,rawA_nrows):
    n = 0 
    for j in rawA.row_values(0):
        n = n+1
        if 'EPS' in j:
            stock_list.append(rawA.row_values(i)[n-1])
stock_list.sort(reverse=True)
stock_list = [n for n in stock_list if n > 0 and n != '']
print "EPS=",stock_list[int(len(stock_list)*0.1)]

#PB
stock_list = []
rawA_nrows = rawA.nrows 
for i in range(1,rawA_nrows):
    n = 0 
    for j in rawA.row_values(0):
        n = n+1
        if u'\u0050\u0042\uff0c\u6700\u65b0' in j:
            stock_list.append(rawA.row_values(i)[n-1])
stock_list.sort()
stock_list = [n for n in stock_list if n > 0 and n != '']
print "PB=",stock_list[int(len(stock_list)*0.1)]

#PE
stock_list = []
rawA_nrows = rawA.nrows 
for i in range(1,rawA_nrows):
    n = 0 
    for j in rawA.row_values(0):
        n = n+1
        if u'\u0050\u0045\uff0c\u0054\u0054\u004d' in j:
            stock_list.append(rawA.row_values(i)[n-1])
stock_list.sort()
stock_list = [n for n in stock_list if n > 0 and n != '']
print "PE_TTM=",stock_list[int(len(stock_list)*0.1)]




    



#stock_list.remove('')
#stock_list.remove(u'\u6570\u636e\u6765\u6e90\uff1a\u540c\u82b1\u987aiFinD')


#在rawA中筛选高收益股票（EPS）
#for i in range(1,rawA_nrows):
#    rawA_row = rawA.row_values(i)
#    if 



#定位到EPS
#rawA_row = rawA.row_values(0)
#n = 0 
#for i in rawA.row_values(0):
#    n = n+1
#    if 'EPS' in i:
#        print i
#        print n






