#!/usr/bin/env python2

import sys
import krakenex  # This is the installation of Kraken API for python
import json
import datetime
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pylab as p
import numpy as np
from pymongo import MongoClient

# Initializing Mongo Connection
client = MongoClient()
db = client['bitkraken']
symbol='XXBTZEUR'
books = db[symbol+'_books'] # Mongo Database name 


def print_time(timestamp):
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y%m%d-%H%M%S')

# Funtion to send queries to the Kraken APU
def send_query(entries):    

    k = krakenex.API()
    
    jquery=None
    try:
        jquery = k.query_public('Depth', {'pair': 'XXBTZEUR','count':entries})
    except:
        e = sys.exc_info()[0]
        print "Error getting a jquery public from Krakenex API:",e

    
    return jquery
    
#print json_query_string
#json_dump=json.dumps(json_query_string, sort_keys=True, indent=4, separators=(',',': '))
#print json_dump


class Book(object):
    def __init__(self,ask,askvol,asktime,bid,bidvol,bidtime):
        self.ask = ask
        self.askvol = askvol
        self.asktime = asktime
        self.bid = bid
        self.bidvol = bidvol
        self.bidtime = bidtime



        
def get_book_entry(bid_ask,number_entry,price_vol_time):
    value = None
    try:
        price_vol_time = [0 if price_vol_time=='price' else 1 if price_vol_time=='vol' else 2 if price_vol_time=='time' else -1]
        
        value = json_query_string['result']['XXBTZEUR'][bid_ask][number_entry][price_vol_time[0]]
               
    except:
        e = sys.exc_info()[0]
        print "Error getting public query againts krakenex API"

    return value
        
        
def fill_book(number_of_entries):

    # List of variable to store the entries
    ask = []
    askvol = []
    asktime = []
    bid = []
    bidvol = []
    bidtime = []

    for n in range(0,number_of_entries):
        ask.append(get_book_entry('asks',n,'price'))
        askvol.append(get_book_entry('asks',n,'vol'))
        asktime.append(get_book_entry('asks',n,'time'))

        bid.append(get_book_entry('bids',n,'price'))
        bidvol.append(get_book_entry('bids',n,'vol'))
        bidtime.append(get_book_entry('bids',n,'time'))

    book = Book(ask,askvol,asktime,bid,bidvol,bidtime)        
    return book
    
def print_book(ask,bid,askvol,bidvol,asktime,bidtime):
    for i in reversed(range(0,number_of_entries)):
        print "Time:",print_time(asktime[i])," Ask:",ask[i]," Vol:",askvol[i]
    print "---------------------------------------------"    
    for i in range(0,number_of_entries):
        print "Time:",print_time(bidtime[i])," Bid:",bid[i]," Vol:",bidvol[i]
        
def plot_book(book):
    
    x1 = [p for p in book.ask]
    x2 = [p for p in book.bid]
    y1 = [v for v in book.askvol]
    y2 = [v for v in book.bidvol]

    plt.scatter(x1,y1,color='red',s=5)
    plt.scatter(x2,y2,color='blue',s=5)
    plt.show()    


num_queries=10
json_query_string=send_query(num_queries)
book = fill_book(num_queries)

print book.ask
# 6 is the number of variable on the book
#print np.reshape(book,(num_queries,6))


plot_book(book)    
#print get_book_entry('asks',0,'price')


