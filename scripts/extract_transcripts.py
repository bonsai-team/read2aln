from Bio import SeqIO
import sys

# sort la liste des transcrits pour 1 chromosome voulu
#usage : python extract_transcripts.py ref.fa chr

f = open("transcripts_list.grp", "w")
transcripts = []
for record in SeqIO.parse(sys.argv[1], "fasta"):
    if record.description.split(":")[2] == sys.argv[2]:
        transcripts.append(record.name + "\n")
f.writelines(transcripts)
f.close()
