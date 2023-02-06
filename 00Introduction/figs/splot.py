from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import sunpy.visualization.colormaps

a=fits.open("20140528_161615_14euA.fts")
hd=a[0].header
x=(np.array((0, hd['NAXIS1']))-hd['CRPIX1'])*hd['CDELT1']+hd['CRVAL1']
y=(np.array((0, hd['NAXIS2']))-hd['CRPIX2'])*hd['CDELT2']+hd['CRVAL2']
plt.imshow(a[0].data, extent=[*x, *y], cmap='sdoaia304', origin='lower', vmin=40, vmax=800)
plt.ylim(-100, 200)
plt.xlim(-1150, -750)
plt.xlabel('Helioprojective Longitude [arcsec]')
plt.ylabel('Helioprojective Latitude [arcsec]')
plt.colorbar(label='DN')
plt.title(hd['OBSRVTRY'].replace('_', '-')+' '+hd['INSTRUME'].strip()+' '+hd['DATE-OBS'][:-4].replace('T', ' '))
plt.show()
