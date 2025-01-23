# Source Library <br />
All sources from COSI's data challenges are available here. Sources must be specified in the input yaml file just as given below, i.e. including the relative path from the Source_Library directory. 

## Data Challenge 1 (DC1) <br /> 
DC1/crab <br />
DC1/crab_10xFlux <br />
DC1/cenA <br />
DC1/cenA_10xFlux <br />
DC1/vela <br />
DC1/vela_10xFlux <br />
DC1/cygX1 <br />
DC1/cygX1_10xFlux <br />
DC1/LingBG <br />
DC1/Al26 <br />
DC1/Al26_10xFlux <br /> 
DC1/GC511A <br />
DC1/GC511A_10xFlux <br />
DC1/GC511B <br />
DC1/OrthoPs <br />

## Data Challenge 2 (DC2) <br />
DC2/proto_dc2/gruber99 <br />
DC2/proto_dc2/gruber99_LEO <br />
DC2/backgrounds/PrimaryProtons <br />
DC2/backgrounds/PrimaryAlphas <br />
DC2/backgrounds/CosmicPhotons <br />
DC2/backgrounds/AtmosphericNeutrons <br />
DC2/backgrounds/PrimaryElectrons <br />
DC2/backgrounds/AlbedoPhotons <br />
DC2/backgrounds/PrimaryPositrons <br />
DC2/backgrounds/SecondaryProtons <br />
DC2/sources/511/511_ThickDisk <br />
DC2/sources/511/511_ThinDisk <br />
DC2/sources/511/511_ThickDiskx10 <br />
DC2/sources/511/511_ThinDiskx10 <br />
DC2/sources/511/511_Testing <br />
DC2/sources/Al26/Al26_R5000_z0200_M30 <br />
DC2/sources/Al26/Al26_R5000_z1000_M60 <br />
DC2/sources/Al26/Al26_R5000_z0200_M30_10xflux <br />
DC2/sources/Al26/Al26_R5000_z1000_M60_10xflux <br />
DC2/sources/Ti44/CasA <br />
DC2/sources/Ti44/CasA_x50 <br />
DC2/sources/Ti44/G1903 <br />
DC2/sources/Ti44/G1903_x10 <br />
DC2/sources/Ti44/SN1987A <br /> 
DC2/sources/Ti44/SN1987A_x50 <br />
DC2/sources/Ti44/SNsurprise <br />
DC2/sources/Ti44/SNsurprise_x50 <br />
DC2/sources/GRBs/GRB080723557 <br />
DC2/sources/GRBs/GRB080725541 <br />
DC2/sources/GRBs/GRB081101491 <br />
DC2/sources/GRBs/GRB081122614 <br />
DC2/sources/GRBs/GRB081223419 <br />
DC2/sources/GRBs/GRB090206620 <br />
DC2/sources/GRBs/GRB090227772 <br />
DC2/sources/GRBs/GRB090228204 <br />
DC2/sources/GRBs/GRB101216721 <br />
DC2/sources/GRBs/GRB130425327 <br />
DC2/sources/GRBs/GRB180128215 <br />
DC2/sources/GRBs/GRB200415A  <br />
DC2/sources/Extragalactic/3C273 <br /> 
DC2/sources/Extragalactic/3C273_10xFlux <br />
DC2/sources/Extragalactic/4C21p35 <br />
DC2/sources/Extragalactic/3C279_low100 <br />
DC2/sources/Extragalactic/3C279_high100 <br />
DC2/sources/Galactic/1E1740_compton-powerlaw <br />
DC2/sources/Galactic/1E1740_two_components <br />
DC2/sources/Galactic/cygX1_soft <br />
DC2/sources/Galactic/cygX1_hard <br />
DC2/sources/Galactic/GRS1758 <br />
DC2/sources/Galactic/cygX3_transition <br />
DC2/sources/Galactic/cygX3_FSXR <br />
DC2/sources/Galactic/Crab <br />
DC2/sources/Galactic/PSRB1509 <br />
DC2/sources/Galactic/PSRJ1846 <br />

## Data Challenge 3 (DC3) <br />
DC3/sources/Galactic/crab_baseline <br />
DC3/backgrounds/GalTotal_SA100_F98 <br />
DC3/sources/511/511_Testing <br />
DC3/sources/511/511_Testing_Extended <br />
DC3/sources/511/LMC_Gaussian_511 <br/>
DC3/sources/511/LMC_Gaussian_511_x100 <br />
DC3/sources/511/M31_Gaussian_511 <br />
DC3/sources/511/M31_Gaussian_511_x100 <br />
DC3/sources/511/Virgo_Gaussian_511 <br />
DC3/sources/511/Virgo_Gaussian_511_x100 <br />
DC3/sources/511/Globular_Cluster_NGC_6121 <br />
DC3/sources/511/Globular_Cluster_NGC_6397 <br />
DC3/sources/511/Globular_Cluster_Omega_Cen <br />
DC3/sources/511/Globular_Cluster_Tuc_47 <br />

## Galactic Diffuse (Galdiff) <br />
Galdiff/GalIC <br />
Galdiff/GalBrem <br />
Galdiff/GalTotal_SA100_F98 <br />
Galdiff/GalTS_Baseline <br />
Galdiff/GalTS_BestMatch <br />

## Using your own sources:
To use your own sources specifiy 'other' in the input yaml source list.  <br />
The source files must still be copied to the source directory of the run, and all corresponding paths need to be correct. <br />
When running define_sim (in run_sims.py) you need to pass 'external_src=True'.
