This is the same as in DC2
The 6 different spectral models for Cyg X3 are best fit eqpair  models of time averaged INTEGRAL data 
(Cangemi et al 2021, https://www.aanda.org/articles/aa/pdf/2021/01/aa37951-20.pdf).
We would like to assume a succession of the different states :

            % of time of observed state    ->    time in days (for a 2 year mission)
Quiescent:  6.                                    47
Transition  46.                                   335
FHXR:       10.                                   73
FIM:        22.                                   161
FSXR:       54.                                   28
Hypersoft:  12.                                   86

In this order and for the specified approximate durations. 

If DC3 simulates less than 2 years of observation then reduce the time spent in each states accordingly and 
increase the fluxes as to obtain the same total number of photons as we would in 2 yrs of observations. 

This is to check  if COSI could achieve a decent measurement of the average spectrum over its life time 
and if so, check if we can detect the spectral changes on shorter time scales. 


CK Note: 
Total time above: 730 days.
Total time in DC3 ori file: 92.38 days.
This implies: flux_2 = (730/92.38)flux_1 = 7.9.
Therefore, I scale up the flux of each component by a factor of 7.9
in order to account for the reduced exposure. 
NB: You must also scale up the BG in the same way when performing the analysis!

Also note that I was not able to run all source components with a single run. This is was not working for me 
in MEGAlib. I believe it might be related to the fact that all the components have different light curves, although
I haven't looked into it in detail. Instead, I ran each component separately, and then combined them in the end. It works, 
although it takes much longer to process and run everything!
