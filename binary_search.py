# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:39:34 2024

@author: Madhumitha
"""
nums=[-1, 0, 3, 5, 9, 12]
target=9

l=0
r=len(nums) - 1
found=False  

while(l<=r):
    m=(l+r)//2
    if (target==nums[m]):
        print(m)  
        found=True  
        break  
    elif (target>nums[m]):
        l=m+1
    elif (target<nums[m]):  
        r=m-1

else:
    print("not found")