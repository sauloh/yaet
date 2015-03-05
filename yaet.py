#!/usr/bin/python
#-*- coding:utf-8 -*-

from bingpy import WebSearch
import sys, os

# Initializing data
bing_key = os.environ.get('BING_KEY') # Get BING_API from Environment Variable
output = open(sys.argv[3], 'a') # Output File
inputIps = open(sys.argv[1], 'r') # Input Ips
nResults = int(sys.argv[2])	# Number of Results

web = WebSearch(bing_key) # BING API

for ip in inputIps.readlines():
	pages = web.search("IP:%s" % (ip), nResults)
	for page in pages:
		output.write("%s - %s\n" % (page.title.encode('utf-8'), page.url.encode('utf-8')))

output.close()
