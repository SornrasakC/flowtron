""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
# from text import cmudict
# from pythainlp import thai_characters

_punctuation = '!\'",.:;? '
_math = '#%&*+-/[]()'
_special = '_@©°½—₩€$'
_accented = 'áçéêëñöøćž'
_numbers = '0123456789'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
# _arpabet = ['@' + s for s in cmudict.valid_symbols]

# 32
_thai_ipa = ['s', 'l', 'e', '3', 'j', 'i', 'o', 'z', 'v', 'n', 'w', 'q', 'g', 'a', 'm', 'c', 'h', 'x', 'f', '2', '4', 't', '@', '0', 'u', 'b', 'k', 'r', 'd', 'p', '1', '^']

# Export all symbols:
# 185 (engs syms/arpabet) + 88 (thai) = 273
# symbols = list(_punctuation + _math + _special + _accented + _numbers + _letters) + _arpabet + list(thai_characters)

# (39) + 88 = 127
# symbols = list(_punctuation + _math + _special + _numbers) + list(thai_characters)

# 101 (engs syms) + 1 (31 same symbol) (_thai_ipa) = 102
symbols = list(set( list(_punctuation + _math + _special + _accented + _numbers + _letters) + _thai_ipa ))
