import sys
import matplotlib.pyplot as plt

file=sys.argv[1]

gc_value=[]

with open(file)as f:
        line=f.readlines()

for i in range(0,len(line),4):
        seq=line[i+1].strip().upper()
        gc=(seq.count("G") +seq.count("C"))/len(seq) *100
        gc_value.append(gc)

plt.hist(gc_value)
plt.xlabel("GC%")
plt.ylabel("Frequency")
plt.title("GC percent distribution")
plt.savefig("fastq_gc_plot.png")
print("fastq file generated")
