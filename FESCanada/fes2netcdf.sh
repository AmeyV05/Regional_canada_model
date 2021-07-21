#! /bin/sh
#
# Generate tidal timeseries at locations in an .xyn file from the FES2012
# tidal constituents
#
export xynfile=$1
#Time range from to
export tstart=$2
 # format YYYYMMDD also allowed is YYYYMMDDhhmm
export tstop=$3
export dt=10 #in minutes


/p/1230882-emodnet_hrsm/FES2014/fes2014_linux64_gnu/bin/fes2netcdf.sh $xynfile $tstart $tstop $dt


#$PWD/fes2012_linux64_gnu/bin/ncdump  test_fes2012.nc
