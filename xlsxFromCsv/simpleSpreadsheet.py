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
import numpy as np
import pandas as pd


def parse_args():
	"""Parse the command line for options."""
	parser = argparse.ArgumentParser(description='LR fixer')

	parser.add_argument('-i', '--input_file_name', default='template.csv', help='Input csv')
	parser.add_argument('-o', '--output_file_name', default='object.xlsx', help='Output file name')

	options = parser.parse_args()

	return options




def run_as_script():
	options = parse_args()
	
	

	tab1content = {'col_a': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c']),
				  'col_b': pd.Series(data=np.random.randint(10, 100, 3),	index=['a', 'b', 'c']),
				  'col_c': pd.Series(data=np.random.randint(10, 100, 3),	index=['a', 'b', 'c'])}
	tab2content = {'col_a': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c']),
				   'col_b': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c']),
				   'col_c': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c'])}
	tab3content = {'col_a': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c']),
				   'col_b': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c']),
				   'col_c': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c'])}
	tab4content = {'col_a': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c']),
				   'col_b': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c']),
				   'col_c': pd.Series(data=np.random.randint(10, 100, 3),index=['a', 'b', 'c'])}
	tab1 = pd.DataFrame(data=tab1content)
	tab2 = pd.DataFrame(data=tab2content)
	tab3 = pd.DataFrame(data=tab3content)
	tab4 = pd.DataFrame(data=tab4content)

	#with open(options.output_file_name, 'w', newline='\r\n') as actionfile:
	with pd.ExcelWriter(options.output_file_name, engine='xlsxwriter') as spreadsheetWriter:
		tab1.to_excel(spreadsheetWriter, sheet_name='tab1', index=False)
		tab2.to_excel(spreadsheetWriter, sheet_name='tab2', index=False)
		tab3.to_excel(spreadsheetWriter, sheet_name='tab3', index=False)
		tab4.to_excel(spreadsheetWriter, sheet_name='tab4', index=False)
	
if __name__ == '__main__':
	sys.exit(run_as_script())


