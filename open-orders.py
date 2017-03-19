#!/usr/bin/env python2

# This script print out the open orders on your account summary
# the total volumen, average price and total fees


import krakenex
import json

    
def printOpenPositions():

    # Sum variables for volume, price and fees
    sumVol = 0
    sumPriceVol = 0
    sumfee = 0
    
    print "Open positions"
    print "--------------"
    def getOrderValue(order_code,string):
        return query_string["result"][order_code][string]

    for order_code in query_string["result"]:
        # list of keys to extract from the query
        listKeys=["ordertype","pair","type","cost","fee","margin","vol"]
        listKeyValues=[]    
        for key in listKeys:
            listKeyValues.append([key,getOrderValue(order_code,key)])
        string_out=""
        for keyValue in listKeyValues:
            string_out+=keyValue[0]+":"+keyValue[1]+"|"

        cost = getOrderValue(order_code,"cost")
        vol  = getOrderValue(order_code,"vol")
        fee  = getOrderValue(order_code,"fee")
        price = float(cost) / float(vol)
        string_out+=" price:"+str(price)
        print string_out

        sumPriceVol += float(price) * float(vol)
        sumVol += float(vol)
        sumfee += float(fee)

    return sumPriceVol,sumVol,sumfee

def printJSONquery(json_string):
    print json.dumps(json_string, sort_keys=True, indent=4, separators=(',',': '))    


# creating the API object
k = krakenex.API()
# loading privete API keys
k.load_key('kraken.key')

query_string=[]

try:
    query_string=k.query_private('OpenPositions',{'pair':'XXBTZEUR'})

    #printJSONquery(query_string)
    sumPriceVol,sumVol, sumfee = printOpenPositions()

    # Check whether we have volumen or not
    if sumVol > 0:
        print "Average Price:", sumPriceVol / sumVol
        print "Total Volume:", sumVol
        print "Total Fees:", sumfee
    else:
        print "No open orders"
except:
    e = sys.exc_info()[0]
    print "ERROR on query private againts krakenex API"

    
