#!/usr/bin/env python

""" Created by Mason S. Morales on November 6, 2018
    Copyright (c) 2018 Mason Morales
    Indexes.conf Config Generator
    Run with a filename as an argument. The file should contain a list of index names you want to generate, with each index on its own line.
"""
import argparse
import sys
import traceback

parser = argparse.ArgumentParser()
parser.add_argument("file", help="input filename")

try:
        args = parser.parse_args()
	file = args.file
except:
	print('\n')
	print('Looks like you didn\'t provide any arguments!')
        print('\n')
	print('Here\'s some syntax help: ')
	print('genindexes.py <filename>')
	print('\n')
	sys.exit(0)

def generateIndexes():
	# Iterate through each line in the text file

	try:
		with open(file, 'rt') as f:
			# Remove line breaks from list items
			list=[line.rstrip('\n') for line in f]
		
			# Define l as the number of elements in the list
			l = len(list)

			# Iterate through each item in the list
			for i in list:
					x = i
					x = x.strip()
					print('[' + x + ']')
					print('homePath = $SPLUNK_DB/' + x + '/db')
                    			print('coldPath = $SPLUNK_DB/' + x + '/colddb')
                    			print('thawedPath = $SPLUNK_DB/' + x + '/thaweddb')
					print('frozenTimePeriodInSecs = 604800')
		                        # Set maxTotalDataSizeMB to 100 TB - assume we have enough storage to keep data through frozenTimePeriodInSecs
					print('maxTotalDataSizeMB = 100000000')
                    			# Enable data integrity control as a best practice
                    			print('enableDataIntegrityControl=true')
                    			# Enable larger bucket sizes as a best practice - scales indexer clustering better and yields faster search performance
                    			print('maxDataSize = auto_high_volume')
                    			# Assuming we are in a clustered environment, set the replication factor for this index to automatic, comment this out if not clustered
					sys.stdout.write('repFactor = auto')
					# Print a new line to help with readability
                    			print('\n')
	except:
		print('ERROR: The specified input file does not exist, or parsing failed! Here\'s the exception:\n')
		traceback.print_exc(file=sys.stdout)
		sys.exit(0)

generateIndexes()
