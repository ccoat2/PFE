#!/usr/bin/env python2.7

import csv # Wont work if csv no present, you forgot it !
import json # Wont work if json no present, you forgot it !
import logging
import sys
import os
import pymongo
from pymongo import MongoClient

def convert(fullpath,directory):
    if not fullpath.endswith('.csv'):
        # Use logging for debug statement
        logging.info("Not a CSV file: %s", fullpath)
        # exit if not a CSV file
        return      
    logging.info("Opening CSV file: %s", fullpath)
    # pattern to open file and automatically close it
    with open(fullpath, 'r') as f:
        csv_reader = csv.DictReader(f)
        json_fullpath = fullpath.split(".")[0] + ".json"
        logging.info("Saving JSON to file: %s", json_fullpath)
        with open(json_fullpath, 'w') as jsonf:
            # open row by row, to be able to insert localisation field
            jsonf.write('[')
            for row in csv_reader:
            	row ["prevision"] = directory
                row["localisation"] = json_fullpath.split("/")[len(json_fullpath.split("/"))-1].split("_")[0]
                # dump one by one the entries
                json.dump(row, jsonf)
                jsonf.write(',')
            jsonf.seek(-1, os.SEEK_END)
            jsonf.truncate()
            jsonf.write(']')
        
        with open(json_fullpath,'r') as jsonf:
            client = MongoClient('localhost', 27017)
            #print (json.load(jsonf))
            db = client.mydb            
            pfe = db.db_pfe
            pfe.insert(json.load(jsonf))
            
def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    # Check if one paramter is present
    assert len(sys.argv) == 3
    # Get first parameter and pass it to the method
    i = 0
    for root, dirs, files in os.walk(os.path.abspath(sys.argv[1])):
    	for f in files:
           	convert(os.path.join(root, f),sys.argv[2])

# Pattern for "main" function
if __name__ == '__main__':
    main()


#Wpred   
#real	2m9.796s
#user	1m20.511s
#sys	0m6.020s

#Weprog
#real	26m40.322s
#user	15m11.995s
#sys	1m17.981s


#WRF
#18 Mai 2012 wfr manquant jusqu'au 31
#16 et 17 Juin 2012
#19 jusqu'au 22 Juin 2012
#6 jusqu'au 09 Juin 2012
