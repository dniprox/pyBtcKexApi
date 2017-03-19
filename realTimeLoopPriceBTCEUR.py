#!/usr/bin/env python2
import sys
import krakenex
import json
import datetime
import time

def print_time(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y%m%d-%H%M%S')

def send_query(entries):    
    k = krakenex.API()

    query=None
    try:
        query=k.query_public('Depth', {'pair': 'XXBTZEUR','count':entries})
    except:
        e = sys.exc_info()[0]
        print "Error doing a query public againts krakenex API"

    return query



while True:

    number_of_entries=1
    json_query=send_query(number_of_entries)

    if json_query != None:
        try:
            ask=json_query['result']['XXBTZEUR']['asks'][0][0]
            askvol=json_query['result']['XXBTZEUR']['asks'][0][1]
            asktime=json_query['result']['XXBTZEUR']['asks'][0][2]

            bid=json_query['result']['XXBTZEUR']['bids'][0][0]
            bidvol=json_query['result']['XXBTZEUR']['bids'][0][1]
            bidtime=json_query['result']['XXBTZEUR']['bids'][0][2]

            f = open("prices.dat","a")
            print >>f, "Time:",print_time(asktime)," Ask:",ask," Vol:",askvol," Time:",print_time(bidtime)," Bid:",bid," Vol:",bidvol
            f.close()
            
        except:
            e = sys.exc_info()[0]
            print "Error parsing json query:",e
            try:
                print json_query['result']
            except:
                print json_query
    else:
        print "Error sending query to Kraken API"

    time.sleep(10)
    





