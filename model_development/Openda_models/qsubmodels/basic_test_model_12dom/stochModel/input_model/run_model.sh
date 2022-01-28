#!/bin/bash
# To start Dimr, execute this script

# stop after an error occured:
set -e
 
# Set numbers of hosts and cores per host
nNodes=2
nProc=4

# set DIMR version to be used
dimrdir=/p/d-hydro/dimrset/weekly/2.16.05.71137

# select queue; one of : normal-e3-c7 , normal-e5-c7
queue=normal-e3-c7

nPart=$((nNodes * nProc))

# DIMR input-file; must already exist!
dimrFile=dimr.xml
mduFile=canada_model.mdu

# Replace number of processes in DIMR file
PROCESSSTR="$(seq -s " " 0 $((nPart-1)))"
sed -i "s/\(<process.*>\)[^<>]*\(<\/process.*\)/\1$PROCESSSTR\2/" $dimrFile

# Replace MDU file in DIMR-file
sed -i "s/\(<inputFile.*>\)[^<>]*\(<\/inputFile.*\)/\1$mduFile\2/" $dimrFile


# jobName: $FOLDERNAME
export jobName="${PWD##*/}"


# if [ "$nPart" == "1" ]; then
#     $dimrdir/lnx64/bin/submit_dimr.sh -m $dimrFile -j $jobName -q $queue
# else
#     $dimrdir/lnx64/bin/run_dflowfm.sh        --partition:ndomains=$nPart:icgsolver=6 $mduFile
#     # $dimrdir/lnx64/bin/submit_dimr.sh -c $nProc -n $nNodes -m $dimrFile -q $queue -j $jobName
# fi

$dimrdir/lnx64/bin/run_dimr.sh --NNODES $nNodes -c $nProc -m $dimrFile --D3D_HOME $dimrdir/lnx64/bin/..

while [! -f sim.done];do
	sleep 10
done
echo "test has finished"
