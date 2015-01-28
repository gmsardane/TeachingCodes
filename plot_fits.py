import sys
import numpy as np
import matplotlib.pyplot as plt
import astropy.io.fits as fits

spec, header = fits.getdata(sys.argv[1], 1, header=True) #Load in data
wave=10**spec['loglam'] #wavelength converted from the log.
err=np.sqrt(1./spec['ivar']) #Error array. ivar =  inverse of the square of the estimated error 
plt.plot(wave, spec['flux'], label='Flux', linestyle='-')
plt.plot(wave, err, 'r', label='Error', linestyle='-')
plt.xlabel(r'Observed Wavelength, [$\AA$]')
plt.ylabel(r'$f_{\lambda}$, [$10^{-17} erg s^{-1}cm^{-2}\AA^{-1}]$')
plt.title('Quasar with emission redshift at z = 1.72')
plt.xlim([3800,9200] )
plt.minorticks_on()
plt.legend(loc="upper right", frameon=False)
plt.text(4100, 65, 'CIV')
plt.text(5100, 43, 'CIII')
plt.text(7500, 32, 'MgII')
plt.savefig("Quasar.pdf",dpi=400)
