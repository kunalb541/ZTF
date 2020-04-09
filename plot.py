"""
Created on Tue Mar 10 22:35:43 2020

@author: blahblahmac
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import statistics as st

## Loading different arrays
''' 
jd = np.load('jd.npy')
fwhm = np.load('fwhm.npy')
m = np.load('')
m = np.load('')
b = np.load('')
s = np.load('')
f = np.load('')

# Substracting  min jd
jd = jd - min(jd)

plt.clf()

#Plotting diff figures
plt.figure(1)
plt.hist(m, bins = 20)
plt.title('magpsf')
plt.show()
plt.savefig("magpsf",dpi = 1200)

plt.figure(2)
plt.hist(b, bins = 20)
plt.title('bogus score')
plt.savefig("bogus score",dpi = 1200)
#plt.show()

plt.figure(3)
plt.hist(s, bins = 20,)
plt.title('spsf')
plt.savefig("spsf",dpi = 1200)
#plt.show()

plt.figure(4)
plt.hist(jd,400)
plt.title('Julian Date from the start of the survey')
plt.ylabel('Number of Alerts')
plt.xlabel('Julian Date (after substracting the minimum)')
plt.savefig("jd",dpi = 1200)
plt.show()
'''
fwhm = np.load('nparray/fwhm.npy')
plt.hist(fwhm)
plt.title('fwhm')
plt.savefig("fwhm",dpi = 1200)
#plt.show()

print(st.median(fwhm))
