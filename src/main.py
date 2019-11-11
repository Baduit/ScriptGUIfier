#!/usr/bin/env python3

import json

import tkinter as tk
from tkinter import ttk

class InputOption:
	def __init__(self, name, parent_widget, default_input_text):
		self.frame = ttk.Frame(parent_widget)
		self.label = ttk.Label(self.frame, text = name)
		self.label.grid(column = 0, row = 0, padx = 5)
		self.input_value = tk.StringVar()
		self.input_widget = ttk.Entry(self.frame, textvariable = self.input_value)
		self.input_widget.grid(column = 1, row = 0, padx = 5)
		self.input_value.set(default_input_text)

	def retrieve_value(self):
		return self.input_value.get()

class BoolOption:
	def __init__(self, name, parent_widget, default_value):
		self.check_box_var = tk.IntVar()
		self.check_box_widget = ttk.Checkbutton(parent_widget, text = name, variable = self.check_box_var)
		self.frame = self.check_box_widget
		if default_value:
			self.check_box_var.set(1)	
		else:
			self.check_box_var.set(0)

	def retrieve_value(self):
		return self.check_box_var.get()

class OptionWrapper:
	def __init__(self, parent_widget, json_conf):
		self.name = json_conf["name"]
		self.type = ''
		self.literal = ''
		self.frame = ttk.Frame(parent_widget)
		
		process_good = True
		option_type = json_conf["type"]
		if option_type == 'boolean':
			self.option = BoolOption(self.name, self.frame, json_conf["default_value"])
		elif option_type == 'string' or option_type == 'path':
			self.option = InputOption(self.name, self.frame, json_conf["default_value"])
		else:
			process_good = False
			print("Option: " + self.name + " unknown option type: " + option_type)
		
		if process_good:
			self.option.frame.grid(column = 0, row = 0, padx = 5)

class Script:
	def __init__(self, parent_widget, json_conf, row, nb_max_option):
		self.script_path = json_conf["script"]
		self.row = row
		self.label_name = ttk.Label(parent_widget, text = json_conf["name"])
		self.label_name.grid(column = 0, row = self.row, padx = 5)

		self.options = []
		i = 1
		for option_description in json_conf["options"]:
			new_option = OptionWrapper(parent_widget, option_description)
			new_option.frame.grid(column = i, row = self.row, padx = 5)
			self.options.append(new_option)
			i += 1

		self.exec_button = ttk.Button(parent_widget, text = "Start")
		self.exec_button.grid(column = nb_max_option + 1, row = self.row, padx = 5)

	def execute(self):
		pass

class Category:
	def __init__(self, parent_widget, json_conf):
		self.name = json_conf["name"]
		self.frame = ttk.Frame(parent_widget)

		nb_max_option = self._get_nb_max_option(json_conf["scripts"])
		self.scripts = []
		for i, script_description in enumerate(json_conf["scripts"]):
			new_script = Script(self.frame, script_description, i, nb_max_option)
			self.scripts.append(new_script)
	
	def _get_nb_max_option(self, script_description_list):
		max = 0
		for script_description in script_description_list:
			options = script_description["options"]
			if len(options) > max:
				max = len(options)
		return max


class GUI:
	def __init__(self, json_conf):
		self.form = tk.Tk()
		self.form.geometry("800x280")
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

def main():
	with open("./test_data/SimpleConf.json", "r") as read_file:
		conf = json.load(read_file)

	gui = GUI(conf)
	gui.main_loop()

if __name__ == "__main__":
	main()

