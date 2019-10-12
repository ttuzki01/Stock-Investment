# -*- coding: utf-8 -*-
import xlwt
import xlrd
from xlutils.copy import copy 
#表格准备
rawA = xlrd.open_workbook("rawA.xlsx")
rawA = rawA.sheet_by_name('Sheet1') #读rawA中的sheet1
op = xlrd.open_workbook("operating.xlsx")
opw = copy(op)
opw_buy = opw.get_sheet(0)  #写入 将op中的buy转为可写入
op_buy = op.sheet_by_name('buy') #读取 获取op中的buy sheet
op_buy_nrows = op_buy.nrows #获取OA中的行数
rawA_nrows = rawA.nrows 

#PB定位 a
for i in range(1,rawA_nrows):
    a = 0 
    for j in rawA.row_values(0):
        a = a+1
        if u'\u0050\u0042\uff0c\u6700\u65b0' in j:
            break
#PE定位 b
for i in range(1,rawA_nrows):
    b = 0 
    for j in rawA.row_values(0):
        b = b+1
        if u'\u0050\u0045\uff0c\u0054\u0054\u004d' in j:
            break
#解禁定位 c
for i in range(1,rawA_nrows):
    c = 0 
    for j in rawA.row_values(0):
        c = c+1
        if u'\u9650\u552e\u89e3\u7981\u65e5\u671f' in j:
            break
#所有者权益合计 定位 d
for i in range(1,rawA_nrows):
    d = 0 
    for j in rawA.row_values(0):
        d = d+1
        if u'\u6240\u6709\u8005\u6743\u76ca\u5408\u8ba1' in j:
            break
#商誉 定位 e
for i in range(1,rawA_nrows):
    e = 0 
    for j in rawA.row_values(0):
        e = e+1
        if u'\u5546\u8a89' in j:
            break



#EPS定位 n

for i in range(1,rawA_nrows):
    n = 0 
    for j in rawA.row_values(0):
        n = n+1
        if 'EPS' in j:
            EPS = rawA.row_values(i)[n-1]
            if EPS >= 1:
                PB = rawA.row_values(i)[a-1]
                if PB <= 1:
                    PE = rawA.row_values(i)[b-1]
                    if PE <= 12:
                        if u'\u94f6\u884c' not in rawA.row_values(i)[1]: #剔除银行股
                            equity = rawA.row_values(i)[d-1]
                            goodwill = rawA.row_values(i)[e-1]
                            print '买入', rawA.row_values(i)[0], rawA.row_values(i)[1],' ','EPS=',EPS, 'PB=', PB, 'PE=', PE, goodwill/equity,rawA.row_values(i)[c-1]



            
