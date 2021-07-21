#!/bin/bash
#SBATCH -J pyscript_gtsm
#SBATCH -n 1
#SBATCH -t 5-00:00:000

module purge
module load 2019
module load surfsara
module load intel/2018b
module load netCDF/4.6.1-intel-2018b netCDF-Fortran/4.4.4-intel-2018b
module load PETSc/3.11.2-intel-2018b
module load METIS/5.1.0-intel-2018b ParMETIS/4.0.3-intel-2018b
# Export path
./run_partition_cartesius_parallel.sh

echo "Partitioning done"

./run_cartesius_parallel.sh

echo "Sim done."