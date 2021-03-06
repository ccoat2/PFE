#!/usr/bin/env python2.7

import csv # Wont work if csv no present, you forgot it !
import json # Wont work if json no present, you forgot it !
import logging
import sys
import os


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
            for row in csv_reader:
            	row ["prevision"] = directory
                row["localisation"] = json_fullpath.split("/")[len(json_fullpath.split("/"))-1].split("_")[0]
                # dump one by one the entries
                data = json.dump(row, jsonf)

def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    # Check if one paramter is present
    assert len(sys.argv) == 2
    # Get first parameter and pass it to the method
    i = 0
    for root, dirs, files in os.walk(os.path.abspath(sys.argv[1])):
    	for dir in dirs:
    	for f in files:
           	convert(os.path.join(root, f),dirs[i])

# Pattern for "main" function
if __name__ == '__main__':
    main()
