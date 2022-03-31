#! /bin/sh
#run mode with dflowfm
echo "TEST RUN_MODEL_BATCH FILE"
export ndom=8
export nnode=2
export ncore=4
#export version= "1.2.103.66440"
#/opt/dflowfm/scripts/runscript_dflow_oda.sh -n $nnode -m ${model} -v 1.2.103.66440
chmod +x run_model.sh
./run_model.sh     #-n $nnode -m ${model} -v 1.2.103.66440
# echo "run_finished">finish.out
while [! -f sim.done];do
	sleep 10
done
echo "test has finished"
#sh ./clean.sh