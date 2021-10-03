""" from https://github.com/keithito/tacotron """

'''
Defines the set of symbols used in text input to the model.

The default is a set of ASCII characters that works well for English or text that has been run through Unidecode. For other data, you can modify _characters. See TRAINING_DATA.md for details. '''
from text import cmudict
from pythainlp import thai_characters

_punctuation = '!\'",.:;? '
_math = '#%&*+-/[]()'
_special = '_@©°½—₩€$'
_accented = 'áçéêëñöøćž'
_numbers = '0123456789'
_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# Prepend "@" to ARPAbet symbols to ensure uniqueness (some are the same as uppercase letters):
_arpabet = ['@' + s for s in cmudict.valid_symbols]

# 54
_thai_ipa = ['ô', 'à', 'ŋ', 'h', 'á', 's', '́', '!', '̌', 'w', 'ǒ', 'û', 'ǎ', '̂', 'í', 'ì', 'y', 'ǐ', 'ǔ', 'î', 'c', 'ʉ', 'S', 'l', 'â', 'o', 'é', 't', 'n', 'A', 'ò', 'ɔ', 'a', 'ù', '̀', 'd', 'e', 
'f', 'I', 'k', 'm', 'i', 'r', 'P', 'è', 'ɛ', 'ě', 'b', 'ê', 'p', 'ə', 'ú', 'ó', 'u']

# Export all symbols:
# 185 (engs syms) + 88 (thai) = 273
# symbols = list(_punctuation + _math + _special + _accented + _numbers + _letters) + _arpabet + list(thai_characters)

# (39) + 88 = 127
# symbols = list(_punctuation + _math + _special + _numbers) + list(thai_characters)

# 179
symbols = list(set( list(_punctuation + _math + _special + _numbers) + list(thai_characters) + _thai_ipa ))