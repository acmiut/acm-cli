#! /bin/python3

import argparse
import os

parser = argparse.ArgumentParser()

# Program Arguments
parser.add_argument("--init" , help="initiates the repository for acm icpc problem solving")
parser.add_argument("--solve" , help="creates (or opens the existed) problem to solve")
parser.add_argument("--test" , help="compiles and runs with the given input file")
parser.add_argument("--commit" , help="gets and commits the status about the problem")
parser.add_argument("--addinput" , help="adds an input file to the problem")



# Reading Aeguments

args = parser.parse_args()


if args.init:
    print ("init called!")

if args.solve:
    print ("salve called!")

if args.commit:
    print ("commit called!")
