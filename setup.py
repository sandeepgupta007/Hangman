import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages":["os","RandomWords","random","string"]}

setup( name="Hangman",
	version = "1.0",
	description = "A fun and recreational game!",
	executables = [Executable("hangman.py")])
