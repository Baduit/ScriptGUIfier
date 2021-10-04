#!/usr/bin/env python3

import time
import argparse

parser = argparse.ArgumentParser(description='Graphical user interface for YololTranslator')
parser.add_argument('-e', '--endpoint', default='https://yololtranslate-api.baduit.eu/translate', help='The address of the Yolol Translator API used. The default address is the official API.')
parser.add_argument('-o', '--other', default='Blablabla', help='kk')
parser.add_argument('-p', '--pretty', action='store_true', help='Enable pretty logs (add colors)')
args = parser.parse_args()

if args.pretty:
	print("The endpoint is", args.endpoint)
else:
	print("This is not pretty :'(", args.other)

time.sleep(5)

""" while True:
	pass """