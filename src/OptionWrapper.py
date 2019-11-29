import json

import tkinter as tk
from tkinter import ttk

from Options.BooleanOption import BoolOption
from Options.InputOption import InputOption
from Options.ListOption import ListOption
from Options.PathOption import PathOption

class OptionWrapper:
	def __init__(self, parent_widget: ttk.Widget, json_conf: json):
		self.frame = ttk.Frame(parent_widget)
		self.frame.config(relief=tk.SOLID)
		
		self.add_option(json_conf)
	
	def add_option(self, json_conf: json):
		process_good = True
		literal = json_conf["literal"] if "literal" in json_conf else ""
		if json_conf["type"] == 'boolean':
			if literal == "":
				raise AssertionError("A boolean option MUST have a literal")
			self.option = BoolOption(self.frame, json_conf)
		elif json_conf["type"] == 'string':
			self.option = InputOption(self.frame, json_conf)
		elif json_conf["type"] == 'path':
			self.option = PathOption(self.frame, json_conf)
		elif json_conf["type"] == 'combo_box':
			self.option = ListOption(self.frame, json_conf)
		else:
			process_good = False
			print("Option: " + self.option.name + " unknown option type: " + json_conf["type"])
		
		if process_good:
			self.option.frame.grid(column = 0, row = 0, padx = 5, pady = 2)

	def retrieve_value(self):
		return self.option.retrieve_value()

	def prepare_argument(self):
		arg = []
		if self.option.type == 'boolean':
			if self.retrieve_value():
				arg.append(self.option.literal)
		elif self.option.type == 'string' or self.option.type == 'path' or self.option.type == 'combo_box':
			retrieved_value = self.retrieve_value()
			if retrieved_value != '':
				if self.option.literal != "":
					arg.append(self.option.literal)
				arg.append(retrieved_value)
		else:
			pass # Not supposed to happend. Log? Throw? Show an image with cute kittens?
		return arg