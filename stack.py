# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:03:59 2024

@author: Madhumitha
"""

#importing
from collections import deque
st=deque([1,2,3,4])

#to access the last element
print("accessing top most stack element:",st[-1])

#inserting
st.append(5)
print("inserting element to stack:",st)
print("accessing top most stack element:",st[-1])

#deleting
st.pop()
print("deleting element from stack:",st)

print("------------------------------------------------------------")
#-----------------------------------------------------------------

#initialization
empty_stack=[]
print("empty stack:",empty_stack)
stack=[1,2,3,4]
print("stack with elements:",stack)

#accessing
print("accessing top most stack element:",stack[-1])

#inserting
stack.append(5)
print("inserting element to stack:",stack)
print("accessing top most stack element:",stack[-1])

#deleting
stack.pop()
print("deleting element from stack:",stack)
print("accessing top most stack element:",stack[-1])

#searching
print("checking whether the particular element exists or not:")
x=4
if(stack[-1]==x):
    print("True")
else:
    print("False")