import sys, os
from Bio import SeqIO

f = open("tmp_wo_fail.fa", "w")
for rec in SeqIO.parse(sys.argv[1], "fasta"):
    if "fail" not in rec.name:
        f.write(rec.format("fasta"))
os.system("mv tmp_wo_fail.fa " + sys.argv[1])
