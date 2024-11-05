# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:42:06 2024

@author: Madhumitha
"""
# =============================================================================
# TWO SUMS-2
# =============================================================================

arr=[1,2,3,4,5,6]
t=10
h=1
l=0
r=len(arr)-1


while(l<r):
    act=arr[l]+arr[r]
    if(act==t):
        print("printing the elements:",arr[l],arr[r]) #printing the elements
        print("printing the index values:",l,r) #printing the index values
        h=1
        break
    elif(act<t):
        l=l+1
    elif(act>t):
        r=r-1
if(h==0):
    print("no combination")
