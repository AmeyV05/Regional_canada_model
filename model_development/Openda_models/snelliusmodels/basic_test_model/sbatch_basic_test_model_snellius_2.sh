#! /bin/sh
#SBATCH --nodes 2
#SBATCH --ntasks-per-node=32
#SBATCH --job-name=basic_test_model_snellius_2
#SBATCH --time 05:00:00
#SBATCH --chdir=./
#SBATCH --partition=thin
cd /u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/basic_test_model_snellius
# load modules
module load 2021
module load intel/2021a
module load Java/11.0.2 
cd /u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/basic_test_model_snellius
export OPENDADIR=/home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin
. /home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin/setup_openda.sh
. /home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin/settings_local.sh linux
cat $PE_HOSTFILE | cut -d' ' -f1 > hosts
head -1 hosts>output1
tail -n +1 hosts>./stochModel/host
sh oda_run.sh Dud.oda
touch /u/vasulkar/p_emodnet_amey/Regional_canada_model/model_development/Openda_models/basic_test_model_snellius/basic_test_model_snellius_2.done
