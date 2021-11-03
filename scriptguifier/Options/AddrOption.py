import json
import os
import subprocess
import sys

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
from tkinter.filedialog import askdirectory

if sys.platform == "win32":
	ping_option = "-n"
else: # I assume that the ping command works the same way as the Linux one in every other plaform
	ping_option = "-c"

class AddrOption:
	def __init__(self, parent_widget, json_conf):
		self.literal = json_conf["literal"] if "literal" in json_conf else ""
		self.name = json_conf["name"] if "name" in json_conf else self.literal
		self.type = json_conf["type"]

		self.frame = ttk.Frame(parent_widget)
		self.path_type = json_conf["path_type"] if "path_type" in json_conf else "files"

		self.label = ttk.Label(self.frame, text = self.name)
		self.label.grid(column = 0, row = 0, padx = 5, pady = 2, sticky = tk.E + tk.W)

		self.input_value = tk.StringVar()
		self.input_widget = ttk.Entry(self.frame, textvariable = self.input_value)
		self.input_widget.grid(column = 1, row = 0, padx = 5, pady = 2)
		self.input_value.set(self._extract_default_value(json_conf))

		self.ping_result_label = ttk.Label(self.frame, text = "     ")
		self.ping_result_label.grid(column = 2, row = 0, padx = 5, pady = 2, sticky = tk.E + tk.W)
		self.ping_result_label.config(relief=tk.SOLID)
		
		self.frame.after(500, self._ping)
		self.ping_process = None
		

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

	def _ping(self):
		if self.ping_process is None:
			self.ping_process = subprocess.Popen(["ping", ping_option, "1", self.retrieve_value()], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
		else:
			if self.ping_process.poll() is not None:
				if self.ping_process.returncode == 0: 
					self.ping_result_label.configure(background = 'green')
				else:
					self.ping_result_label.configure(background = 'red')
				self.ping_process = None
		self.frame.after(500, self._ping)

	def retrieve_value(self):
		return self.input_value.get()