import json
import subprocess

import tkinter as tk
from tkinter import ttk

from OptionWrapper import OptionWrapper

class Script:
	def __init__(self, parent_widget: ttk.Widget, json_conf: json, category_options, row: int, nb_max_option: int):
		self.script_path = json_conf["script"]
		self.row = row
		self.category_options = category_options

		self._add_script_name(parent_widget, json_conf, row, nb_max_option)
		self._add_options(parent_widget, json_conf, row, nb_max_option)
		self._add_last_exec_result(parent_widget, json_conf, row, nb_max_option)
		self._add_execute_button(parent_widget, json_conf, row, nb_max_option)

		self.process = None
		

	def _add_script_name(self, parent_widget: ttk.Widget, json_conf: json, row: int, nb_max_option: int):
		self.label_name = ttk.Label(parent_widget, text = json_conf["name"])
		self.label_name.grid(column = 0, row = self.row, padx = 5, pady = 2, sticky = tk.E + tk.W + tk.N + tk.S)
		self.label_name.config(relief=tk.SOLID)

	def _add_options(self, parent_widget: ttk.Widget, json_conf: json, row: int, nb_max_option: int):
		self.options = []
		i = 1
		if "options" in json_conf:
			for option_description in json_conf["options"]:
				group = option_description["group"] if "group" in option_description else None
				option_with_group = self._find_wrapper_by_group(group) if group is not None else None
				if  option_with_group is None:
					new_option = OptionWrapper(parent_widget, option_description)
					new_option.frame.grid(column = i, row = self.row, padx = 5, pady = 2, sticky = tk.E + tk.W)
					self.options.append(new_option)
					i += 1
				else:
					option_with_group.add_option(option_description)
	
	def _find_wrapper_by_group(self, group: str):
		for option in self.options:
			if option.group == group:
				return option
		return None

	def _add_last_exec_result(self, parent_widget: ttk.Widget, json_conf: json, row: int, nb_max_option: int):
		self.last_exec_result = ttk.Label(parent_widget, text = "     ")
		self.last_exec_result.grid(column = nb_max_option + 1, row = self.row, padx = 5, pady = 2, sticky = tk.E + tk.W)
		self.last_exec_result.config(relief=tk.SOLID)

	def _add_execute_button(self, parent_widget: ttk.Widget, json_conf: json, row: int, nb_max_option: int):
		self.exec_button = ttk.Button(parent_widget, text = "Start", command = self.on_execute_button)
		self.exec_button.grid(column = nb_max_option + 2, row = self.row, padx = 5, pady = 2, sticky = tk.E + tk.W)

	def _update_last_exec_result(self, return_code):
		if return_code == 0:
			self.last_exec_result.configure(background = 'green')
		else:
			self.last_exec_result.configure(background = 'red')

	def _prepare_cmd(self):
		cmd = []
		cmd.append(self.script_path)
		for cat_opt in self.category_options:
			cmd += cat_opt.prepare_argument()
		for opt in self.options:
			cmd += opt.prepare_argument()
		return cmd

	def _execute(self, cmd):
		self.process = subprocess.Popen(cmd, shell=True)
		self.check_process_alive()

	def on_execute_button(self):
		if self.process is None:
			cmd = self._prepare_cmd()
			self._execute(cmd)
			self.exec_button.configure(text = "Stop")
		else:
			self.process.kill()
			self.process = None
			self._update_last_exec_result(1)
			self.exec_button.configure(text = "Start")
		
	def check_process_alive(self):
		if self.process is not None:
			if self.process.poll() is None:
				self.last_exec_result.after(100, self.check_process_alive)
			else:
				self._update_last_exec_result(self.process.returncode)
				self.process = None
				self.exec_button.configure(text = "Start")
