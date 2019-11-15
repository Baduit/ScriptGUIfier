import tkinter as tk
from tkinter import ttk

from BooleanOption import BoolOption
from InputOption import InputOption
from ListOption import ListOption

class OptionWrapper:
	def __init__(self, parent_widget, json_conf):
		self.name = json_conf["name"]
		self.type = json_conf["type"]
		self.literal = json_conf["literal"]
		self.frame = ttk.Frame(parent_widget)
		
		process_good = True
		if self.type == 'boolean':
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