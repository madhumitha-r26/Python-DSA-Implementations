# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:33:08 2024

@author: Madhumitha
"""

arr=[14,33,27,10,10,35,19,42,44]
for pos in range(len(arr)-1):
    min=pos
    for i in range(pos+1,len(arr)):
        if(arr[i]<arr[min]):
            min=i
    arr[min],arr[pos]=arr[pos],arr[min]
    print(arr)