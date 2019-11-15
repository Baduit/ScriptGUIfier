#!/usr/bin/env python3

import json
import argparse

from GUI import GUI

def main():
	parser = argparse.ArgumentParser(description='Graphical user interface for YololTranslator')
	parser.add_argument('-c', '--config', default='./test_data/SimpleConf.json', help='Path of the config file')
	args = parser.parse_args()

	with open(args.config, "r") as read_file:
		conf = json.load(read_file)

	gui = GUI(conf)
	gui.main_loop()

if __name__ == "__main__":
	main()

