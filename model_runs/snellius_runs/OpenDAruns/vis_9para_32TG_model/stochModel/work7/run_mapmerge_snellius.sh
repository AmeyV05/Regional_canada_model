#! /bin/bash

mergefile=listmapfilessnellius.txt

basedir=$PWD

rm -f $basedir/merge.done

module load 2021
module load intel/2021a
dfmoutputscript=/projects/0/einf220/AV/dflowfm_myversion/run_dfmoutput_singularity.sh
$dfmoutputscript mapmerge --listfile $mergefile
touch $basedir/merge.done