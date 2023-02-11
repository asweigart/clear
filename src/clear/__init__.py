"""clear
By Al Sweigart al@inventwithpython.com
Special thanks to David George for allowing me to use the Clear name on PyPI.

A cross-platform Python module that provides a clear() function which clears the terminal. That's all.

This function runs the one-liner: os.system('cls' if os.name == 'nt' else 'clear')

This module exists as a simpler alternative to defining this function on your own."""

__version__ = '2.0.0'

import os

def clear():
	"""Clears the terminal screen by running cls (on Windows) or clear (on macOS/Linux)."""
	os.system('cls' if os.name == 'nt' else 'clear')
