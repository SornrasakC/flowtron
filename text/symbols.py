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

# 54
_thai_ipa = ['ô', 'à', 'ŋ', 'h', 'á', 's', '́', '!', '̌', 'w', 'ǒ', 'û', 'ǎ', '̂', 'í', 'ì', 'y', 'ǐ', 'ǔ', 'î', 'c', 'ʉ', 'S', 'l', 'â', 'o', 'é', 't', 'n', 'A', 'ò', 'ɔ', 'a', 'ù', '̀', 'd', 'e', 
'f', 'I', 'k', 'm', 'i', 'r', 'P', 'è', 'ɛ', 'ě', 'b', 'ê', 'p', 'ə', 'ú', 'ó', 'u']

_thai_ipa_map = {
'ô': 'O1',
 'à': 'A1',
 'ŋ': 'N1',
 'h': 'H1',
 'á': 'A2',
 's': 'S1',
 '́': 'BL1',
 '!': '!',
 '̌': 'BL2',
 'w': 'W1',
 'ǒ': 'O2',
 'û': 'U1',
 'ǎ': 'A3',
 '̂': 'BL3',
 'í': 'I1',
 'ì': 'I2',
 'y': 'Y1',
 'ǐ': 'I3',
 'ǔ': 'U2',
 'î': 'I4',
 'c': 'C1',
 'ʉ': 'U3',
 'S': 'S2',
 'l': 'L1',
 'â': 'A4',
 'o': 'O3',
 'é': 'E1',
 't': 'T1',
 'n': 'N2',
 'A': 'A5',
 'ò': 'O4',
 'ɔ': 'C2',
 'a': 'A6',
 'ù': 'U4',
 '̀': 'BL4',
 'd': 'D1',
 'e': 'E2',
 'f': 'F1',
 'I': 'I5',
 'k': 'K1',
 'm': 'M1',
 'i': 'I6',
 'r': 'R1',
 'P': 'P1',
 'è': 'E3',
 'ɛ': 'E4',
 'ě': 'E5',
 'b': 'B1',
 'ê': 'E6',
 'p': 'P2',
 'ə': 'E7',
 'ú': 'U5',
 'ó': 'O5',
 'u': 'U6'
 }

_thai_ipa_mapped = ['@' + s for s in _thai_ipa_map.values()]

# Export all symbols:
# 185 (engs syms) + 88 (thai) = 273
# symbols = list(_punctuation + _math + _special + _accented + _numbers + _letters) + _arpabet + list(thai_characters)

# (39) + 88 = 127
# symbols = list(_punctuation + _math + _special + _numbers) + list(thai_characters)

# 93
symbols = list(set( list(_punctuation + _math + _special + _numbers) + _thai_ipa_mapped ))