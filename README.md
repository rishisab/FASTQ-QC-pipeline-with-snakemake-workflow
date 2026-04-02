# FASTQ-QC-pipeline-with-snakemake-workflow
This project implements a bioinformatics workflow using Snakemake.

### Input
- FASTQ file (sweuence.fastq)

### Steps
1. Quality Control (read count, length, GC%)
2. GC Distribution Plot

### Run Pipeline
snakemake --cores 1

### Output
- qc_report.txt
- fastq_gc_plot.png
