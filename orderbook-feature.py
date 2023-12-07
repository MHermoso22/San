#.https://github.com/MHermoso22/San
#.장산, 이자용

import pandas as pd

mid_type = ''

def cal_mid_price (gr_bid_level, gr_ask_level):

    level = 5
    #gr_rB = gr_bid_level.head(level)
    #gr_rT = gr_ask_level.head(level)

    if len(gr_bid_level) > 0 and len(gr_ask_level) > 0:
        bid_top_price = gr_bid_level.iloc[0].price
        bid_top_level_qty = gr_bid_level.iloc[0].quantity
        ask_top_price = gr_ask_level.iloc[0].price
        ask_top_level_qty = gr_ask_level.iloc[0].quantity
        mid_price = (bid_top_price + ask_top_price) * 0.5 #what is mid price?

        return (mid_price)

    else:
        print ('Error: serious cal_mid_price')
        return (-1)


df = pd.read_csv('2023-11-15-upbit-BTC-trade.csv').apply(pd.to_numeric,errors='ignore')
groups = df.groupby('timestamp')

keys = groups.groups.keys()
for i in keys:
    gr_o = groups.get_group(i)
    gr_bid_level = gr_o[(gr_o.type == 0)]
    gr_ask_level = gr_o[(gr_o.type == 1)]
    print (gr_bid_level)
    print (gr_ask_level)
 
#. print (df)
    
    df.to_csv("./2023-11-15-upbit-btc-feature.csv", index=False, header=False, mode = 'a')

    #should_write_header = os.path.exists(fn)
    #if should_write_header == False:
    #    df.to_csv(fn, index=False, header=True, mode = 'a')
    #else:
    #    df.to_csv(fn, index=False, header=False, mode = 'a')

    break


