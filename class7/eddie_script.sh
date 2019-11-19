#!/bin/bash
#$ -cwd
#$ -t 000-099
#$ -N FXB_BPSM_week7

./analysis.sh split_files/reads_$SGE_TASK_ID

#$ -o FXB_week7.o
#$ -e FXB_week7.e
