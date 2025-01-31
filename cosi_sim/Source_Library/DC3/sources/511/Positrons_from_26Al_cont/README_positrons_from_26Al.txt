2024/July/16 Pierre Jean

This is the description of the model of the diffuse emission due to the steady state annihilation of positrons produced by 26Al decay in our Galaxy.

The spatial distribution is derived from the calculation of the propagation of positrons in our Galaxy. The initial positions of positrons follow the model NE2001 of Cordes & Lazio (2002, arXiv:astro-ph/0207156) that fits the distribution of massive stars in our Galaxy, with a fraction of 26Al in the bulge of 2%. The positron propagation method is described in Alexis et al. (2014 - https://ui.adsabs.harvard.edu/abs/2014A%26A...564A.108A/abstract).  
The spectral distribution takes into account the annihilation line and the orthopositronium continuum. It was obtained from the model of Guessoum et al (2005 - https://ui.adsabs.harvard.edu/abs/2005A%26A...436..171G/abstract) that compute a spectrum for each phase of the interstellar medium. The spectral model was corrected by the Galactic rotation using the model of Fich, Blitz and Stark (1989 - https://ui.adsabs.harvard.edu/abs/1989ApJ...342..272F/abstract) for R > 3 kpc and a solid rotation model for R < 3 kpc.

The input fits file (annihilation_pos_from_26Al_v2.fits.gz) contains the intensity (ph/s/cm2/keV/sr) as a function of the Galactic coordinates and the photon energy (l, b, E) with a binning of 1 deg x 1 deg x 0.1 keV. The input files has 3 extensions:
> primary extension => intensity matrix
> second extension => longitude values (deg)
> third extension => latitude values (deg)
> fourth extension => energy values (keV)
This fits file (annihilation_pos_from_26Al_v2.fits.gz) has been converted to the COSIMA-specific format ("3D Functions"): annihilation_pos_from_26Al_v2.dat

Goal: Detection of the diffuse line and continuum emissions, detection of the Doppler shift in the disk, detection of the spectral shape, correlation with the 26Al map (1809 keV emission).
The input fits file for the corresponding 26Al map is 3Dmap_26Al_ne2001_v2.fits.gz, which has a format similar to the one of annihilation_pos_from_26Al_v2.fits.gz. 

2025/January/28 Pierre Jean

The energy binning has been changed in order to reduce the size of the input files.
The spectral distribution has been separated into two files: the line (_line) and the ortho-positronium continuum (_cont).
The files Positrons_from_26Al_line.source and Positrons_from_26Al_cont.source should be used.