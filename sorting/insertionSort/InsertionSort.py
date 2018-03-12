# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:57:57 2018

@author: iu_refat
"""

#Python program to implement insertion sort

#functon to do insertion sort
def insertionSort(arr):
    #travel thtough 1 to len(arr)
    for i in range(1,len(arr)):
        key=arr[i]
        #move element [0..i-1]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
        
#main function
arr=[2,1,5,3,6]
#call insertion sort function
insertionSort(arr)
print("sorted array is :")
for i in range(0,len(arr)):
    print("%d" %arr[i])