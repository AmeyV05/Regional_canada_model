#! /bin/sh
#
# Generate tidal timeseries at locations in an .xyn file from the FES2012
# tidal constituents
#
export xynfile='GridPointsArctic.xyn'

#Time range from to
export tstart='20140301' # format YYYYMMDD also allowed is YYYYMMDDhhmm
export tstop='20140401'
export dt=60 #in minutes


/p/1230882-emodnet_hrsm/FES2014/fes2014_linux64_gnu/bin/fes2netcdf.sh $xynfile $tstart $tstop $dt


#$PWD/fes2012_linux64_gnu/bin/ncdump  test_fes2012.nc
