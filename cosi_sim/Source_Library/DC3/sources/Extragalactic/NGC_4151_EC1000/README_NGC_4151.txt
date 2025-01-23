###########################################
#
##-- Created by Lea Marcotulli, Sept 10 2024
#
###########################################

This folder contains the spectral model of the AGN NGC 4151. 

The columns in each file are: Format <Energy in keV> <Spectrum in ph cm^-2 s^-1 keV^-1>
The energy band used is 100 keV to 10000 keV


The baseline model is a powerlaw with exponential cut-off. 


NGC_4151_ec200__COSI.dat - flux in the 20-30 keV calibrated from NuSTAR observations; Gamma=1.75, Ecut=200 keV
NGC_4151_ec1000_COSI.dat - flux in the 20-30 keV calibrated from NuSTAR observations; Gamma=1.75, Ecut=1000 keV

NGC_4151_bright_COSI.dat - bright state flux calibrated from INTEGRAL observation of Lubinski+2010; Gamma=1.71, Ecut=264 keV
NGC_4151_faint_COSI.dat  - faint state flux calibrated from INTEGRAL observation of Lubinski+2010; Gamma=1.81, Ecut=1000 keV

The goal of these data for COSI is: determine flux in the COSI band, and coronal cut-off location



