# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:38:53 2024

@author: Madhumitha
"""

arr=[1,2,3,4,5]
x=3
for i in range(0,len(arr)):
    if(arr[i]==x):
        print("True")
        break
else:
    print("False")