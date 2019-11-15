import json
import os

import tkinter as tk
from tkinter import ttk

class ListOption:
	def __init__(self, name, parent_widget, json_conf):
		self.frame = ttk.Frame(parent_widget)

		self.label = ttk.Label(self.frame, text = name)
		self.label.grid(column = 0, row = 0, padx = 5)

		self.combo_box = ttk.Combobox(self.frame)
		self.combo_box.grid(column = 1, row = 0, padx = 5)
		self.combo_box['values'] = json_conf["values"]
		self.combo_box.current(0)

	def retrieve_value(self):
		return self.combo_box.get()