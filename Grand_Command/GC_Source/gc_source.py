
# General info , random, time, os, sys
try:
    from gc_source_module import *
except ImportError:
    print('Unable to import gc_source_mod')

# Screen Size Data
try:
    from gc_window import *
except ImportError:
    print('Unable to import gc_window')

# Contains fonts
try:
    from gcfonts import *
except:
    print('Unable to import gcfonts')


# Draws all the tiles
try:
    from gc_tileinfo import *
except ImportError:
    print('Unable to import tileinfo')

# Loading the images
try:
    from gc_loadimg import *
except ImportError:
    print('Unable to import gc_loadimg')

try:
    from gc_shorten import *
except ImportError:
    print('Unable to import gc_shorten')

# Contains Prestige Count, Multipliers for Prestige, Map Level, & Background Music
try:
    from gc_global_info import *
except ImportError:
    print('Unable to import gc_global_info')




