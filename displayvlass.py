from astropy.io import fits
from astropy import wcs

import os
import numpy as np
import matplotlib.pyplot as plt
import aplpy

target_url = 'http://www.cv.nrao.edu/~bkent/VLASS1.1.ql.T12t35.J231013+073000.10.2048.v1.I.iter1.image.pbcor.tt0.subim.fits'

VLASS_FITS = fits.open(target_url)

fig = plt.figure(facecolor='w', edgecolor='w', frameon=True, figsize=(10,9))

ax = aplpy.FITSFigure(VLASS_FITS, figure=fig)

ax.show_colorscale(cmap='magma', vmin=-.0001, vmax=0.00080)

ax.add_grid()
ax.grid.show()
ax.set_title(os.path.basename(target_url))

fig.canvas.draw()
