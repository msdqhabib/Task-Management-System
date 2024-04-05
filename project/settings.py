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

# # development_settings_file = os.path.join(BASE_DIR, 'development.py')
# development_settings_file = os.path.join(BASE_DIR, 'development.py')

# print(f'development_settings_file - {development_settings_file}')
# isfileexist = os.path.exists(development_settings_file)
# print(f'isfileexist - {isfileexist}')


if isDevelopmentExists:
    include('development.py')
else:
    include('production.py')
