#!/usr/bin/env python2

import argparse
import pandas as pd
import math

#command arguements
parser = argparse.ArgumentParser(description='Sort CSV file according to mentioned columns')
parser.add_argument('file', help='csv file to import', action='store')
parser.add_argument('col_1', help="Enter name of column one", action='store')
parser.add_argument('col_2', help="Enter name of column two", action='store')
args = parser.parse_args()

#read input parameters
filename = args.file
column_1 = args.col_1
column_2 = args.col_2

#open CSV file
csv_file = open(filename,'r')

#read CSV file
df = pd.read_csv(csv_file)

#extract required columns
saved_column_1 = df[str(column_1)].tolist()
saved_column_2 = df[str(column_2)].tolist()

#copy extracted columns
alist = saved_column_1
blist = saved_column_2

#extract row and column number
row_number = df['row'].tolist()
column_number = df['column'].tolist()

#remove nan
def removeNan(alist,blist):
    for i in range(len(alist)):
	if math.isnan(alist[i])==1:
	    alist[i]=0
	if math.isnan(blist[i])==1:
	    blist[i]=0

#sort
def bubbleSort(alist,blist,row_number,column_number):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
	    if alist[i] + blist[i] < alist[i+1] + blist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                temp1 = blist[i]
                blist[i] = blist[i+1]
                blist[i+1] = temp1
                row_temp = row_number[i]
                row_number[i] = row_number[i+1]
                row_number[i+1] = row_temp
                column_temp = column_number[i]
                column_number[i] = column_number[i+1]
                column_number[i+1] = column_temp

#call functions
removeNan(alist,blist)
bubbleSort(alist,blist,row_number,column_number)

#open YAML file
afile = open('output.yaml', 'w')

#write on the YAML file
for i in range(3):
    afile.write('-row: %s' %row_number[i])
    afile.write('\n')
    afile.write(' column: %s' %column_number[i])
    afile.write('\n')
    afile.write(' data: %s' %column_1)
    afile.write('=%s' %alist[i])
    afile.write(' ')
    afile.write(' %s' %column_2)
    afile.write('=%s' %blist[i])
    afile.write('\n')

    
