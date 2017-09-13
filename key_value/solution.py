import argparse
import json
import os
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("--key",)
# parser.add_argument("--value")
args = parser.parse_args()

storage_filename = os.path.join(tempfile.gettempdir(), "storage.data")

print(args.key)
print(storage_filename)
# with open(storage_filename, "w") as f:
#    f.write(args.key + "\n")

"""
def main():
    print("Script output")


if __name__ == "__main__":
    main()
"""
