"""
Created on Tue Mar 10 22:35:43 2020

@author: blahblahmac
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import statistics as st

# Loading different arrays
magpsf = np.load('nparray/magpsf.npy')
rb = np.load('nparray/rb.npy')
jd = np.load('nparray/jd.npy')
sigmagap = np.load('nparray/sigmagap.npy')
fwhm = np.load('nparray/fwhm.npy')

# Substracting  min jd
jd = jd - min(jd)

#printing median of fwhm
print(st.median(fwhm))

#plt.clf()

#Plotting diff figures
#Magpsf
plt.figure(1)
plt.hist(magpsf, bins = 20)
plt.title('Magnitude from PSF-fit photometry')
plt.ylabel('No of alerts')
plt.xlabel('Mag')
#plt.show()
plt.savefig("graphs/magpsf",dpi = 1200)

#RB
plt.figure(2)
plt.hist(rb, bins = 20)
plt.title('RealBogus quality score')
plt.ylabel('No of alerts')
plt.xlabel('RB Score')
#plt.show()
plt.savefig("graphs/rb",dpi = 1200)

#JD
plt.figure(3)
plt.hist(jd, bins = 20)
plt.title('Julian Date')
plt.ylabel('No of alerts')
plt.xlabel('Julian Date - min')
#plt.show()
plt.savefig("graphs/jd",dpi = 1200)

'''
#Sigmagap
#plt.figure(4)
plt.hist(sigmagap, bins = 20)
plt.title('1-sigma uncertainty in magpsf')
plt.ylabel('No of alerts')
plt.xlabel('MAG')
#plt.show()
plt.savefig("graphs/sigmapsf",dpi = 1200)
'''

#FWHM
plt.figure(5)
plt.hist(fwhm, bins = 20)
plt.title('Full Width Half Max assuming a Gaussian core, from SExtractor')
plt.ylabel('No of alerts')
plt.xlabel('Pixels')
#plt.show()
plt.savefig("graphs/fwhm",dpi = 1200)



print(st.median(fwhm))
