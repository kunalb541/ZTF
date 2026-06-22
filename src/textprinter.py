#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a DS9 region file from the alert coordinates.

Reads the saved RA/Dec arrays and prints out every alert position as a
DS9 "point" region, so the alerts can be overlaid on a FITS image in DS9.

Created on Thu Mar 12 01:06:24 2020
"""
# Prints out all the ra and dec for ds9

from pathlib import Path

import numpy as np

# Resolve paths relative to the repo root so the script runs from anywhere.
ROOT = Path(__file__).resolve().parent.parent
ARRAYS = ROOT / "data" / "arrays"

# Loading np array
r = np.load(ARRAYS / 'ra.npy')
d = np.load(ARRAYS / 'dec.npy')
num = len(r)
f = open(ROOT / "coord.txt", "w+")

for i in range(num):

    # if 10.24 <= r[i] <= 11.37 and 41.2 <= d[i] <= 43:

    f.write("point(")
    f.write(str(r[i]))
    f.write(",")
    f.write(str(d[i]))
    f.write(') # point=circle 4\n')


f.close()
