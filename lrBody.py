#!/usr/bin/python3
#-*- coding: UTF-8 -*-

#import os
import sys
import logging
import argparse
import time
import re
import json

def parse_args():
	"""Parse the command line for options."""
	parser = argparse.ArgumentParser(description='LR fixer')

	parser.add_argument('-i', '--input_file_name', default='ActionBody.c', help='Input Loadrunner file name')
	parser.add_argument('-o', '--output_file_name', default='ActionBodyPretty.c', help='Output file name')

	options = parser.parse_args()

	return options

def bodyArgumentsLineByLine(match):
	options = parse_args()
	match = match.group()
	match = match.replace('\n','').replace('\t','').replace(' ','').replace(',LAST);','').replace('"','')
	#remove last & if eol:
	match = re.sub(r'&$', '', match)
	#divide into lines, add " at eol:
	match = match.replace('&','&"\n"')
	return '"' + match + '",\nLAST);'


def run_as_script():
	options = parse_args()
	
	lrAction = open(options.input_file_name,'r').read()
	
	#body contains parameters a=b&c=d
	lrAction = re.sub(r'"Body=[a-zA-Z0-9].*?LAST\);', bodyArgumentsLineByLine, lrAction, flags=re.DOTALL)
	#print(lrAction)
		
	with open(options.output_file_name, 'w', newline='\r\n') as actionfile:
		actionfile.write(lrAction)
		#print('### Fixed action written to %s' % (options.out_file_name))
	
	#sys.exit()
	
if __name__ == '__main__':
	sys.exit(run_as_script())


#NTP
#tempus1.gum.gov.pl 194.146.251.100
#tempus2.gum.gov.pl 194.146.251.101
