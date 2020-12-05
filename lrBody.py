#!/usr/bin/python3
#-*- coding: UTF-8 -*-

#import os
import sys
import logging
import argparse
import time
import re
import json
import xml.etree.ElementTree
from xml.dom import minidom

def parse_args():
	"""Parse the command line for options."""
	parser = argparse.ArgumentParser(description='LR fixer')

	parser.add_argument('-i', '--input_file_name', default='ActionBody.c', help='Input Loadrunner/C file name')
	parser.add_argument('-o', '--output_file_name', default='ActionBodyPretty.c', help='Output file name')

	options = parser.parse_args()

	return options

def bodyArgumentsLineByLine(match):
	#options = parse_args()
	match = match.group()
	match = match.replace('\n','').replace('\t','').replace(' ','').replace('"','').replace(',LAST);','')
	#remove last & if eol:
	match = re.sub(r'&$', '', match)
	#divide into lines, add " at eol:
	match = match.replace('&','&"\n"')
	
	print("\nXXXXXXXX")
	print(match)
	
	return '"' + match + '",\nLAST);'

def prettyPrintJson(match):
	#options = parse_args()
	#print("\n### json fix")
	
	#prepare for parsing
	match = match.group()
	match = match.replace('"Body=','').replace('LAST);','')
	#" as first/last char in line
	#match = match.replace('\n"','\n').replace('"\n','\n')
	#remove last " if eol:
	match = re.sub(r',[ \t]*$', '', match, flags=re.MULTILINE)
	match = re.sub(r'"$', '', match, flags=re.MULTILINE)
	match = re.sub(r'^[\t ]*"', '', match, flags=re.MULTILINE)
	match = match.replace('\n','')
	match = match.replace('\\\\n','')
	match = match.replace('\\\\','\\') #embedded json decode
	#print("xxxxxxxxxxx")
	#print(match)
	#unescape \"
	match = match.replace('\\"','"')
	#print("zzzzzzzzzz")
	#print(match)
	
	##parse json
	parsed = json.loads(match)
	parsed = json.dumps(parsed, indent="\t", sort_keys=False)
	#print("xxxxx222")
	#print(parsed)
	
	#encode json back
	match = match.replace('\\','\\\\') #embedded json encode
	match = parsed.replace('"', '\\"')
	#" as first/last char in line
	match = re.sub(r'$', '"', match, flags=re.MULTILINE)
	match = re.sub(r'(^[\t]*)', '\\1"', match, flags=re.MULTILINE)

	#print("yyyyyyY")
	#print(match)
	return '"Body="\n' + match + ',\nLAST);'

def prettyPrintXml(match):
	#options = parse_args()
	
	#clean XML
	match = match.group()
	match = match.replace('"Body=','').replace('LAST);','')

	#remove first/last " in line
	match = re.sub(r',[ \t]*$', '', match, flags=re.MULTILINE)
	match = re.sub(r'"$', '', match, flags=re.MULTILINE)
	match = re.sub(r'^[\t ]*"', '', match, flags=re.MULTILINE)
	
	#concatenate lines
	match = match.replace('\n','')

	#unescape \"
	match = match.replace('\\"','"')
	
	##process XML
	xmlBody = xml.dom.minidom.parseString(match)
	prettyXmlBody = xmlBody.toprettyxml()
	#print(prettyXmlBody)

	#remove xml declaration
	match = prettyXmlBody.replace('<?xml version="1.0" ?>\n','')

	#encode " with \"
	match = match.replace('"', '\\"')
	#" as first/last char in line
	match = re.sub(r'$', '"', match, flags=re.MULTILINE)
	match = re.sub(r'(^[\t ]*)', '\\1"', match, flags=re.MULTILINE)

	#remove empty line
	match = re.sub(r'^[ \t]*""\n', '', match, flags=re.MULTILINE)
	match = re.sub(r'\\n\\n', '', match, flags=re.MULTILINE)
	match = match.replace('""', '')
	
	#print(match)
	
	return '"Body="\n' + match + ',\nLAST);'

def run_as_script():
	options = parse_args()
	
	lrAction = open(options.input_file_name,'r').read()
	
	#body contains parameters a=b&c=d
	lrAction = re.sub(r'"Body=[a-zA-Z0-9].*?LAST\);', bodyArgumentsLineByLine, lrAction, flags=re.DOTALL)
	#print(lrAction)
		
	#body contains JSON
	lrAction = re.sub(r'"Body=[\[{].*?LAST\);', prettyPrintJson, lrAction, flags=re.DOTALL)
	#print(lrAction)
		
	#body contains XML
	lrAction = re.sub(r'"Body=<.*?LAST\);', prettyPrintXml, lrAction, flags=re.DOTALL)
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
