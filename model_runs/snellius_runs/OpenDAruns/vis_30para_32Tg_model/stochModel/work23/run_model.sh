#!/bin/bash
# New script written to run canada_model on snellius without batch script. 
# Author: ANV: 19/01/2011.
# This is an initial script which runs a .sif singularity version on dflowfm
# it works on only 1 node and there will be an update soon. 
# ===========================================================================
# model to run:
set -e
nNodes=1
nProc=32 # tasks per node 
mdufile=canada_model.mdu
maxwalltime="01:00:00"
nPart=$((nNodes * nProc))




runscript=/projects/0/einf220/AV/dflowfm_myversion/run_dflowfm_singularity_AV.sh

srun --nodes $nNodes --ntasks $nPart $runscript  --autostartstop $mdufile
echo "run_finished">sim.done
while [! -f sim.done];do
sleep 1
done
echo "test has finished"

