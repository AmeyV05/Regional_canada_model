#! /bin/sh
# usage: qsub ./trial2param.sh
module load java/jdk_11.0.7
cd /u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/basic_test_model_12dom
export OPENDADIR=/u/vasulkar/p_emodnet_amey/OpenDA/openda_3.0.2/bin
. /u/vasulkar/p_emodnet_amey/OpenDA/openda_3.0.2/bin/setup_openda.sh
cat $PE_HOSTFILE | cut -d' ' -f1 > hosts
head -1 hosts>output1
tail -n +1 hosts>./stochModel/host
sh oda_run.sh Dud.oda
touch /u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/basic_test_model_12dom/trial2param.done
