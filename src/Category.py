import json

import tkinter as tk
from tkinter import ttk

from Script import Script
from OptionWrapper import OptionWrapper

class Category:
	def __init__(self, parent_widget: ttk.Widget, json_conf: json):
		self.name = json_conf["name"]
		self.frame = ttk.Frame(parent_widget)

		self.options_frame = ttk.Frame(self.frame)
		self.options_frame.config(relief=tk.SOLID)
		self.options_frame.pack(expand = 1, fill = "both")

		self.scripts_frame = ttk.Frame(self.frame)
		self.scripts_frame.config(relief=tk.SOLID)
		self.scripts_frame.pack(expand = 1, fill = "both")

		self.nb_max_option = self._get_nb_max_option(json_conf["scripts"])

		self._create_options(json_conf)
		self._create_scripts(json_conf)

		self.frame.pack(expand = 1, fill = "both")
		
	def _get_nb_max_option(self, script_description_list):
		max = 0
		for script_description in script_description_list:
			options = script_description["options"] if "options" in script_description else []
			if len(options) > max:
				max = len(options)
		return max

	def _create_options(self, json_conf: json):
		self.options = []
		if "options" in json_conf:
			for i, option_description in enumerate(json_conf["options"]):
				new_option = OptionWrapper(self.options_frame, option_description)
				new_option.frame.grid(column = i, row = 0, padx = 5, pady = 2, sticky = tk.E + tk.W)
				self.options.append(new_option)
				pass
		pass

	def _create_scripts(self, json_conf: json):
		self.scripts = []
		for i, script_description in enumerate(json_conf["scripts"]):
			new_script = Script(self.scripts_frame, script_description, self.options, i, self.nb_max_option)
			self.scripts.append(new_script)
		