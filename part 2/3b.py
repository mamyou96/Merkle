# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:59:27 2019

@author: Mohammad_Younesi
"""

import hashlib
import math

def calculate_merkle_root(myhash , m):
    n = 20
    height = int(n/2)
    d = int(math.log2(n))+1
    toPrint = []
    merkle = myhash
    if(m%2 == 0):
        toPrint.append(myhash[m+1])
    else:
        toPrint.append(myhash[m-1])

        
    while(d!=0):
        for i in range(height):
            merkle[i] = myHash(merkle[2*i] + merkle[2*i+1])
        if(height%2 == 1):
            merkle[height] = merkle[height - 1]
            height+=1
        if(d!=1):
            toPrint.append(merkle[int(m/2) + pow(-1,int(m/2))])
        m = int(m/2)
        height = int(height/2)
        d-=1
    print(merkle[0])
    
    return toPrint

def myHash(text):
    n = hashlib.sha256(str(text).encode('utf-8'))
    return n.hexdigest()

myhash = [None for _ in range(20)]
n=20

for i in range(n):
    myhash[i] = input()

m = int(input()) - 1
A = calculate_merkle_root(myhash , m)
for a in A:
    print(a)
