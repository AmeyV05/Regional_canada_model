#!/bin/bash
# To start Dimr, execute this script

# stop after an error occured:
set -e
 
# Set numbers of hosts and cores per host
nNodes=1
nProc=32
fmversion=2.14.07.69056
# set DIMR version to be used
dimrdir=/p/d-hydro/dimrset/weekly/$fmversion

# select queue; one of : normal-e3-c7 , normal-e5-c7, test-c7
queue=normal-e3-c7

nPart=$((nNodes * nProc))

# DIMR input-file; must already exist!
dimrFile=dimr.xml
mduFile=canada_model.mdu

# Replace number of processes in DIMR file
PROCESSSTR="$(seq -s " " 0 $((nPart-1)))"
sed -i "s/\(<process.*>\)[^<>]*\(<\/process.*\)/\1$PROCESSSTR\2/" $dimrFile

# Read MDU file from DIMR-file
#mduFile="$(sed -n 's/\r//; s/<inputFile>\(.*\).mdu<\/inputFile>/\1/p' $dimrFile)".mdu
# Replace MDU file in DIMR-file
sed -i "s/\(<inputFile.*>\)[^<>]*\(<\/inputFile.*\)/\1$mduFile\2/" $dimrFile

# jobName: $FOLDERNAME
#export jobName="${PWD##*/}"
export jobName="${PWD##*/}_${nNodes}x${nProc}"


# if [ "$nPart" == "1" ]; then
#     $dimrdir/lnx64/bin/submit_dimr.sh -m $dimrFile -j $jobName -q $queue
# else
#     $dimrdir/lnx64/bin/run_dflowfm.sh --partition:ndomains=$nPart:icgsolver=6 $mduFile
#     #$dimrdir/lnx64/bin/submit_dimr.sh -c $nProc -n $nNodes -m $dimrFile -q $queue -j $jobName
#     #qsub -pe distrib $nNodes -q $queue -N $jobName $dimrdir/lnx64/bin/run_dimr.sh --NNODES $nNodes -c $nProc -m $dimrFile --D3D_HOME $dimrdir/lnx64/bin/..
# fi


# $dimrdir/lnx64/bin/run_dimr.sh --NNODES $nNodes -c 1 -m $dimrFile --partition:ndomains=$nPart:icgsolver=6 $mduFile 
$dimrdir/lnx64/bin/run_dflowfm.sh --partition:ndomains=$nPart:icgsolver=6 $mduFile