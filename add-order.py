#!/usr/bin/env python2

# This file is part of krakenex.
# Licensed under the Simplified BSD license. See examples/LICENSE.

# Demonstrates how to use the conditional close functionality; that is,
# placing an order that, once filled, will place another order.
#
# This can be useful for very simple automation, where a bot is not
# needed to constantly monitor execution.

import sys,getopt
import krakenex

def send_query(type_order,price,volume,leverage):

    # Get Kraken API
    k = krakenex.API()
    # Loading credentials
    k.load_key('kraken.key')

    query_arguments = {'pair': 'XXBTZEUR',
                                           'type': type_order,        # type: {buy.sell}
                                           'ordertype': 'limit',      # always limit
                                           'price': price,            # price: XXX.XX
                                           'volume': volume,          # volume: X.XX (first leg of currency)
                                           'leverage': leverage   }    # leverage taken
    
    ret_val = k.query_private('AddOrder', query_arguments)
    return ret_val
    
def main(argv):
        
    type_order = ''
    price = ''
    volume = ''
    leverage = ''


    def pringHelp():
        print 'add-order.py -t <type> -p <price> -v <volume> -l <leverage>'    
    try:
        opts, args = getopt.getopt(argv,"ht:p:v:l",["type=","price=","vol=","leverage="])
    except getopt.GetoptError:
        print 'Exception Launched'
        sys.exit(2)
        for opt,arg in opts:
            if opt == '-h':
                printHelp()
    for opt, arg in opts:
        if opt == '-h':
            printHelp()
            sys.exit()
        elif opt in ("-t", "--type"):
            type_order = arg
        elif opt in ("-p", "--price"):
            price  = arg
        elif opt in ("-v", "--vol"):
            volume = arg
        elif opt in ("-l", "--lev"):
            leverage = arg    
            

    ret = send_query(type_order,price,volume,5)
    print "Order Send Completed Done at Leverage 5:"
    print 'Type:',type_order,' Price:',price, ' Volume:',volume, ' Leverage:',leverage        
    print "Return JSON Statment:",ret

    
if __name__ == "__main__":
    main(sys.argv[1:])

   

