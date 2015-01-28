import numpy as np
import matplotlib.pyplot as plt

#cm = plt.cm.get_cmap('RdYlBu')

'''
List of stars near many open clusters in the SDSS. Compiled via CASJOBS SQL QUERY.
'''
datatype = [('id', '|S10'), ('ra', '<f8'), ('dec','<f8'), ('type', '|S7'), ('distance', '<f8'), \
('modelMag_g', '<f8'),('modelMag_r', '<f8'), ('modelMag_i', '<f8'), ('modelMag_z', '<f8'), \
('mode', '<i5'), ('clean', '<i5'), ('modelMagErr_g', '<f8'),('modelMagErr_r', '<f8')]
data = np.genfromtxt('ClustersListResultsv2.csv', names=True, delimiter=',', dtype=datatype)

g = data['modelMag_g']; r = data['modelMag_r']
wh=np.where( (data['id'] == 'NGC6791' ) & (data['modelMag_r']/data['modelMagErr_r'] > 5.) & \
(data['modelMag_g']/data['modelMagErr_g'] > 5.))
clf()
wg = g[wh]; wr = r[wh]
wcol = wg - wr
#print "length of colors = ", len(wcol)
plt.plot( wcol, wr,  'ro', alpha=0.5, markersize=2.25) 

plt.ylim(23, 10); plt.xlim(-0.5,3)
plt.xlabel(r'$g -r$' + ' [mag]')
plt.ylabel(r'$r$' + ' [mag]')

b25_u =  0.000
b25_g = -0.060
b25_r = -0.035
b25_i = -0.041
b25_z =  0.030

uP_gP_zp = 1.39  
gP_rP_zp = 0.53  
rP_iP_zp = 0.21  
iP_zP_zp = 0.09  

isodata = np.genfromtxt('isoc_z040a.dat', names=True, comments='#', skip_header=1)
gP=isodata['g'];  rP=isodata['r']; iP=isodata['i'];  
'''
Theoretical isochrones in several photometric systems
I. Johnson-Cousins-Glass, HST/WFPC2, HST/NICMOS, 
Washington, and ESO Imaging Survey filter sets"
by L. Girardi, G. Bertelli, A. Bressan, C. Chiosi, 
M.A.T. Groenewegen, P. Marigo, B. Salasnich, and A. Weiss,
2002, Astronomy & Astrophysics, in press (astro-ph/0205080).
'''
#u = uP - b25_u*( (uP-gP)-uP_gP_zp )
g = gP - b25_g*( (gP-rP)-gP_rP_zp )
r = rP - b25_r*( (rP-iP)-rP_iP_zp )
#i = iP - b25_i*( (rP-iP)-rP_iP_zp )
#z = zP - b25_z*( (iP-zP)-iP_zP_zp )
col = g - r
wh = np.where((isodata['logage_yr'] == 9.95) & (g - r < 1.5))
plt.plot(col[wh]+0.15, r[wh]+13.3, 'bo', label='9 Gyr',  linestyle='--')
plt.text(2.25, 12, r'$Z = 0.040$', fontweight='bold', fontsize=16)
plt.legend(loc="upper right", frameon=False)
plt.title('NGC 6791 : ' + r'$r - M_r = 5log(g) - 5 + A_r = 13.4 $')
plt.minorticks_on()
plt.savefig("NGC6791_CMD.pdf",dpi=400)


