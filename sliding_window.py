# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:22:16 2024

@author: Madhumitha
"""
nums=[1,2,3,4,5,6]
target=9

l=0
r=0
minimum=[]
subsum=0
while(r<len(nums)):
    subsum+=nums[r]
    while(subsum>=target):
        minimum.append(r-l+1)
        subsum-=nums[l]
        l+=1
    r+=1
if len(minimum)==0:
    print("0")
else:
    print(min(minimum))