This DC features the magnetar (AXP) 1RXS J170849.0-400901. The resons to focus on this magnetar are:
* it is quite bright
* it has a spectrum (nuFnu) rising above 10 keV well constrained by INTEGRAL-IBIS
* it showed an extreme polarization in soft X-rays with strong energy dependence (Zane et al 2024)

The models used are based on _Hartog, Kuiper and Hermsen 2008_ (https://drive.google.com/drive/u/0/home)

The Challenges:
---------------
* Can COSI detect the magnetar? (i.e. detect he pulsations?)
* Can COSI detect the turn over in the spectrum?
* Can COSI detect polarization?

The Spectrum:
-------------
The spectrum is a log parabola in the MeV energy range:

    def log_parabola(x, norm, alpha, beta, pivot):
        var = x/pivot
        spec = norm * var**(-alpha-beta*np.log(var))
        return spec

The assumed parameters are:
* alpha = 1.637
* beta = 0.261  
* norm = 1.68e-6 ph/cm2/s/keV 
* pivot = 143.276 keV

The Polarization:
-----------------
For this challenge the polarization is assumed energy independent int the COSI band with a phase-integrated polarization degree of 80% (PA=-60 deg).

The Lightcurve:
---------------
The file _1RXSJ170849_magnetar_lightcurve.dat_ contains the periodic lightcurve of the magnetar:
* Period: P = 11.00502461 s
* Period derivative: Pdot = 1.95E-11 s/s
* Pulsed Fraction: PF = 0.5 

The Pulsed fraction is defined as (Fmax - Fmin)/(Fmax + Fmin), with F being the flux.
