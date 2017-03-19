#!/usr/bin/env python2
import sys
import krakenex
import json

k = krakenex.API()

interval=1 # 1 minute, 5, 15 ,30, 60, 240, 1440, 10080

json_query_string = k.query_public('OHLC',{'pair':'XXBTZEUR','interval':interval})

print json.dumps(json_query_string, sort_keys=True, indent=4, separators=(',',': '))

