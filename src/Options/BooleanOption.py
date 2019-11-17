import json
import os

import tkinter as tk
from tkinter import ttk

class BoolOption:
	def __init__(self, name: str, parent_widget: ttk.Widget, json_conf: json):
		self.check_box_var = tk.IntVar()
		self.check_box_widget = ttk.Checkbutton(parent_widget, text = name, variable = self.check_box_var)
		self.frame = self.check_box_widget
		if "default_value" in json_conf and json_conf["default_value"]:
			self.check_box_var.set(1)	
		else:
			self.check_box_var.set(0)

	def retrieve_value(self):
		return self.check_box_var.get()