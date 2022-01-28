# Script to give snellius to run openda. 
# Purpose : startup script for openda calibration with dflowfm model.
# Args    : none
# Comments: this script must be started in the same direcory as the input files.
# Date    : 19 Jan 2021
# Author  : Amey
# ===========================================================================
# model to run:
set -e
nNodes=1
nProc=32 # tasks per node # one node has 128 cores and 32 is 1/4 of a node which can be considered a shared node
export odafile=Dud.oda
# name used for slurm:
name="${PWD##*/}_${nNodes}"
nPart=$((nNodes * nProc))
maxwalltime="05:00:00"  # more wall time because now you run canada model n number of times. 
# purpose of run
echo "========================================================================="
echo "Submitting OpenDA calibration of Dflow-FM run $name in  $PWD"

# Find out where this script is
basedir=$PWD

#create this empty file when run is done
export donefile="$basedir/$name.done"

# Delete existing output and error files
rm -f $donefile
rm -f $basedir/$name.out
rm -f $basedir/$name.err
rm -f $basedir/sim.done

#Start snellius slurm


# save environment for debugging
OPENDADIR=/home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin
# Create sbatch script and submit job
echo "#! /bin/sh" >sbatch_$name.sh
echo "#SBATCH --nodes ${nNodes}" >>sbatch_$name.sh
echo "#SBATCH --ntasks-per-node=${nProc}" >>sbatch_$name.sh
echo "#SBATCH --job-name=$name" >>sbatch_$name.sh
echo "#SBATCH --time $maxwalltime" >>sbatch_$name.sh
echo "#SBATCH --chdir=./" >>sbatch_$name.sh   #chdir set as /path/to/runfolder is useful when calling this script from a different directory
echo "#SBATCH --partition=thin" >>sbatch_$name.sh #type of node.
echo "set -e"
echo "cd $basedir" >>sbatch_$name.sh
echo "# load modules" >>sbatch_$name.sh
echo "module load 2021" >>sbatch_$name.sh
echo "module load intel/2021a" >>sbatch_$name.sh
echo "module load Java/11.0.2 ">>sbatch_$name.sh
echo "cd $basedir" >>sbatch_$name.sh
echo "export OPENDADIR=/home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin" >>sbatch_$name.sh
echo ". $OPENDADIR/setup_openda.sh" >>sbatch_$name.sh
echo ". $OPENDADIR/settings_local.sh linux" >>sbatch_$name.sh
echo "cat \$PE_HOSTFILE | cut -d' ' -f1 > hosts" >>sbatch_$name.sh
echo "head -1 hosts>output1">>sbatch_$name.sh
echo "tail -n +1 hosts>./stochModel/host">>sbatch_$name.sh
echo "sh oda_run.sh $odafile" >>sbatch_$name.sh
echo "touch $donefile" >>sbatch_$name.sh
chmod +x sbatch_$name.sh
export result=`sbatch ./sbatch_$name.sh `
echo "sbatch --> $result"
echo $?
squeue -u $USER
echo "Submitting done."
echo "========================================================================="

