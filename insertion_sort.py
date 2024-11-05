# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:33:09 2024

@author: Madhumitha
"""

arr=[4,3,2,10,12,1,5,6]
for i in range(1,len(arr)):
    cur=arr[i]
    j=i-1
    while((j>=0) and (cur<arr[j])):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=cur
print(arr)