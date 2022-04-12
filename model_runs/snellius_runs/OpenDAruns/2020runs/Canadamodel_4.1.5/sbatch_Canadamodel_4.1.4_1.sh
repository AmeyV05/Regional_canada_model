#! /bin/sh
#SBATCH --nodes 1
#SBATCH --ntasks-per-node=32
#SBATCH --job-name=Canadamodel_4.1.4_1
#SBATCH --time 1-00:00:00
#SBATCH --chdir=./
#SBATCH --partition=thin
cd /home/vasulkar/einf220/AV/canada_model/OpenDAruns/2020runs/Canadamodel_4.1.4
# load modules
module load 2021
module load intel/2021a
module load Java/11.0.2 
cd /home/vasulkar/einf220/AV/canada_model/OpenDAruns/2020runs/Canadamodel_4.1.4
export OPENDADIR=/home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin
. /home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin/setup_openda.sh
. /home/vasulkar/einf220/AV/OpenDA/openda_3.0.2/bin/settings_local.sh linux
cat $PE_HOSTFILE | cut -d' ' -f1 > hosts
head -1 hosts>output1
tail -n +1 hosts>./stochModel/host
sh oda_run.sh Dud.oda
touch /home/vasulkar/einf220/AV/canada_model/OpenDAruns/2020runs/Canadamodel_4.1.4/Canadamodel_4.1.4_1.done
