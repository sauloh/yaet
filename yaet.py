#!/usr/bin/python
#-*- coding:utf-8 -*-

from bingpy import WebSearch
import sys 

output = open(sys.argv[3], 'a') # Output File
inputIps = open(sys.argv[1], 'r') # Input Ips
nResults = int(sys.argv[2])	# Number of Results

web = WebSearch("") # BING API
pages = web.search("IP:", nResults)


for page in pages:
	output.write("%s - %s\n" % (page.title.encode('utf-8'), page.url.encode('utf-8')))

output.close()
