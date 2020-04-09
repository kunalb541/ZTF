import json
import urllib.request
import time
import numpy as np

start_time = time.time()

url1 = "https://mars.lco.global/?objectcone=m31%2C1.5&page="
url2 = "&format=json"

#Data to be extracted from the saved alerts json file 
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
for x in range(1,352):
    
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

# Saving all files as  np  arrays
np.save('nparray/magpsf',magpsf)
np.save('nparray/fid',fid)
np.save('nparray/xpos',xp)
np.save('nparray/ypos',yp)
np.save('nparray/distnr',distnr)
np.save('nparray/sigmagap',sigmagap)
np.save('nparray/rb',rb)
np.save('nparray/ra',ra)
np.save('nparray/dec',dec)
np.save('nparray/jd',jd)
np.save('nparray/fwhm',fwhm)
