import json
import os
import subprocess

import tkinter as tk
from tkinter import ttk

class ListOption:
	def __init__(self, parent_widget, json_conf: json):
		self.literal = json_conf["literal"] if "literal" in json_conf else ""
		self.name = json_conf["name"] if "name" in json_conf else self.literal
		self.type = json_conf["type"]

		self.frame = ttk.Frame(parent_widget)

		self.label = ttk.Label(self.frame, text = self.name)
		self.label.grid(column = 0, row = 0, padx = 5, pady = 2, sticky = tk.E + tk.W)

		self.combo_box = ttk.Combobox(self.frame)
		self.combo_box.grid(column = 1, row = 0, padx = 5, pady = 2, sticky = tk.E + tk.W)
		self.combo_box['values'] = self._extract_default_value(json_conf)
		self.combo_box.current(0)

	def _extract_default_value(self, json_conf: json):
		if "values" in json_conf:
			return json_conf["values"]
		elif "values_from_env" in json_conf:
			splitted = os.environ[json_conf["values_from_env"]].split(';')
			splitted.remove('')
			return splitted
		elif "values_from_script" in json_conf:
			splitted = self._get_stdout_from_subprocess(json_conf["values_from_script"]).decode().split('\n')
			splitted.remove('')
			return splitted
		else:
			return ""

	def _get_stdout_from_subprocess(self, process_name):
		process = subprocess.Popen(process_name, stdout=subprocess.PIPE, shell=True)
		stdout, _ = process.communicate()
		return stdout

	def retrieve_value(self):
		return self.combo_box.get()