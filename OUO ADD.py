# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:51:12 2020

@author: user
"""
def add (y,x,z):
    num = x+y+z
    return num

y = int(input("YOUR NUM1 :"))
x = int(input("YOUR NUM2 :"))
z = int(input("YOUR NUM3 :"))

YA = add(x,y,z)
print("A:",YA)