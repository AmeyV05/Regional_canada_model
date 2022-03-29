#! /bin/bash

resfile=listfoufilescartesius.txt

basedir=$PWD

rm -f $basedir/merge.done

module load purge
module load 2019
module load surfsara
module load intel/2018b
module load netCDF/4.6.1-intel-2018b netCDF-Fortran/4.4.4-intel-2018b
module load PETSc/3.11.2-intel-2018b
module load METIS/5.1.0-intel-2018b ParMETIS/4.0.3-intel-2018b
export OSS=/projects/0/einf220/GTSM_software/dflowfm_66542
export PATH=$OSS/src/bin:$PATH
dfmoutput mapmerge --listfile $resfile
touch $basedir/merge.done
