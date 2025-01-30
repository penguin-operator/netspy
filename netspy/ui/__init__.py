import sys
from .ui import ui

if sys.stdout.isatty(): from .tui import tui as ui
else: from .gui import gui as ui
