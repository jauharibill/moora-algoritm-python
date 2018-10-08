#!/bin/bash
from math import sqrt
from cmath import sqrt


LENGTH_OF_ROW = 0
LENGTH_OF_COLUMN = 0

# clean data from dirty file text
with open('data/sample.txt', 'r') as file:
    with open('result/clean.txt', 'w') as newfile:
        for newdata in file:
            data_info = newdata.split(' ')
            data_count = len(data_info)
            for index, newdimension in enumerate(data_info):
                if newdimension!='' and newdimension!='\n':
                    if index<(data_count-2):
                        newfile.write(newdimension.strip()+',')
                    else:
                        newfile.write(newdimension.strip()+'\n')

print('success clean dimension!')

# create sqr.txt file that contain sqr for all element dimension
with open('result/clean.txt', 'r') as file:
    with open('result/sqr.txt', 'w') as newfile:
        for data in file:
            datainfo = data.split(',')
            datacount = len(datainfo)
            for index, newdata in enumerate(datainfo):
                datainfo[index] = int(datainfo[index])**2
                if index<(datacount-1):
                    newfile.write(str(datainfo[index])+' ') 
                else:
                    newfile.write('\n')

print('success sqr dimension')

# create file sumrow.txt that contain sum of all rows
with open('result/sqr.txt') as file:
    with open('result/sumrow.txt', 'w') as newfile:
        for data in file:
            datainfo = data.split(' ')
            datacount = len(datainfo) 
            sum_row = 0
            for index, newdata in enumerate(datainfo):
                if newdata!='\n':
                    sum_row += int(newdata)
            newfile.write(str(sum_row).rstrip('\n')+',')

print('success sum all rows')

with open('result/sumrow.txt', 'r') as file:
    with open('result/normalization.txt', 'w') as newfile:
        with open('result/sqr.txt', 'r') as sqr:
            for sumrow in file:
                splitIntoColumn = sumrow.split(',')
                # for index, column in enumerate(splitIntoColumn):
                    # indexColumn = 0
                    # print(column)
                indexColumn = 0
                for row in sqr:
                    datainfo = row.split(' ')
                    for index, newdata in enumerate(datainfo):
                        if newdata!='\n':
                            if splitIntoColumn[indexColumn]!='':
                                resultPerElement = int(splitIntoColumn[indexColumn])-int(newdata)
                            else:
                                resultPerElement = 0
                            if resultPerElement>0:
                                sqrtElement = sqrt(int(newdata))
                                resultPerElement = sqrt(resultPerElement)
                                result = sqrtElement/resultPerElement
                            else:
                                sqrtElement = 0
                                resultPerElement = 0 
                                result = 0
                            newfile.write(str(result.real)+' ')
                    newfile.write('\n')
                    indexColumn += 1

print('success normalized!')

                
