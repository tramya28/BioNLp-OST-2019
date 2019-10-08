#!/usr/bin/env python
import json
import time
import csv
import argparse
import re
import datetime
import spacy
import os
import sys
import threading
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span

constructList=[]
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--constructdictionary", help="Construct dictionary file with extension")
    parser.add_argument("-o", "--outputfile", help="Output file name with extension", required = False, default= "")
    parser.add_argument("-i", "--inputfile", help="Input file name with extension")
   
    args = parser.parse_args()
    if args.constructdictionary is None or args.inputfile is None:
        parser.error("please add necessary arguments")
    
    starttime = datetime.datetime.now()
    
    print(starttime)
    with open(args.constructdictionary) as f:
        reader = csv.reader(f, delimiter=",", quotechar="\"")
        next(reader)
        for constructRow in reader:
            constructList.append(constructRow[0].lower())
    print("completed loading construct dictionary")
    fO = open(args.outputfile, "w", encoding="utf-8")
    
    with open(args.inputfile, 'r', encoding="utf-8") as f:
        for line in f:
            #print (line)
            fields = line.rstrip().split(' (#$@!!@$#) ')
            abstractText = fields[1]
            #print (abstractText)
            for construct in constructList:
                if construct in abstractText:
                    fO.write( construct + " (#$@!!@$#) " + abstractText + "\n") 
        fO.close()
# main invoked here    
main()