# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 18:11:29 2024

@author: Madhumitha
"""

# =============================================================================
# FACTORIAL OF A NUMBER
# =============================================================================

def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
print("factorial of 4 is:",factorial(4))

# =============================================================================
# SUM OF N NATURAL NUMBERS
# =============================================================================

def sum_of_natural(n):
    if(n==1):
        return 1
    else:
        return n+sum_of_natural(n-1)
print("sum 5 natural numbers is:",sum_of_natural(5))
    