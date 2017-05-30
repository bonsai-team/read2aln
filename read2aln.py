#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os, sys

def print_usage():
    print ("Usage :\n\tpython read2aln.py install\nthen")
    print ("\tpython read2aln.py run reads.fa\nor")
    print ("\tpython read2aln.py demo")
    return;

if __name__ == '__main__':
    print(sys.argv)
    print(len(sys.argv))
    if len(sys.argv) != 2 | len(sys.argv) != 3 and sys.argv[1] != "run":
        print_usage()
    elif sys.argv[1] == "install":
        if not os.system("test -e graphmap/bin/Linux-x64/graphmap"):
            print("Already done.")
        else:
            os.system("git submodule update --init --recursive")
            os.system("git submodule foreach git pull origin master")
            os.system("make -C graphmap")
    elif sys.argv[1] == "demo":
        print("Searching overlaps between reads...")
        os.system("graphmap/bin/Linux-x64/graphmap align -x overlap -r examples/example_seqs.fa -d examples/example_seqs.fa -o examples/example_aln.sam")
    elif sys.argv[1] == "run":
        os.system("graphmap/bin/Linux-x64/graphmap align -x overlap -r " + sys.argv[2] + " -d " + sys.argv[2] + " -o " + os.path.splitext(sys.argv[2])[0] +".sam")
    else:
        print_usage()
