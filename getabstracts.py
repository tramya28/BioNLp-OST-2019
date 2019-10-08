import sys, urllib, re, json, socket, string
from xml.dom import minidom
import glob
import argparse
import csv
import datetime
import time

# parse an xml file by name
xmlFilesList = []

def xmlParse(inputPath):
    xmlFiles = glob.glob(inputPath + '/**/*.xml', recursive=True)
    for file in xmlFiles:
        xmlFilesList.append(file)
    return xmlFilesList


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--inputpath", help="Enter input path")
    parser.add_argument("-o", "--outputfile", help="Output file name with extension", required = False, default= "")
    args = parser.parse_args()
    if args.inputpath is None:
        parser.error("please add necessary arguments")
    
    starttime = datetime.datetime.now()
    print(starttime)
    xmlFilesList = xmlParse(args.inputpath) 
    fO = open(args.outputfile, "a", encoding="utf-8")
    for xmlfile in xmlFilesList:
        mydoc = minidom.parse(xmlfile)
        titleCount = 0
        abstactTextCount = 0
        items = mydoc.getElementsByTagName('MedlineCitation')

        # print all items
        for item in items:
            titleItem = item.getElementsByTagName('ArticleTitle')
            abstractTextItem = item.getElementsByTagName('AbstractText')

            if len(titleItem) > 0:
                titleCount += 1
            
            if len(abstractTextItem) > 0:
                abstactTextCount += 1
            abstractTitle = (titleItem[0].firstChild.nodeValue  if (len(titleItem) > 0 and titleItem[0].firstChild is not None and titleItem[0].firstChild.nodeValue is not None) else " No Title ") 
            abstractText = (abstractTextItem[0].firstChild.nodeValue or "" if (len(abstractTextItem) > 0 and abstractTextItem[0].firstChild is not None and abstractTextItem[0].firstChild.nodeValue is not None)  else " No Text ")
            abstractTitle = abstractTitle.replace('\n',' ')
            abstractTitle = abstractTitle.replace('\t',' ')
            abstractText = abstractText.replace('\n',' ')
            abstractText = abstractText.replace('\t',' ')
            abstractText = abstractText.replace(' (#$@!!@$#) ',' ')
            abstractTitle = abstractTitle.replace(' (#$@!!@$#) ',' ')
            fO.write(abstractTitle + " (#$@!!@$#) " + abstractText + "\n" )
            fO.flush()
    fO.close()
    stoptime = datetime.datetime.now()
    timedifference = stoptime - starttime
    print("Time taken to get all abstracts is " + str(timedifference))
main()  #break


