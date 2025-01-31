2024/July/16 Pierre Jean

This is the description of the model of the 1809 keV line diffuse emission due decay of 26Al in our Galaxy.

The spatial distribution is derived from the model NE2001 of Cordes & Lazio (2002, https://arxiv.org/abs/astro-ph/0207156) that fits 
the distribution of massive stars in our Galaxy. The fraction of 26Al in the bulge is 2%. This value is a compromise between SPI observations and results of studies of star formation rate in this region. 
The shape of the line in each spatial bin takes into account the turbulence of the interstellar medium and the Galactic rotation using the model of Fich, Blitz and Stark 
(1989 - https://ui.adsabs.harvard.edu/abs/1989ApJ...342..272F/abstract) for R > 3 kpc and a solid rotation model for R < 3 kpc.

The input fits file (3Dmap_26Al_ne2001_v2.fits.gz) contains the intensity (ph/s/cm2/keV/sr) as a function of the Galactic coordinates and the photon energy (l, b, E) with a binning of 1 deg x 1 deg x 0.1 keV. The input files has 3 extensions:
> primary extension => intensity matrix
> second extension => longitude values (deg)
> third extension => latitude values (deg)
> fourth extension => energy values (keV)
The fits file (3Dmap_26Al_ne2001_v2.fits.gz) has been converted to the COSIMA-specific format ("3D Functions"): 3Dmap_26Al_ne2001_v2.dat

Goal: Detection of the diffuse emission, detection of the Doppler shift in the disk, detection of the spectral shape, correlation with the emission of the galactic positron annihilations, extract F(26Al)/F(60Fe) ratio and its uncertainty.


2024/July/18 Pierre Jean

The input files, in .fits and .dat format, for the disk and bulge components of the model "3Dmap_26Al_ne2001_v2" are 3Dmap_26Al_disk_ne2001_v2.* and 3Dmap_26Al_bulge_ne2001_v2.*, respectively.

2025/January/28 Pierre Jean

The energy binning has been changed in order to reduce the size of the input files.
