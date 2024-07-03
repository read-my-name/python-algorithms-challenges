import websocket, json
import pandas as pd
import dateutil.parser
import datetime
from datetime import timedelta, datetime, date

minutes_processed = {}
minute_candlesticks = []
current_tick = None
previous_tick = None

def on_open(ws):
    print('opened connection')
    subscribe_message = {
        "type": "subscribe",
        "channels": [
            {
                "name": "ticker",
                "product_ids": [
                    "BTC-USD",
                ]
            }
        ]
    }
    ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
    global current_tick, previous_tick
    previous_tick = current_tick
    current_tick = json.loads(message) #converts string to dictionary
    
    print("===Received Tick===")
    print(f"Time: {current_tick['time']} @ Price:{current_tick['price']}" )

    tick_datetime_object = dateutil.parser.parse(current_tick['time'])
    timenow = tick_datetime_object + timedelta(hours=8) #convert to local time
    tick_dt = timenow.strftime("%Y-%m-%d %H:%M:%S")
    #print(tick_datetime_object.minute) #print minute
    print(tick_dt) #print local time

    if not tick_dt in minutes_processed:
        print("This is a new candlestick")
        minutes_processed[tick_dt] = True

        if len(minute_candlesticks) > 0:
            minute_candlesticks[-1]['close'] = previous_tick['price']

        minute_candlesticks.append({
            'minute': tick_dt,
            'open': current_tick['price'],
            'high': current_tick['price'],
            'low': current_tick['price'],
            })

        df = pd.DataFrame(minute_candlesticks[:-1])
        csv_path = r"python-algorithms-challenges/trading_system/bitcoin_data_tut.csv"
        
        # Save the data into csv file
        df.to_csv(csv_path, index=False)

    if len(minute_candlesticks) > 0:
        current_candlestick = minute_candlesticks[-1]
        if current_tick['price'] > current_candlestick['high']:
            current_candlestick['high'] = current_tick['price']
        if current_tick['price'] < current_candlestick['low']:
            current_candlestick['low'] = current_tick['price']

        print("== Candlesticks ==")
        # for candlestick in minute_candlesticks:
        #     print(candlestick)
        print(minute_candlesticks[0])

socket = 'wss://ws-feed.pro.coinbase.com'
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()




