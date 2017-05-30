import sys

f = open(sys.argv[1], "r")
output = open(sys.argv[2], "w")
alns = f.readlines()
for aln in alns:
    if aln[0] == "@":
        continue;
    tmp = aln.split()
    if tmp[0] != tmp[2]:
        output.write(aln)
f.close()
output.close()
