import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

# storage_filename = os.path.join(tempfile.gettempdir(), "storage.data")
storage_filename = "storage.data"

print(args.key)
print(args.value)
print(storage_filename)

data = {}

if args.key and args.value:
    data[args.key] = data.get(args.key, []) + [args.value]
    print(data)
    with open(storage_filename, "w+") as f:
        json.dump(data, f)

if not args.value:
    with open(storage_filename, "r") as f:
        data = json.load(f)
        print(data)
"""
def main():
    print("Script output")


if __name__ == "__main__":
    main()
"""
