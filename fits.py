#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 23:03:45 2020

@author: blahblahmac
"""

from astropy.io import fits
from astropy import wcs
from astropy import units as u
import numpy as np
from astropy.coordinates import SkyCoord

from matplotlib.image import NonUniformImage
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
'''
hdul = fits.open('1.fits')
w = wcs.WCS(hdul[0].header)
hdr = hdul[0].header
#print(w.wcs.name)
#w.wcs.print_contents()

pixcrd = np.array([[0, 0], [24, 38], [45, 98]], dtype=np.float64)
world = w.wcs_pix2world(pixcrd, 0)
print(world)

pixcrd2 = w.wcs_world2pix(world, 0)
print(pixcrd2)
'''
'''
#hdul.info()
print(repr(hdr))
print(list(hdr.keys()))

from astropy import units as u
from astropy.coordinates import SkyCoord
import numpy as np

c = SkyCoord(ra=(1.080015330000E+01)*u.degree, dec=(4.165377920000E+01)*u.degree, frame='icrs')
w = wcs('1.fits')

r = np.load('ra.npy')
d = np.load('dec.npy')

c = SkyCoord(ra=(r)*u.degree, dec=(d)*u.degree, frame='icrs')
'''
r = np.load('ra.npy')
d = np.load('dec.npy')

c = np.vstack((r, d)).T

#c = SkyCoord(ra=(r)*u.degree, dec=(d)*u.degree, frame='icrs')


w = wcs.WCS(naxis=2)
w.wcs.crpix = [1.080015330000E+01, 4.165377920000E+01]
pixcrd2 = w.wcs_world2pix(c, 0)
#print(pixcrd2[0:, 1])

#np.histogram2d(pixcrd2[0:, 0],pixcrd2[0:, 1])
#plt.hexbin(pixcrd2[0:, 0],pixcrd2[0:, 1])
#plt.hist2d(pixcrd2[0:, 0],pixcrd2[0:, 1],bins = (200,200),cmap = 'Greys')

#clustering = DBSCAN(eps=1.69000005722046).fit(pixcrd2)
#labels = clustering.labels_ 
plt.hist2d(pixcrd2[0:, 0],pixcrd2[0:, 1],bins = (200,200),cmap = 'Reds')
plt.show()

