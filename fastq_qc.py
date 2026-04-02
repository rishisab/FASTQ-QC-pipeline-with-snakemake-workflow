import sys

#Input
file=sys.argv[1]

total_reads=0
total_base=0
gc_count=0

with open(file)as f:
        line=f.readlines()

for i in range(0,len(line),4):
        seq=line[i+1].strip().upper()
        total_reads +=1
        total_base +=len(seq)
        gc_count+= seq.count("G")+ seq.count("C")

avg_length= total_base/total_reads
gc_percent=(gc_count/total_base)*100


with open("fastq_qc.txt","w") as out:
        out.write(f"Total reads: {total_reads}\n")
        out.write(f"Total base count : {total_base}\n")
        out.write(f"Average length : {avg_length}\n")
        out.write(f"GC percent: {gc_percent:.2f}\n")
print("qc report generated")
