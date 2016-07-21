#! /bin/python3

import argparse #to parse Arguments
import os # to run commands
import untangle # for maipulating xml database



parser = argparse.ArgumentParser()

# Program Arguments
parser.add_argument("--init" , help="initiates the repository for acm icpc problem solving" , action = "store_true")
parser.add_argument("--solve" , type = int , help="creates (or opens the existed) problem to solve")
parser.add_argument("--test" , type = int ,help="compiles and runs with the given input file")
parser.add_argument("--commit" , type = int ,help="gets and commits the status about the problem")
parser.add_argument("--addinput" , type = int ,help="adds an input file to the problem")



# Reading Aeguments

args = parser.parse_args()


if args.init:
    print ("init called!")
    

if args.solve:
    str_problem = str(args.solve)
    print ("salve called on problem " + str_problem + "!")

if args.test:
    str_problem = str(args.test)
    print ("test called on problem " + str_problem + "!")

if args.commit:
    str_problem = str(args.commit)
    print ("commit called on problem " + str_problem + "!")
