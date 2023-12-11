import re
import json

def parse_log_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            # Extract the JSON data from the log line
            match = re.search(r'\s*(\d+)\s*-\s*(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})-\s*-\s*(.*)', line)
            if match:
                timestamp = match.group(2)
                json_data = match.group(3)

                # Parse the JSON data into a dictionary
                data = json.loads(json_data)

                # Extract specific data from the dictionary
                event_type = data['e']
                event_time = data['E']
                symbol = data['s']
                price = data['p']
                percentage_change = data['P']
                weighted_average_price = data['w']
                close = data['c']
                quantity_traded = data['Q']
                open_price = data['o']
                high_price = data['h']
                low_price = data['l']
                volume = data['v']
                quote_volume = data['q']
                open_time = data['O']
                close_time = data['C']
                first_trade_id = data['F']
                last_trade_id = data['L']
                number_of_trades = data['n']

                # Process the extracted data
                # print(f"Timestamp: {timestamp}")
                print(f"Event type: {event_type}")
                print(f"Event time: {event_time}")
                print(f"Symbol: {symbol}")
                print(f"Price: {price}")
                # print(f"Percentage change: {percentage_change}")
                # print(f"Weighted average price: {weighted_average_price}")
                # print(f"Close: {close}")
                # print(f"Quantity traded: {quantity_traded}")
                # print(f"Open price: {open_price}")
                # print(f"High price: {high_price}")
                # print(f"Low price: {low_price}")
                # print(f"Volume: {volume}")
                # print(f"Quote volume: {quote_volume}")
                print(f"Open time: {open_time}")
                print(f"Close time: {close_time}")
                # print(f"First trade ID: {first_trade_id}")
                # print(f"Last trade ID: {last_trade_id}")
                # print(f"Number of trades: {number_of_trades}")
                print("--------------------------------------------------------")

# Specify the log file to parse
filename = 'currency_logs/Perpetual_currency_logs/BTCUSDT'

# Parse the log file
parse_log_file(filename)
