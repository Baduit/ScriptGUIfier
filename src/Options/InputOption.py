import json
import os

import tkinter as tk
from tkinter import ttk

class InputOption:
	def __init__(self, name, parent_widget, json_conf):
		self.frame = ttk.Frame(parent_widget)

		self.label = ttk.Label(self.frame, text = name)
		self.label.grid(column = 0, row = 0, padx = 5)

		self.input_value = tk.StringVar()
		self.input_widget = ttk.Entry(self.frame, textvariable = self.input_value)
		self.input_widget.grid(column = 1, row = 0, padx = 5)
		self.input_value.set(self._extract_default_value(json_conf))

	def _extract_default_value(self, json_conf):
		if "default_value" in json_conf:
			return json_conf["default_value"]
		elif "default_value_from_env" in json_conf:
			return os.environ[json_conf["default_value_from_env"]]
		else:
			return ""

	def retrieve_value(self):
		return self.input_value.get()