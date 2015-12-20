#!/usr/bin/env python

import argparse
from time import sleep
from socket import gethostbyname
import sys

parser = argparse.ArgumentParser()
parser.add_argument("name", help="DNS name to test")
parser.add_argument("-c", "--count", help="set total count of resolves", type=int, default=100)
parser.add_argument("-d", "--delay", help="set delay between resolves in 1/100s of second", type=int, default=100)

args = parser.parse_args()

data = {}


def report(cycle):
    sys.stdout.write("\x1b[2J\x1b[H")
    print("==== %s ======== %d of %d ====" % (args.name, cycle, args.count))
    for ip in data:
        perc = data[ip] * 100.0 / cycle
        print("%16s [%20s %03.1f%%] %d" % (ip, "|" * int(perc / 5.0), perc, data[ip]))


for cycle in range(0, args.count):
    if cycle:
        sleep(args.delay / 100.0)
    ip = gethostbyname(args.name)
    if ip in data:
        data[ip] += 1
    else:
        data[ip] = 1
    report(cycle + 1)
