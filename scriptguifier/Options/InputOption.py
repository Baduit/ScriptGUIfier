import json
import os
import subprocess

import tkinter as tk
from tkinter import ttk

class InputOption:
	def __init__(self, parent_widget, json_conf):
		self.literal = json_conf["literal"] if "literal" in json_conf else ""
		self.name = json_conf["name"] if "name" in json_conf else self.literal
		self.type = json_conf["type"]

		self.frame = ttk.Frame(parent_widget)

		self.label = ttk.Label(self.frame, text = self.name)
		self.label.grid(column = 0, row = 0, padx = 5, pady = 2, sticky = tk.E)

		self.input_value = tk.StringVar()
		self.input_widget = ttk.Entry(self.frame, textvariable = self.input_value)
		self.input_widget.grid(column = 1, row = 0, padx = 5, pady = 2, sticky = tk.W)
		self.input_value.set(self._extract_default_value(json_conf))

	def _extract_default_value(self, json_conf):
		if "default_value" in json_conf:
			return json_conf["default_value"]
		elif "default_value_from_env" in json_conf:
			return os.environ[json_conf["default_value_from_env"]]
		elif "default_value_from_script" in json_conf:
			return self._get_stdout_from_subprocess(json_conf["default_value_from_script"])
		else:
			return ""

	def _get_stdout_from_subprocess(self, process_name):
		process = subprocess.Popen(process_name, stdout=subprocess.PIPE, shell=True)
		stdout, _ = process.communicate()
		return stdout

	def retrieve_value(self):
		return self.input_value.get()