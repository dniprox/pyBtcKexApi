#!/usr/bin/env python2
import sys
import krakenex
import json
import datetime

def print_time(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y%m%d-%H%M%S')

def send_query(entries):    
    k = krakenex.API()
    return k.query_public('Depth', {'pair': 'XXBTZEUR','count':entries})

number_of_entries=1
json_query_string=send_query(number_of_entries)

#print json_query_string
#json_dump=json.dumps(json_query_string, sort_keys=True, indent=4, separators=(',',': '))

#print json_dump

ask=json_query_string['result']['XXBTZEUR']['asks'][0][0]
askvol=json_query_string['result']['XXBTZEUR']['asks'][0][1]
asktime=json_query_string['result']['XXBTZEUR']['asks'][0][2]

bid=json_query_string['result']['XXBTZEUR']['bids'][0][0]
bidvol=json_query_string['result']['XXBTZEUR']['bids'][0][1]
bidtime=json_query_string['result']['XXBTZEUR']['bids'][0][2]

print "Time:",print_time(asktime)," Ask:",ask," Vol:",askvol
print "Time:",print_time(bidtime)," Bid:",bid," Vol:",bidvol




