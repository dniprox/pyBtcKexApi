#!/usr/bin/env python2

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

    type_order = 'buy'
    price = ''
    volume = ''
    leverage = '5'

    def pringHelp():
        print 'buy-order.py -p <price> -v <volume>'
        
    try:
        opts, args = getopt.getopt(argv,"hp:v",["help","price=","volume="])
        print "opts:",opts
        print "arg:",args
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
            #print "price:",arg
            price  = arg
        elif opt in ("-v", "--vol"):
            volume = arg
            #print "vol:",arg
        elif opt in ("-l", "--lev"):
            leverage = arg
        else:
            assert False, "Unhandled option"
            
    print 'Price:',price, ' Volume:',volume, ' Leverage:',leverage

    if volume == '':
        print "Volumen not set"
        return 1
    
    ret = send_query(type_order,price,volume,5)
    print "Buy Order Done Leverage 5:",ret
    
if __name__ == "__main__":
    main(sys.argv[1:])

   

