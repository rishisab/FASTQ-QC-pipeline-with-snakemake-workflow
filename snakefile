rule gc:
	input:
		"sequence.fastq"
	output:
		"fastq_qc.txt"
	shell:
		"python fastq_qc.py"
	



rule gc_fasta:
	input:
		"sequence.fastq"
	output:
		"fastq_qc_plot.png"
	shell:
		"python fastq_qc_plot.py"
