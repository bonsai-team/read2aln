import sys

#arguments pertinents a priori : taille : 65, evalue : 10e-10
#python parse_evalue.py aln_tmp.sam reads.sam evalue taille

f = open(sys.argv[1], "r")
alns = f.readlines()
output = open(sys.argv[2], "w")
for aln in alns:
    tmp = aln.split()
    if float(tmp[13].split(":")[-1]) < float(sys.argv[3]) and int(tmp[12].split(":")[2]) > int(sys.argv[4]):
        output.write(aln)
f.close()
output.close()
