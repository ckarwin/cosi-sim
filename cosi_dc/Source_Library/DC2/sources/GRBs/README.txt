Included are:
3 long GRBs with realistic lightcurves - GRB080723557.source, GRB090206620.source, GRB130425327.source
3 short GRBs with realistic lightcurves - GRB090227772.source, GRB090228204.source, GRB101216721.source
4 short GRBs with constant lightcurves - GRB080725541.source, GRB081101491.source, GRB081122614.source, GRB081223419.source
2 magnetar giant flares (MGFs) - GRB180128215.source, GRB200415A.source

Spectra are either Band function or Comptonized spectrum fits from GBM.
Long GRB lightcurves are downloaded directly from GBM.
Short GRB realistic lightcurves are downloaded from GBM & binned using Bayesian blocks.
Short GRB constant lightcurves are constant over the duration of the GRB.
Magnetar giant flare lightcurves are downloaded from GBM & binned using Bayesian blocks.

GRBs occur randomly in time throughout the duration of the orientation file (20280301_3_month_edited.ori), and 1835487300.0 s needs to be added to the .sim files to match the Data Challenge 2 orientation file. 
GRB positions were chosen to have incidence angles between 0 and 30 degrees with a range of azimuthal angles.

Goals:
Determine time of each event and create lightcurve
Determine source locations
Fit spectra
Identify event type (GRB vs MGF)