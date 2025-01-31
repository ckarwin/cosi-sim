2024/July/18 Pierre Jean

This is the description of the model of the diffuse emission due to the steady state annihilation of positrons produced by 44Ti decay in our Galaxy.

The spatial distribution is derived from the calculation of the propagation of positrons in our Galaxy. The initial positions of positrons follow the model NE2001 of Cordes & Lazio (2002, arXiv:astro-ph/0207156) that fits the distribution of massive stars in our Galaxy, with a fraction of 44Ti in the bulge of 2%, which corresponds to the fraction of massive stars also used for the 26Al. The positron propagation method is described in Alexis et al. (2014 - https://ui.adsabs.harvard.edu/abs/2014A%26A...564A.108A/abstract). The positron rate due to 44Ti decay is ~3 x 10^42 e+/s (see section 2.3 of Alexis et al. 2014).
The spectral distribution takes into account the annihilation line and the orthopositronium continuum. It was obtained from the model of Guessoum et al (2005 - https://ui.adsabs.harvard.edu/abs/2005A%26A...436..171G/abstract) that compute a spectrum for each phase of the interstellar medium. The spectral model was corrected by the Galactic rotation using the model of Fich, Blitz and Stark (1989 - https://ui.adsabs.harvard.edu/abs/1989ApJ...342..272F/abstract) for R > 3 kpc and a solid rotation model for R < 3 kpc.

The input fits file (annihilation_pos_from_44Ti_v2.fits.gz) contains the intensity (ph/s/cm2/keV/sr) as a function of the Galactic coordinates and the photon energy (l, b, E) with a binning of 1 deg x 1 deg x 0.1 keV. Some hot spots at high latitudes, due to close positron annihilations, were removed with a filter. The total flux for E > 100 keV is 1.7e-3 ph/s/cm^2. The input file has 3 extensions:
> primary extension => intensity matrix
> second extension => longitude values (deg)
> third extension => latitude values (deg)
> fourth extension => energy values (keV)
This fits file (annihilation_pos_from_44Ti_v2.fits.gz) has been converted to the COSIMA-specific format ("3D Functions"): annihilation_pos_from_44Ti_v2.dat

Goal: Detection of the diffuse line and continuum emissions, detection of the Doppler shift in the disk, detection of the spectral shape.

2025/January/28 Pierre Jean

The energy binning has been changed in order to reduce the size of the input files.
The spectral distribution has been separated into two files: the line (_line) and the ortho-positronium continuum (_cont).
The files Positrons_from_44Ti_line.source and Positrons_from_44Ti_cont.source should be used.