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

def send_query(type,price,volume):

    """ 
    Arguments:
    type   -- {buy,sell}
    price  -- Price XXX.XX
    volume -- Volume XX.X
    """
    
    k = krakenex.API()
    k.load_key('kraken.key')
    ret=k.query_private('AddOrder', {'pair': 'XXBTZEUR',
                                        'type': type,         # type: {buy.sell}
                                        'ordertype': 'limit', #
                                        'price': price,       # price: XXX.XX
                                        'volume': volume})    # volume: X.XX
    print "done"
    return ret
    
    
def send_query_conditional(type,price):
    
    k = krakenex.API()
    k.load_key('kraken.key')
    k.query_private('AddOrder', {'pair': 'XXBTZEUR',
                                 'type': 'buy',
                                 'ordertype': 'limit',
                                 'price': '938.75',
                                 'volume': '0.05',
                                 'close[pair]': 'XXBTZEUR',
                                 'close[type]': 'sell',
                                 'close[ordertype]': 'limit',
                                 'close[price]': '9001',
                                 'close[volume]': '1'})

    
def main(argv):
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)

    type = ''
    price = ''
    volume = ''
    try:
        opts,args = getopt.getopt(argv,"ht:p:v:",["type=","price=","vol="])
    except getopt.GetoptError:
        print 'kraken_query.py'
        sys.exit(2)
        for opt,arg in opts:
            if opt == '-h':
                print 'conditional-close.py -t <type> -p <price>'
    for opt, arg in opts:
        if opt == '-h':
            print 'conditional-close.py -t <type> -p <price>'
            sys.exit()
        elif opt in ("-t", "--type"):
            type = arg
        elif opt in ("-p", "--price"):
            price  = arg
        elif opt in ("-v", "--vol"):
            volume = arg


    print 'Sending query to Kraken - ','type:',type,'price:',price,' volume:',volume
    ret=send_query(type,price,volume)
    print ret
    
if __name__ == "__main__":
   main(sys.argv[1:])

   

