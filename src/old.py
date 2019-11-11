import json

import tkinter as tk
from tkinter import ttk

# Rework tout ça en plus objet je m'y retrouverai mieux je pense

def create_option_frame(frame, option_configuration):
	if option_configuration["type"] == "boolean":
		option_frame = ttk.Checkbutton(frame)
	else:
		option_frame = ttk.Label(frame, text = option_configuration["name"])
	return option_frame

def create_script_frame(frame, script_configuration):
	script_frame = ttk.Frame(frame)
	name_label = ttk.Label(script_frame, text = script_configuration["name"])
	name_label.grid(column = 0, row = 0)
	for option_index, new_option in enumerate(script_configuration["options"]):
		new_option_label = create_option_frame(script_frame, new_option)
		new_option_label.grid(column = 1 + option_index, row = 0)
	return script_frame

def create_category_frame(frame, category_configuration):
	category_frame = ttk.Frame(frame)
	frame.add(category_frame, text = category_configuration["name"])

	for script_index, new_script in enumerate(category_configuration["scripts"]):
		script_frame = create_script_frame(category_frame, new_script)
		script_frame.grid(row = script_index)

def create_notebook(main_form, configuration):
	tab_parent = ttk.Notebook(main_form)

	for new_category in configuration["categories"]:
		create_category_frame(tab_parent, new_category)

	tab_parent.pack(expand = 1, fill = "both")

def create_GUI(configuration):
	main_form = tk.Tk()
	main_form.winfo_toplevel().title(configuration["app_name"])
	main_form.geometry("500x280")

	create_notebook(main_form, configuration)

	return main_form

with open("./test_data/SimpleConf.json", "r") as read_file:
    conf = json.load(read_file)

gui = create_GUI(conf)
gui.mainloop()