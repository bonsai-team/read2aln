import sys
import time
import os
from Bio import SeqIO
from Bio.SeqIO.FastaIO import SimpleFastaParser

try:
    start_time = time.time()
    reads = {}
    print ("Reading reads...\n")
    with open(sys.argv[2]) as handle:
        for values in SimpleFastaParser(handle):
            reads[values[0]] = values[1]
    reads = sorted(reads.items())
    ref = []
    print ("Collecting reference genes... chr" + sys.argv[4] + "...\n")
    for record in SeqIO.parse(sys.argv[1], 'fasta'):
        if record.description.split(":")[2] == sys.argv[4]:
            ref.append(record.name)
    f = open(sys.argv[3], "r")
    sam = f.readlines()
    sam = sorted(sam)
    output = open("chr" + sys.argv[4] + "_aligned.fa", "w")
    it = 0
    print ("Reading alignment file...\n")
    for aln in sam:
        if aln.split()[2] in ref:
            while reads[it][0] != aln.split()[0]:
                it += 1
            output.write(">" + reads[it][0] + "\n" + reads[it][1] + "\n")
    output.close()
    os.system("head -n -1 chr" + sys.argv[4] + "_aligned.fa > reads_chr" + sys.argv[4] + "_aligned.fa")
    os.system("rm chr" + sys.argv[4] + "_aligned.fa")
    interval = time.time() - start_time
    print ("Done.\n\tTotal time in sec : " + str(interval))
except:
    print ("Usage :\n\tpython parser_chromosome.py ref_genome.fa reads.fa align.sam chromosome\n")
