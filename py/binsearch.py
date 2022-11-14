# filename: binsearch.py
# Ed Hawkins
# CSCI 77800 Fall 2022
# collaborators: me, myself, I
# consulted: ThinkPython
#
# Binary Search
#
#create random data set
from random import random
data = []
for i in range(10):
    data = data+[int(10*random()+1)]
print(data)
#sort data set
for i in range(9):
    for j in range(9):
        if(data[j+1]<data[j]):
            temp=data[j]
            data[j]=data[j+1]
            data[j+1]=temp
print(data)
#binary search function: find index of first instance of tgt in data
def binarySearch(tgt,data):
    min=0
    max=len(data)-1
    middle = int((min+max)/2)
    while (min < max):
        if (data[middle]==tgt):
            return middle
        elif (data[middle]<tgt):
            min = middle
            middle = int((min+max)/2)
        else:
            max = middle
            middle = int((min+max)/2)
#call binarySearch and print result
print(binarySearch(5,data))
    

