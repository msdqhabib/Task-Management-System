from split_settings.tools import optional, include
from pathlib import Path
import os

try:
    from . import development
    isDevelopmentExists = True
except:
    isDevelopmentExists = False


BASE_DIR = Path(__file__).resolve().parent.parent

# Include the base settings file
include('base.py')


# Check if development.py exists

if isDevelopmentExists:
    include('development.py')
else:
    include('production.py')
