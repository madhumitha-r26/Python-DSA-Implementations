# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 16:33:08 2024

@author: Madhumitha
"""

def MergeSort(arr):
    if(len(arr)>1):
        middle=len(arr)//2
        left=arr[:middle]
        right=arr[middle:]
        MergeSort(left)
        MergeSort(right)
        
        lp=0
        rp=0
        fp=0
        while(lp<len(left) and rp<len(right)):
            if(left[lp]<right[rp]):
                arr[fp]=left[lp]
                lp+=1
            else:
                arr[fp]=right[rp]
                rp+=1
            fp+=1
        while(lp<len(left)):
            arr[lp]=left[lp]
            fp+=1
            lp+=1
        while(rp<len(right)):
            arr[fp]=right[rp]
            fp+=1
            rp+=1
            lp+=1
    
    return arr

arr=[38,27,43,3,9,82,10]
print(MergeSort(arr))