#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os, sys

def print_usage():
    print ("Usage :\n\tpython read2aln.py install\nthen")
    print ("\tpython read2aln.py run reads.fa\nor")
    print ("\tpython read2aln.py demo")
    return;

if __name__ == '__main__':
    if len(sys.argv) != 2 | len(sys.argv) != 3 & sys.argv[1] != "run":
        print_usage()
    elif sys.argv[1] == "install":
        os.system("git submodule update --init --recursive")
        os.system("git submodule foreach git pull origin master")
        os.system("cd graphmap | make | cd ..")
    elif sys.argv[1] == "demo":
        print("Searching overlaps between reads...")
        os.system("graphmap/bin/Linux-x64/graphmap align -x overlap -r examples/example_seqs.fa -d examples/example_seqs.fa -o examples/example_aln.sam")
    elif sys.argv[1] == "run":
        os.system("graphmap/bin/Linux-x64/graphmap align -x overlap -r " + sys.argv[2] + " -d " + sys.argv[2] + " -o aln.sam")
    else:
        print_usage()
