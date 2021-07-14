#test_telescope.py

from astropy.io import fits

def check_telescope(url):
    hdul = fits.open(url)
    return hdul[0].header['TELESCOP']
  
def test_check_telescope():
    target_url = 'http://www.cv.nrao.edu/~bkent/VLASS1.1.ql.T12t35.J231013+073000.10.2048.v1.I.iter1.image.pbcor.tt0.subim.fits'
    
    assert check_telescope(target_url) == 'EVLA'
