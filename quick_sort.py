# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:33:07 2024

@author: Madhumitha
"""
import random
def QuickSort(arr):
    if(len(arr)<=1):
        return arr
    
    pivot= random.choice(arr)
     
    left=[i for i in arr if i<pivot]
    right=[i for i in arr if i>pivot]
    middle=[i for i in arr if i==pivot]
     
    return QuickSort(left)+middle+QuickSort(right)

arr=[6,3,7,2,4,5] 
print(QuickSort(arr))