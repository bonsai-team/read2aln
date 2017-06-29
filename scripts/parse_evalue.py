import sys, re

#arguments pertinents a priori : taille : 65, evalue : 10e-10
#python parse_evalue.py aln_tmp.sam reads.sam evalue taille

f = open(sys.argv[1], "r")
alns = f.readlines()
output = open(sys.argv[2], "w")
for aln in alns:
    tmp = aln.split()
    cig = re.split('(\d+)', tmp[5])
    taille_id = 0
    for i in range(0, len(cig)):
        if cig[i] == "=":
            taille_id += 1
    identity = taille_id / float(tmp[12].split(":")[2])
    if identity > 0.9 and int(tmp[12].split(":")[2]) > int(sys.argv[4]):
        output.write(aln)
f.close()
output.close()
