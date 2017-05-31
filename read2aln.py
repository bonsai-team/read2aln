#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os, argparse

def install_mode(args):
    if not os.system("test -e graphmap/bin/Linux-x64/graphmap"):
        print("Already done.")
    else:
        os.system("git submodule update --init --recursive")
        os.system("git submodule foreach git pull origin master")
        os.system("make -C graphmap")
    return

def demo_mode(args):
    os.system("graphmap/bin/Linux-x64/graphmap align -r examples/example_seqs.fa -d examples/example_seqs.fa -o examples/example_aln.sam")
    return

def run_mode(args):
    os.system("graphmap/bin/Linux-x64/graphmap align -r " + args.reads + " -d " + args.reads + " -o " + os.path.splitext(args.reads)[0] +".sam")
    return

parser = argparse.ArgumentParser(description = "Find the similarities between long reads.")
subparser = parser.add_subparsers(help = "Choose how to run the program")
parser_install = subparser.add_parser("install", help = "Install the program")
parser_install.set_defaults(func = install_mode)
parser_run = subparser.add_parser("run", help = "Run the program for a set of long reads")
parser_run.add_argument("reads", type = str, help = "Reads in fasta format")
parser_run.set_defaults(func = run_mode)
parser_demo = subparser.add_parser("demo", help = "Run the program with the example file")
parser_demo.set_defaults(func = demo_mode)
args = parser.parse_args()
args.func(args)
