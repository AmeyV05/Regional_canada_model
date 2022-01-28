#! /bin/bash
#SBATCH --nodes 1
#SBATCH --ntasks-per-node=32
#SBATCH --job-name=test_input_moel_1x32
#SBATCH --time 01:00:00
#SBATCH --chdir=./
#SBATCH --partition=thin
cd /home/vasulkar/einf220/AV/canada_model/OpenDAruns/testmodel/test_input_moel
# load modules
module load 2021
module load intel/2021a
# Partition model
/projects/0/einf220/AV/dflowfm_myversion/run_dflowfm_singularity_AV.sh --ntasks 1  --partition:ndomains=32:icgsolver=6 canada_model.mdu
touch /home/vasulkar/einf220/AV/canada_model/OpenDAruns/testmodel/test_input_moel/sim.done
