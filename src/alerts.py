#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download ZTF transient alerts around the Andromeda galaxy (M31).

Queries the MARS/LCO alert broker for every alert within a cone search
centred on M31, paging through the JSON results. The candidate properties
of interest are pulled out and saved as NumPy arrays under data/arrays/.

Note (2020): the full run takes ~27 minutes because it pages through the
results one at a time rather than using the bulk JSON API. Total alerts
collected was ~35,000.

Created 2020.
"""

import json
import urllib.request
import time
from pathlib import Path

import numpy as np

# Resolve paths relative to the repo root so the script runs from anywhere.
ROOT = Path(__file__).resolve().parent.parent
ARRAYS = ROOT / "data" / "arrays"
ARRAYS.mkdir(parents=True, exist_ok=True)

start_time = time.time()

url1 = "https://mars.lco.global/?objectcone=m31%2C1.5&page="
url2 = "&format=json"

# Data to be extracted from the saved alerts json file
magpsf = np.zeros(35100)
fid = np.zeros(35100)
xp = np.zeros(35100)
yp = np.zeros(35100)
distnr = np.zeros(35100)
rb = np.zeros(35100)
sigmagap = np.zeros(35100)
jd = np.zeros(35100)
fwhm = np.zeros(35100)
ra = np.zeros(35100)
dec = np.zeros(35100)

j = 0

# Loop to get results by parsing one page by one
# The whole json file is saved. (jdata)
for x in range(1, 352):

    tempurl = url1 + str(x) + url2
    data = urllib.request.urlopen(str(tempurl)).read().decode()
    jdata = json.loads(data)
    jdata = jdata['results']

    for i in range(len(jdata)):

        temp = jdata[i]['candidate']
        magpsf[j] = temp['magpsf']

        fid[j] = temp['fid']
        xp[j] = temp['xpos']
        yp[j] = temp['ypos']
        distnr[j] = temp['distnr']

        sigmagap[j] = temp['sigmagap']
        rb[j] = temp['rb']
        fwhm[j] = temp['fwhm']
        jd[j] = temp['jd']
        ra[j] = temp['ra']
        dec[j] = temp['dec']
        j = j + 1

print("--- %s seconds ---" % (time.time() - start_time))

# Saving all files as np arrays
np.save(ARRAYS / 'magpsf', magpsf)
np.save(ARRAYS / 'fid', fid)
np.save(ARRAYS / 'xpos', xp)
np.save(ARRAYS / 'ypos', yp)
np.save(ARRAYS / 'distnr', distnr)
np.save(ARRAYS / 'sigmagap', sigmagap)
np.save(ARRAYS / 'rb', rb)
np.save(ARRAYS / 'ra', ra)
np.save(ARRAYS / 'dec', dec)
np.save(ARRAYS / 'jd', jd)
np.save(ARRAYS / 'fwhm', fwhm)
