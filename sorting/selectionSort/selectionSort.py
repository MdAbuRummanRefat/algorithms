# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 22:43:36 2018

@author: iu_refat
"""

# to implement selection sort using python
import sys
arr=[22,11,24,34,5,13]
#travel through all element of array
for i in range(len(arr)):
    index=i
    #find minimum elment of subarray
    for j in range(i+1,len(arr)):
        if arr[j]<arr[index]:
            index=j
    #swap the minimum element of array with first element
    arr[i],arr[index]=arr[index],arr[i]
    
#print the sorted array
for i in range(len(arr)):
    print(arr[i])
    
     