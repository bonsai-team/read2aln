import sys

f = open(sys.argv[1], "r")
alns = f.readlines()
output = open(sys.argv[2], "w")
for aln in alns:
    tmp = aln.split()
    if float(tmp[13].split(":")[-1]) < 10**(-10) and len(tmp[9]) > 65:
        output.write(aln)
f.close()
output.close()
