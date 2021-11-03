import json
import subprocess
import os

import tkinter as tk
from tkinter import ttk

from Category import Category

class GUI:
	def __init__(self, json_conf):
		self.form = tk.Tk()
		self.set_name(json_conf["app_name"])

		self.categories = []
		self.notebook = ttk.Notebook(self.form)
		for category_description in json_conf["categories"]:
			new_category = Category(self.notebook, category_description)
			self.notebook.add(new_category.frame, text = new_category.name)
			self.categories.append(new_category)
			
		self.notebook.pack(expand = 1, fill = "both")

	def get_name(self):
		return self._name

	def set_name(self, name):
		self._name = name
		self.form.winfo_toplevel().title(self._name)
		
	def main_loop(self):
		self.form.mainloop()
