#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os, argparse

def demo_mode(args):
    os.system("bin/lastdb tmpdb examples/example_seqs.fa")
    os.system("bin/lastal tmpdb examples/example_seqs.fa > examples/example_aln.maf")
    os.system("bin/maf-convert sam examples/example_aln.maf > examples/example_aln.sam")
    os.system("python scripts/delete_double.py examples/example_aln.sam examples/output.sam")
    os.system("python scripts/parse_evalue.py examples/output.sam examples/aln.sam")
    os.system("find examples/ ! \( -name \"aln.sam\" -o -name \"example_seqs.fa\" \) -type f -exec rm -f {} + | rm tmp*")
    return

def run_mode(args):
    os.system("bin/lastdb tmpdb " + args.reads)
    os.system("bin/lastal tmpdb " + args.reads + " > " + os.path.splitext(args.reads)[0] + ".maf")
    os.system("bin/maf-convert sam "+ os.path.splitext(args.reads)[0] + ".maf > " + os.path.splitext(args.reads)[0] + ".sam")
    os.system("python scripts/delete_double.py " + os.path.splitext(args.reads)[0] + ".sam output.sam")
    os.system("python scripts/parse_evalue.py output.sam " + os.path.splitext(args.reads)[0] + ".sam")
    os.system("rm tmp* output.sam " + os.path.splitext(args.reads)[0] + ".maf")
    return

parser = argparse.ArgumentParser(description = "Find the similarities between long reads.")
subparser = parser.add_subparsers(help = "Choose how to run the program")
parser_run = subparser.add_parser("run", help = "Run the program for a set of long reads")
parser_run.add_argument("reads", type = str, help = "Reads in fasta format")
parser_run.set_defaults(func = run_mode)
parser_demo = subparser.add_parser("demo", help = "Run the program with the example file")
parser_demo.set_defaults(func = demo_mode)
args = parser.parse_args()
args.func(args)
