import json
import time
import csv
import argparse
import datetime
import spacy
import os
import sys
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
from collections import Counter

constructList=[]

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--constructdictionary", help="Construct dictionary file with extension")
    parser.add_argument("-o", "--outputfile", help="Output file name with extension", required = False, default= "")
    parser.add_argument("-i", "--inputfile", help="Input file name with extension")

    args = parser.parse_args()
    if args.constructdictionary is None or args.inputfile is None:
        parser.error("please add necessary arguments")
    with open(args.constructdictionary) as f:
        reader = csv.reader(f, delimiter=",", quotechar="\"")
        next(reader)
        for constructRow in reader:
            constructList.append(constructRow[0].lower())
    print("completed loading construct dictionary")
    
    fO = open(args.outputfile, "w", encoding="utf-8")
    #drugCount = {}
    with open(args.inputfile, 'r') as f:
        cnt = 0
        for line in f:
            fields = line.rstrip().split('/t')
            abstractText = fields[0]
            for construct in constructList:
                if construct in abstractText:
                    fO.write( construct + "," + abstractText + "\n")
main()
