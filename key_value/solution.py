import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

# storage_filename = os.path.join(tempfile.gettempdir(), "storage.data")
# path = os.path.dirname(os.path.abspath(__file__))

def get_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            data = json.load(f)
    else:
        data = {}
    return data

def write_values(data, key, value):
    data[args.key] = data.get(args.key, []) + [args.value]
    with open(storage_filename, "w") as f:
        json.dump(data, f)

def get_values(data, key):
    if args.key in data:
        return data[args.key]

def print_values(val):
    if val:     
        return ", ".join(val)

if __name__ == "__main__":
    storage_filename = os.path.join(tempfile.gettempdir(), "storage.data")
    data = get_data(storage_filename)
    if args.key and args.value:
        write_values(data, args.key, args.value)
    elif args.key and not args.value:
        output = get_values(data, args.key)
        print(print_values(output))