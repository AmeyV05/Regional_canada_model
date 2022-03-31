#!/bin/bash

basedir=$PWD
mapfile=listmapfiles.txt
# set DIMR version to be used
dimrdir=/p/d-hydro/dimrset/weekly/2.16.05.71137

$dimrdir/lnx64/bin/run_dfmoutput.sh -- mapmerge --listfile $mapfile

touch $basedir/merge.done