#! /bin/bash
#usage: sbatch ./sbatch_oss68758_1x24.sh
#SBATCH -N 1
#SBATCH --ntasks-per-node=24
#SBATCH --job-name=gtsm_runname
#SBATCH -t 1-00:00:00           #reduce the expected time if possible to increase your priority
#SBATCH --constraint=haswell    #haswell constraint is recommended to get one type of node per job, mixing ivy and haswell can cause issues
#SBATCH --chdir=./              #chdir set as /path/to/runfolder is useful when calling this script from a different directory
# load modules
module purge
module load 2019
module load surfsara
module load intel/2018b
module load netCDF/4.6.1-intel-2018b netCDF-Fortran/4.4.4-intel-2018b
module load PETSc/3.11.2-intel-2018b
module load METIS/5.1.0-intel-2018b ParMETIS/4.0.3-intel-2018b
# Export path
export OSS=/projects/0/einf220/dflowfm_68758
export PATH=$OSS/bin:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$OSS/lib
# Partition model
dflowfm --partition:ndomains=240:icgsolver=6 gtsm_model.mdu
srun -N 10 -n 24 dflowfm --autostartstop gtsm_model.mdu
#touch gtsm_runname.done
