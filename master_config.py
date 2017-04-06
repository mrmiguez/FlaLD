"""
# FlaLD CONTROL VARIABLES
#
# CONFIG_DICT is the list of expected repox exports and requisite mappings
#   Keys are shortened forms of repox export directories.
#       They will be expanded by runFlaLD using glob.glob(key*), so full names aren't required.
#       They should be relatively descriptive to avoid collision with other sets.
#   Values are the OAI metadata format mappings.
#       Currently only 'dc', 'qdc', and 'mods' are supported.
"""

CONFIG_DICT = { 'umiami': 'qdc',
                'fiu': 'dc',
                'fsu': 'mods' }