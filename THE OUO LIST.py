# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:01:41 2020

@author: user
"""

SCORE = []
OAO = 0
OUO = 100
TOTAL = 0
P = int(input("PEPOLE :"))

for i in range (P):
    n = int(input("SCORE :"))
    SCORE.append(n)
    
    if n > OAO:
        OAO = n
    if n < OUO :
        OUO = n
    TOTAL = TOTAL + n
    
s = TOTAL/len(SCORE)
print("TOTAL :",TOTAL)
print("ALL :",s)
print("BEST SCORE :",OAO)
print("NOPE OAO :",OUO)