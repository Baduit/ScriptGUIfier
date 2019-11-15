import tkinter as tk
from tkinter import ttk

from Options.BooleanOption import BoolOption
from Options.InputOption import InputOption
from Options.ListOption import ListOption

class OptionWrapper:
	def __init__(self, parent_widget, json_conf):
		self.literal = json_conf["literal"] if "literal" in json_conf else ""
		self.name = json_conf["name"] if "name" in json_conf else self.literal
		self.type = json_conf["type"]
		self.frame = ttk.Frame(parent_widget)
		
		process_good = True
		if self.type == 'boolean':
			if self.literal == "":
				raise AssertionError("A boolean option MUST have a literal")
			self.option = BoolOption(self.name, self.frame, json_conf)
		elif self.type == 'string' or self.type == 'path':
			self.option = InputOption(self.name, self.frame, json_conf)
		elif self.type == 'combo_box':
			self.option = ListOption(self.name, self.frame, json_conf)
		else:
			process_good = False
			print("Option: " + self.name + " unknown option type: " + self.type)
		
		if process_good:
			self.option.frame.grid(column = 0, row = 0, padx = 5)

	def retrieve_value(self):
		return self.option.retrieve_value()