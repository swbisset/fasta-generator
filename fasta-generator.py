import argparse
import sys
import os

import numpy.random
from numpy.random import seed
from numpy.random import randint
import random as Random3

def make_fasta(flength):
    #flength is a list containing the lengths of the fasta(s) to be written
    #return a list of strings
    Random3.seed(1)  #Need to set a seed specifically for Python's random library
    char_list, fastas = ['A', 'C', 'G', 'T'], []
    i = 0
    while i < (len(flength)):
        fasta_chars = Random3.choices(char_list, k=int(flength[i])) #Make a list of random characters samples from char_list
        fastas.append("".join(fasta_chars)) #Join the characters in fasta_chars into a single string
        i+=1
    return fastas

### Start of main code
## Fasta-generator is used to generate a single file of one or more randomised fasta sequences

parser = argparse.ArgumentParser()
parser.add_argument('output', help = "Name of file you would like to generate")
parser.add_argument('-n', '--number', help = "The number of sequences you want to generate. Default is 1")
parser.add_argument('-l', '--lower', help = "The lower limit of fasta size. Default is 100")
parser.add_argument('-u', '--upper', help = "The upper limit of fasta size. Default is 1000")
parser.add_argument('-s', '--specific', help = "Set all generated sequences to the same length. "
                                               "Incompatible with --lower and --upper")
parser.add_argument('-v', '--verbose', help = "Print out all fasta sequence lengths to terminal", action = 'store_true')

err_str = "Type 'python fasta-generator.py -h' for help"    #Default error message

try:
    args = parser.parse_args()
except SystemExit:
    print("No input recognised \n%s" % err_str)
    sys.exit()

args = parser.parse_args()

out_file = args.output

##Begin error check of flags

if args.number:         #Check if user supplied number of fasta sequences to generate
    try:
        int(args.number)
    except ValueError:
        print("Error: Cannot parse '%s' \n%s" % (str(args.number), err_str))
        sys.exit()
    if int(args.number) < 1:
        print("Error: Number of sequences cannot be less than 1")
        sys.exit()
    n = int(args.number)
else:
    n = 1

if args.specific:
    try:
        int(args.specific)
    except ValueError:
        print("Error: cannot pasre '%s' \n%s" % (str(args.specific), err_str))
        sys.exit()
    spec_value = int(args.specific)
    specified = True
else:
    specified = False

if args.lower and not specified:
    try:
        int(args.lower)
    except ValueError:
        print("Error: cannot parse '%s' \n%s" % (str(args.lower), err_str))
        sys.exit()
    lower = int(args.lower)
else:
    lower = 100

if args.upper and not specified:
    try:
        int(args.upper)
    except ValueError:
        print("Error: cannot parse '%s' \n%s" % (str(args.upper), err_str))
        sys.exit()
    upper = int(args.upper)
else:
    upper = 1000

commenting = False
if args.verbose:
    commenting = True

##End error check of flags

numpy.random.seed(1)    #TODO: I suspect this is not actually doing anything, and is just legacy code
if n == 1:
    #Do everything for 1
    if specified:
        flength = spec_value
    else:
        flength = randint(lower, upper, 1)
    fastas = make_fasta(flength)
else:
    #Loop everything
    if specified:
        flength = [spec_value]
        flength *= n
    else:
        flength = randint(lower, upper, n)
    fastas = make_fasta(flength)
if commenting:
    for f in range(0, len(fastas)):
        #print(">header_%s\tlength = %s\n%s" % (str(f+1), str(len(fastas[f])), str(fastas[f])))
        print(">header_%s\tlength = %s bases" % (str(f+1), str(len(fastas[f]))))

#Write to file
if os.path.exists(out_file):
    os.remove(out_file)
outFile = open(out_file, 'a')
i = 0
while i < len(fastas):
    outFile.write(">header_%s\t%s bases\n" % (str(i+1), str(len(fastas[i]))))
    if len(fastas[i]) > 80:
        for j in range(0, len(fastas[i])+80, 80):
            substr = fastas[i][j:(j+80)]
            outFile.write("%s\n" % str(substr))
    else:
        outFile.write("%s\n" % str(fastas[i]))
    i+=1
outFile.close()
print("File written to %s" % (out_file))