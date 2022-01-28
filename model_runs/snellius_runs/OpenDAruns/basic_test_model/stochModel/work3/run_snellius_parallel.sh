# New script written to run canada_model on snellius
# Author: ANV: 19/01/2011.
# This is an initial script which runs a .sif singularity version on dflowfm
# it works on only 1 node and there will be an update soon. 
# ===========================================================================
# model to run:
set -e
nNodes=1
nProc=32 # tasks per node # one node has 128 cores and 32 is 1/4 of a node which can be considered a shared node
# now 32 is the most optimal for our model. See snelliustest folder in einf220/AV/canadamodel/thirdmodelfiles/ o
mdufile=canada_model.mdu
# name used for slurm:
name="${PWD##*/}_${nNodes}x${nProc}"
nPart=$((nNodes * nProc))
maxwalltime="01:00:00" # less wal time helps in getting the model higher priority on snellius.
# purpose of run
purpose="canadamodel_runs"
echo "========================================================================="
echo "Submitting Dflow-FM run $name in  $PWD"
echo "Purpose: $purpose"
echo "Starting on $nPart domains, $nNodes nodes"
echo "Wall-clock-limit set to $maxwalltime"

#
#Find out where this script is
basedir=$PWD

# Create this empty file when run is done
export donefile="$basedir/$name.done" 

# Delete existing output and error files
rm -f $basedir/$name.out
rm -f $basedir/$name.err
rm -f $basedir/sim.done

#mergelist file
mergefile=listmapfilessnellius.txt

# Create sbatch script and submit job
echo "#! /bin/bash" >sbatch_$name.sh
echo "#SBATCH --nodes ${nNodes}" >>sbatch_$name.sh
echo "#SBATCH --ntasks-per-node=${nProc}" >>sbatch_$name.sh
echo "#SBATCH --job-name=$name" >>sbatch_$name.sh
echo "#SBATCH --time $maxwalltime" >>sbatch_$name.sh
echo "#SBATCH --chdir=./" >>sbatch_$name.sh   #chdir set as /path/to/runfolder is useful when calling this script from a different directory
echo "#SBATCH --partition=thin" >>sbatch_$name.sh #type of node.
#see sbatch --help for additional parameters
#overview of node types (partition): https://servicedesk.surfsara.nl/wiki/display/WIKI/Snellius+usage+and+accounting
#partition=thin: Single node jobs run on a shared node by default. Add --exclusive if you want to use a node exclusively.
#partition=thin: You will be charged for 0.25 node. You could request 32 CPU cores without increasing the price. Use --ntasks, --cpus-per-task and/or --mincpus.
#partition=thin: Note that by default you will get 1875 MiB of memory per CPU core, unless explicitly overridden by --mem-per-cpu, --mem-per-gpu or --mem.
# stop after an error occured
echo "set -e"
echo "cd $basedir" >>sbatch_$name.sh
#singularity versions from p:\d-hydro\delft3dfm_containers\delft3dfm_2022.01
# echo "runscript=/projects/0/einf220/AV/dflowfm_myversion/run_dflowfm_singularity_AV.sh" >>sbatch_$name.sh
# echo "dfmoutputscript=/projects/0/einf220/AV/dflowfm_myversion/run_dfmoutput_singularity.sh" >>sbatch_$name.sh
runscript=/projects/0/einf220/AV/dflowfm_myversion/run_dflowfm_singularity_AV.sh
dfmoutputscript=/projects/0/einf220/AV/dflowfm_myversion/run_dfmoutput_singularity.sh
echo "# load modules" >>sbatch_$name.sh
echo "module load 2021" >>sbatch_$name.sh
echo "module load intel/2021a" >>sbatch_$name.sh

echo "srun --nodes $nNodes --ntasks $nPart $runscript  --autostartstop $mdufile" >>sbatch_$name.sh 
echo "touch $basedir/sim.done" >>sbatch_$name.sh
echo "while [! -f sim.done];do">>sbatch_$name.sh
echo "sleep 1">>sbatch_$name.sh
echo "done">>sbatch_$name.sh
echo "Merging map files." >>sbatch_$name.sh
#echo "sh ./run_mapmerge_cartesius.sh" >>sbatch_$name.sh
echo "$dfmoutputscript mapmerge --listfile $mergefile">>sbatch_$name.sh
echo "touch $basedir/merge.done">>sbatch_$name.sh
chmod +x sbatch_$name.sh
export result=`sbatch ./sbatch_$name.sh `
echo "sbatch --> $result"
echo $?
squeue -u $USER
echo "Submitting done."
echo "========================================================================="
