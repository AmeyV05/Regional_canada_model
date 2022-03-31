#! /bin/sh
#SBATCH --nodes 1
#SBATCH --ntasks-per-node=32
#SBATCH --job-name=Canadamodel_bf_sensitivity_1
#SBATCH --time 1-12:00:00
#SBATCH --chdir=./
#SBATCH --partition=thin
cd /home/vasulkar/einf220/AV/canada_model/OpenDAruns/Canadamodel_bf_sensitivity
# load modules
module load 2021
module load 2021_Delft3D
module load intel/2021a
module load Java/11.0.2 
cd /home/vasulkar/einf220/AV/canada_model/OpenDAruns/Canadamodel_bf_sensitivity
export OPENDADIR=/home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin
. /home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin/setup_openda.sh
. /home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin/settings_local.sh linux
cat $PE_HOSTFILE | cut -d' ' -f1 > hosts
head -1 hosts>output1
tail -n +1 hosts>./stochModel/host
sh oda_run.sh Dud.oda
touch /home/vasulkar/einf220/AV/canada_model/OpenDAruns/Canadamodel_bf_sensitivity/Canadamodel_bf_sensitivity_1.done
