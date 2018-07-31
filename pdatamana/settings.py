# If you're deploying then create a new file settings_production.py and
# change settings_devel to settings_production.

try:
    from settings_devel import *
except ImportError:
    pass
