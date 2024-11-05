# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 11:33:03 2024

@author: Madhumitha
"""

#importing
import array as ar

#initialization
arr=ar.array('i',[1,2,3,4,5])
print("displaying the array with the type code:",arr)
a=list(arr) #converting to list
print("displaying the array after converting to list:",a)

#accessing
print("accessing element at 4th index:",a[4])

#inserting
a.insert(0,6)
print("inserting element at 0th position:",a)

#deleting
a.pop(3)
print("deleting element at 0th position:",a)

#searching
print("checking whether the particular element exists or not:")
for i in a:
    if(i==2):
        print("True")
        break
