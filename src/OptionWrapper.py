import json

import tkinter as tk
from tkinter import ttk

from Options.BooleanOption import BoolOption
from Options.InputOption import InputOption
from Options.ListOption import ListOption
from Options.PathOption import PathOption
from Options.AddrOption import AddrOption

class OptionWrapper:
	def __init__(self, parent_widget: ttk.Widget, json_conf: json):
		self.frame = ttk.Frame(parent_widget)
		self.frame.config(relief=tk.SOLID)
		self.group = json_conf["group"] if "group" in json_conf else None
		self.options = []
		
		self.add_option(json_conf)
	
	def add_option(self, json_conf: json):
		process_good = True
		literal = json_conf["literal"] if "literal" in json_conf else ""
		if json_conf["type"] == 'boolean':
			if literal == "":
				raise AssertionError("A boolean option MUST have a literal")
			option = BoolOption(self.frame, json_conf)
		elif json_conf["type"] == 'string':
			option = InputOption(self.frame, json_conf)
		elif json_conf["type"] == 'path':
			option = PathOption(self.frame, json_conf)
		elif json_conf["type"] == 'combo_box':
			option = ListOption(self.frame, json_conf)
		elif json_conf["type"] == 'ip_addr':
			option = AddrOption(self.frame, json_conf)
		else:
			process_good = False
			print("Option: " + literal + " unknown option type: " + json_conf["type"])
		
		if process_good:
			option.frame.grid(column = 0, row = len(self.options), padx = 5, pady = 2, sticky = tk.E + tk.W)
			self.options.append(option)

	def prepare_argument(self):
		arg = []
		for option in self.options:
			if option.type == 'boolean':
				if option.retrieve_value():
					arg.append(option.literal)
			elif option.type == 'string' or option.type == 'path' or option.type == 'combo_box' or option.type == 'ip_addr':
				retrieved_value = option.retrieve_value()
				if retrieved_value != '':
					if option.literal != "":
						arg.append(option.literal)
					arg.append(retrieved_value)
			else:
				pass # Not supposed to happend. Log? Throw? Show an image with cute kittens?
		return arg