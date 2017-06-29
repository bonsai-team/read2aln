#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os, argparse, time, multiprocessing
from joblib import Parallel, delayed
from Bio import SeqIO

def demo_mode(args):
    os.system("bin/lastdb tmpdb examples/example_seqs.fa")
    os.system("bin/lastal tmpdb examples/example_seqs.fa > examples/example_aln.maf")
    os.system("bin/maf-convert sam examples/example_aln.maf > examples/example_aln.sam")
    os.system("python scripts/delete_double.py examples/example_aln.sam examples/output.sam")
    os.system("python scripts/parse_evalue.py examples/output.sam examples/aln.sam 10e-10 65")
    os.system("find examples/ ! \( -name \"aln.sam\" -o -name \"example_seqs.fa\" \) -type f -exec rm -f {} + | rm tmp*")
    return

def mapping_LAST(num_tmp):
    os.system("bin/lastal tmpdb tmp" + str(num_tmp) + ".fa > tmp" + str(num_tmp) + ".maf")
    os.system("bin/maf-convert sam "+ "tmp" + str(num_tmp) + ".maf > tmp" + str(num_tmp) + ".sam")
    return

def run_mode(args):
    start_time = time.time()
    if (os.path.splitext(args.reads)[1] == ".fq" or os.path.splitext(args.reads)[1] == ".fastq"):
        if args.v:
            print("Converting fastq to fasta...")
        os.system("sed -n '1~4s/^@/>/p;2~4p' " + args.reads + " > " + os.path.splitext(args.reads)[0] + ".fa")
        args.reads = os.path.splitext(args.reads)[0] + ".fa"
    if args.v:
        print("Deleting bad reads")
    os.system("bin/dustmasker -in " + args.reads + " -out tmp_dustmasker -outfmt acclist")
    os.system("python scripts/delete_fail.py " + args.reads + " " + args.length)
    if args.v:
        print("Creating index...")
    os.system("bin/lastdb tmpdb " + args.reads)
    if args.v:
        print("Aligning reads against reads...")
    if args.P:
        os.system("bin/lastal -P " + args.P + " tmpdb " + args.reads + " > " + os.path.splitext(args.reads)[0] + ".maf")
    else:
        os.system("bin/lastal tmpdb " + args.reads + " > " + os.path.splitext(args.reads)[0] + ".maf")
    os.system("bin/maf-convert sam "+ os.path.splitext(args.reads)[0] + ".maf > " + os.path.splitext(args.reads)[0] + ".sam")
    if args.v:
        print("Deleting bad alignments...")
    os.system("python scripts/delete_double.py " + os.path.splitext(args.reads)[0] + ".sam output.sam")
    os.system("python scripts/parse_evalue.py output.sam " + os.path.splitext(args.reads)[0] + ".sam " + args.evalue + " " + args.length)
    if args.v:
        print("Cleaning folder...")
    if args.P:
        os.system("rm tmp* output.sam")
    else:
        os.system("rm tmp* output.sam " + os.path.splitext(args.reads)[0] + ".maf")
    if args.v:
        print("Done.\n\tTotal time in sec : " + str(time.time() - start_time))
    return

parser = argparse.ArgumentParser(description = "Find the similarities between long reads.")
subparser = parser.add_subparsers(help = "Choose how to run the program")
parser_run = subparser.add_parser("run", help = "Run the program for a set of long reads")
parser_run.add_argument("reads", type = str, help = "Reads in fasta/fastq format")
parser_run.add_argument("--length", help = "Minimum length of alignments [65]", default = "65", action = 'store')
parser_run.add_argument("--evalue", help = "Maximum e-value of alignments [10e-10]", action = 'store', default = '10e-10')
parser_run.add_argument("-v", help = "Be verbose", action = 'store_true')
parser_run.add_argument("--train", help = "Train score parameters", action = 'store_true')
parser_run.add_argument("-P", help = "Allow parallelization [2]", action = 'store', default = 0)
parser_run.set_defaults(func = run_mode, evalue = "10e-10", size = "65")
parser_demo = subparser.add_parser("demo", help = "Run the program with the example file")
parser_demo.set_defaults(func = demo_mode)
args = parser.parse_args()
args.func(args)
