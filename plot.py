#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 22:35:43 2020

@author: blahblahmac
"""

import numpy as np
import matplotlib.pyplot as plt
import statistics as st
'''
jd = np.load('jd.npy')
jd = jd - min(jd)
plt.clf()

plt.figure(1)
plt.hist(jd,200)
plt.title('jd')
plt.savefig("jd",dpi = 1200)
plt.show()
'''

fwhm = np.load('fwhm.npy')
plt.clf()

plt.figure(1)
plt.hist(fwhm,200)
plt.title('fwhm')
plt.savefig("fwhm",dpi = 1200)
plt.show()

print(st.median(fwhm))