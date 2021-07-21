# New script written to run GTSM4_12.5eu type model on cartesius.
# Author: ANV: 7/04/2021.
# ===========================================================================
# model to run:
set -e
nNodes=10
nProc=24 # tasks per node
mdufile=gtsm_model.mdu
#dfmversion=%FMVERSION%
#queue=%QUEUE%
# name used for slurm:
name="${PWD##*/}_${nNodes}x${nProc}"
nPart=$((nNodes * nProc))
maxwalltime="05:00:00"
# purpose of run
purpose="trial_run"
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

# Create sbatch script and submit job
echo "#! /bin/bash" >sbatch_$name.sh
echo "#SBATCH -N ${nNodes}" >>sbatch_$name.sh
echo "#SBATCH --ntasks-per-node=${nProc}" >>sbatch_$name.sh
echo "#SBATCH --job-name=$name" >>sbatch_$name.sh
echo "#SBATCH -t $maxwalltime" >>sbatch_$name.sh
echo "#SBATCH --constraint=haswell" >>sbatch_$name.sh
echo "set -e"
echo "cd $basedir" >>sbatch_$name.sh
echo "# load modules" >>sbatch_$name.sh
echo "module purge" >>sbatch_$name.sh
echo "module load 2019" >>sbatch_$name.sh
echo "module load surfsara" >>sbatch_$name.sh
echo "module load intel/2018b" >>sbatch_$name.sh
echo "module load netCDF/4.6.1-intel-2018b netCDF-Fortran/4.4.4-intel-2018b" >>sbatch_$name.sh
echo "module load PETSc/3.11.2-intel-2018b" >>sbatch_$name.sh
echo "module load METIS/5.1.0-intel-2018b ParMETIS/4.0.3-intel-2018b" >>sbatch_$name.sh
#echo "module load DFlowFM/2021.03-67911-intel-2018b" >>sbatch_$name.sh
echo "# Export path" >>sbatch_$name.sh
echo 'export OSS=/projects/0/einf220/dflowfm_68758' >>sbatch_$name.sh
echo 'export PATH=$OSS/bin:$PATH'>>sbatch_$name.sh
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$OSS/lib'>>sbatch_$name.sh
#echo "# Partition model" >>sbatch_$name.sh
#echo "dflowfm --partition:ndomains=$nPart:icgsolver=6 $mdufile" >>sbatch_$name.sh  
echo "srun -N $nNodes -n $nPart dflowfm  --autostartstop $mdufile" >>sbatch_$name.sh 
echo "touch $basedir/sim.done" >>sbatch_$name.sh
chmod +x sbatch_$name.sh
export result=`sbatch ./sbatch_$name.sh `
echo "sbatch --> $result"
echo $?
squeue -u $USER
echo "Submitting done."
echo "========================================================================="
