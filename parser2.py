import re
import json
import os

def parse_log_file(filename):
    with open(filename, 'r') as f:
        for line in f:
            try:
                # Extract the JSON data from the log line
                match = re.search(r'\s*(\d+)\s*-\s*(\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2})-\s*-\s*(.*)', line)
                if match:
                    timestamp = match.group(2)
                    json_data = match.group(3)

                    # Parse the JSON data into a dictionary
                    try:
                        data = json.loads(json_data)
                    except json.decoder.JSONDecodeError:
                        print(f"Invalid JSON data: {json_data}")
                        continue

                    # Extract specific data from the dictionary
                    event_type = data['e']
                    event_time = data['E']
                    symbol = data['s']
                    price = data['p']

                    # Process the extracted data
                    print(f"Event type: {event_type}")
                    print(f"Event time: {event_time}")
                    print(f"Symbol: {symbol}")
                    print(f"Price: {price}")
                    print("--------------------------------------------------------")

            except Exception as e:
                print(f"Error processing line: {line}")
                print(f"Error message: {e}")
                print("--------------------------------------------------------")

def parse_files_in_directory(directory, file_extension='.log'):
    for filename in os.listdir(directory):
        if filename.endswith(file_extension):
            filepath = os.path.join(directory, filename)
            parse_log_file(filepath)

if __name__ == '__main__':
    # Specify the base directory containing the log files
    base_directory = 'currency_logs'

    # Parse log files in all subdirectories
    for directory in os.listdir(base_directory):
        if os.path.isdir(os.path.join(base_directory, directory)):
            parse_files_in_directory(os.path.join(base_directory, directory))


        parse_files_in_directory('currency_logs/Perpetual_currency_logs/XRPUSDT', file_extension='.log.YYYY-MM-DD')