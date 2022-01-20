me    : run_calibration_qsub_h6.sh
# Purpose : startup script for openda calibration of dflowfm through scheduler with qsub
# Args    : none
# Comments: this script must be started in the same direcory as the input files.
# Date    : Mar 2019
# Author  : Xiaohui
# ===========================================================================
# model to run:
# export odafile=Dud.oda
export odafile=Dud.oda
# name used for qsub:
export name="ex53"
# purpose of run
echo "========================================================================="
echo "Submitting OpenDA calibration of Dflow-FM run $name in  $PWD"

# find out where this script is
#basedir=`(cd \`dirname $0\`; pwd)`
basedir=$PWD

#create this empty file when run is done
export donefile="$basedir/$name.done"

#Delete old files
rm -f $donefile

#Start qsub 

# save environment for debugging
#env >env.txt

echo "#! /bin/sh" >qsub_$name.sh
echo "# usage: qsub ./$qsub_$name.sh" >>qsub_$name.sh
echo "module load java/jdk_1.8_oracle" >>qsub_$name.sh
echo "module load dflowfm">>qsub_$name.sh
echo "cd $basedir" >>qsub_$name.sh
#echo "export OPENDADIR=$basedir/../../openda_linux64_binaries/bin" >>qsub_$name.sh
echo "export OPENDADIR=$basedir/../software/OpenDA-master/bin" >>qsub_$name.sh
echo ". \$OPENDADIR/settings_local.sh linux" >>qsub_$name.sh
echo "cat \$PE_HOSTFILE | cut -d' ' -f1 > hosts" >>qsub_$name.sh
echo "head -1 hosts>output1">>qsub_$name.sh
echo "tail -n +1 hosts>./stochModel/host">>qsub_$name.sh
#echo "cat $PE_HOSTFILE">>qsub_$name.sh
echo "sh oda_run.sh $odafile" >>qsub_$name.sh
echo "touch $donefile" >>qsub_$name.sh
chmod +x qsub_$name.sh
export result=`qsub -N $name -q normal-e3 -pe distrib 5 -cwd ./qsub_$name.sh `
echo "qsub --> $result"
echo $?
qstat -u $USER
#echo "cat $PE_HOSTFILE | cut -d' ' -f1 > hostfile$$">host.txt
echo "Submitting done."
echo "========================================================================="

