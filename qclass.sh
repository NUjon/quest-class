#!/bin/bash
#MSUB -A b1042
#MSUB -q genomics
#MSUB -l walltime=04:00:00
#MSUB -m a
#MSUB -j oe
#MSUB -l nodes=1:ppn=1
module load python

python quality_threshold.py exome.fastq 30
python long_reads.py exome.fasta 70
python ave_seq_len.py exome.trimmed.fasta


