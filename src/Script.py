import json
import subprocess

import tkinter as tk
from tkinter import ttk

from OptionWrapper import OptionWrapper

class Script:
	def __init__(self, parent_widget, json_conf, row, nb_max_option):
		self.script_path = json_conf["script"]
		self.row = row
		self.label_name = ttk.Label(parent_widget, text = json_conf["name"])
		self.label_name.grid(column = 0, row = self.row, padx = 5)

		self.options = []
		i = 1
		if "options" in json_conf:
			for option_description in json_conf["options"]:
				new_option = OptionWrapper(parent_widget, option_description)
				new_option.frame.grid(column = i, row = self.row, padx = 5)
				self.options.append(new_option)
				i += 1

		self.exec_button = ttk.Button(parent_widget, text = "Start", command = self.execute)
		self.exec_button.grid(column = nb_max_option + 1, row = self.row, padx = 5)

	def execute(self):
		cmd = []
		cmd.append(self.script_path)
		for opt in self.options:
			if opt.type == 'boolean':
				if opt.retrieve_value():
					cmd.append(opt.literal)
			elif opt.type == 'string' or opt.type == 'path' or opt.type == 'combo_box':
				retrieved_value = opt.retrieve_value()
				if retrieved_value != '':
					if opt.literal != "":
						cmd.append(opt.literal)
					cmd.append(retrieved_value)
			else:
				pass # Not supposed to happend. Log? Throw? Show an image with cute kittens?
		subprocess.Popen(cmd, shell=True)