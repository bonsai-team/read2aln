import sys, os
from Bio import SeqIO

d = open("tmp_dustmasker", "r")
dustmasker = d.readlines()
tmp = []
for mask in dustmasker:
    if mask not in tmp:
        tmp.append(mask.split()[0][1:])
f = open("tmp_wo_fail.fa", "w")
for rec in SeqIO.parse(sys.argv[1], "fasta"):
    if "fail" not in rec.name and len(rec.seq) > int(sys.argv[2]) and rec.name not in tmp:
        f.write(rec.format("fasta"))
f.close()
os.system("mv tmp_wo_fail.fa " + sys.argv[1])
