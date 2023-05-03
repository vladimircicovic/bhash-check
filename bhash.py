import bcrypt
import argparse
import os

parser = argparse.ArgumentParser(description='Compare each line from a file with given hash')
parser.add_argument('--filepath', type=str, help='Path to the wordlist.')
parser.add_argument('--hash', type=str, help='Blowfish hash for input.')

args = parser.parse_args()

if not os.path.isfile(args.filepath):
    print(f"Error: The file '{args.filepath}' does not exist.")
    exit(1)


with open(args.filepath, 'r') as file:
    for line in file:
        line = line.strip()
        if bcrypt.checkpw(line.encode('utf-8'), args.hash.encode('utf-8')):
              print("The password matches the hash!")
              print("Hash ", args.hash.strip(), " is ",line.strip())
              exit(0)

print("We did not find password ")
