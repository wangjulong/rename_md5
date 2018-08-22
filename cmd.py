import argparse
from functions.rename import main

parser = argparse.ArgumentParser()
parser.add_argument('a', type=str, help='rename directory')
args = parser.parse_args()

main(args.a)
