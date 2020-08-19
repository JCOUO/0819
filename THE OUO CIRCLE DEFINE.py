# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:20:46 2020

@author: user
"""
def OUO (x):
    num = x*2*3.14
    return num
def OAO (y):
    num = y*y*3.14
    return num

n = int(input("YOUR CIRCLE :"))
w = OUO(n)
Q = OAO(n)
print("CIRCUM :",w)

print("AREA :",Q)