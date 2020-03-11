import json
import urllib.request
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

'''
m = np.zeros(35000)
b = np.zeros(35000)
s = np.zeros(35000)
'''
jd = np.zeros(35000)
f = np.zeros(35000)
ra = np.zeros(35000)
dec = np.zeros(35000)

j = 0

url1 = "https://mars.lco.global/?objectcone=m31%2C1.5&page="
url2 = "&format=json"


for x in range(1,351):
    
    tempurl = url1 + str(x) + url2
    data = urllib.request.urlopen(str(tempurl)).read().decode()
    obj = json.loads(data)
    
    obj = obj['results']
    
    for i in range(len(obj)):
        
        temp = obj[i]['candidate']
        
        '''
        m[j] = temp['magpsf']
        s[j] = temp['sigmagap']
        b[j] = temp['rb']
        '''
        f[j] = temp['fwhm']
        jd[j] = temp['jd']
        ra[j] = temp['ra']
        dec[j] = temp['dec']
        j = j + 1

np.save('ra',ra)
np.save('dec',dec)
np.save('jd',jd)
np.save('fwhm',f)
'''
j = 0
jdf = [np.array([])
       
for x in jdf:
    jd = np.append(jd, x)

for x in jd:
    
    if x > 12000:
        
        jdf[j] = jd[j]
        
no = min(jdf)
jd = [x - no for x in jdf]


plt.clf()

plt.figure(1)
plt.hist(m, bins = 20)
plt.title('magpsf')
#plt.show()
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
plt.title('jd')
plt.savefig("jd",dpi = 1200)
plt.show()

plt.figure(5)
plt.hist(f)
plt.title('fwhm')
plt.savefig("fwhm",dpi = 1200)
plt.show()
'''
print("--- %s seconds ---" % (time.time() - start_time))

