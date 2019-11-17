import json

import tkinter as tk
from tkinter import ttk

from Script import Script

class Category:
	def __init__(self, parent_widget: ttk.Widget, json_conf: json):
		self.name = json_conf["name"]
		self.frame = ttk.Frame(parent_widget)
		self.nb_max_option = self._get_nb_max_option(json_conf["scripts"])

		self._create_scripts(json_conf)
		
	def _get_nb_max_option(self, script_description_list):
		max = 0
		for script_description in script_description_list:
			options = script_description["options"] if "options" in script_description else []
			if len(options) > max:
				max = len(options)
		return max

	def _create_scripts(self, json_conf: json):
		self.scripts = []
		for i, script_description in enumerate(json_conf["scripts"]):
			new_script = Script(self.frame, script_description, i, self.nb_max_option)
			self.scripts.append(new_script)
		