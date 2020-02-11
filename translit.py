#!/usr/bin/python3
import sys, argparse, configparser

parser = argparse.ArgumentParser(description='Transliteration using a particular set of rules.')
parser.add_argument('-i', '--ifile', type=argparse.FileType('r'), default=sys.stdin, help='input file (default: stdin)', metavar='FILE')
parser.add_argument('-o', '--ofile', type=argparse.FileType('w'), default=sys.stdout, help='output file (default: stdout)', metavar='FILE')
parser.add_argument('-r', '--rfile', type=argparse.FileType('r'), default='./default.rules', help='transliteration rules file (default: %(default)s)', metavar='FILE')
parser.add_argument('-v', '--version', action='version', version='%(prog)s v.1.00')

args=parser.parse_args()
rules = configparser.ConfigParser()
rules.optionxform = str
rules.read_file(args.rfile)

try:
    for str in args.ifile:
        for key in rules['DEFAULT']:
            str = str.replace(key, rules['DEFAULT'][key])
        args.ofile.write(str)
except(KeyboardInterrupt): pass
