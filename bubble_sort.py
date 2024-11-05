# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:33:04 2024

@author: Madhumitha
"""

arr=[14,33,27,35,10]
for i in range(0,len(arr)-1):
    for j in range(0,len(arr)-1):
        if(arr[j]<arr[j+1]):
            continue
        elif(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
    print(arr)