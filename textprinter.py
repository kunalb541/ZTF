#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 01:06:24 2020

@author: blahblahmac
"""
# Prints out all the ra and dec for ds9

import numpy as np

#Loading np array
r = np.load('ra.npy')
d = np.load('dec.npy')
num = len(r)
f = open("coord.txt","w+")

for i in range(num):
    
    #if 10.24 <= r[i] <= 11.37 and 41.2 <= d[i] <= 43:
        
     f.write("point(")
     f.write(str(r[i]))
     f.write(",")
     f.write(str(d[i]))
     f.write(') # point=circle 4\n')
     

f.close() 
