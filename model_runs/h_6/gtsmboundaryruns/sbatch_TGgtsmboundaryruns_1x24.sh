#! /bin/bash
#SBATCH -N 1
#SBATCH --ntasks-per-node=24
#SBATCH --job-name=TGgtsmboundaryruns_1x24
#SBATCH -t 05:00:00
#SBATCH --constraint=haswell
cd /home/vasulkar/einf220/AV/canada_model/third_boundary_test_runs/TGgtsmboundaryruns
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
dflowfm --partition:ndomains=24:icgsolver=6 canada_model.mdu
srun -N 1 -n 24 dflowfm  --autostartstop canada_model.mdu
touch /home/vasulkar/einf220/AV/canada_model/third_boundary_test_runs/TGgtsmboundaryruns/sim.done
Merging map files.
dfmoutput mapmerge --listfile listmapfilescartesius.txt
touch /home/vasulkar/einf220/AV/canada_model/third_boundary_test_runs/TGgtsmboundaryruns/merge.done
