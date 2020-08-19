# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:15:17 2020

@author: user
"""

SCORE = []
OAO = 0
OUO = 100
YA = 0
NO = 100
TOTAL = 0
P = int(input("PEPOLE :"))


for i in range (P):
    Q = str(input("NAME :"))
    n = int(input("SCORE :"))
    SCORE.append(n)
    a = int(Q)
    if n > OAO:
        OAO = n
    if n < OUO :
        OUO = n
    if a > YA:
        YA = a
    if a < NO :
        NO = a
    TOTAL = TOTAL + n
    
s = TOTAL/len(SCORE)
print("BEST name :",NO)
print("NOPE name :",Q)
print("TOTAL :",TOTAL)
print("ALL :",s)
print("BEST SCORE :",OAO)
print("NOPE OAO :",OUO)