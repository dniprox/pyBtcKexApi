#!/usr/bin/env python2

import sys
import krakenex
import json

def send_query():

    try:
        k = krakenex.API()
    except Exception:
        print "Fault initiating API"
        return -1;
    try:
        k.load_key('kraken.key')
    except Exception:
        print "Credential could not be found"
        return -1;
    
    return k.query_private('Balance')

query_string=send_query()

if query_string != -1:
    dictResult=query_string['result']
    dictError=query_string['error']
    print "Amount in Euros :  ",dictResult['ZEUR']
    print "Amount in BTC   :  ",dictResult['XXBT']
else:
    print "Error querying API"

