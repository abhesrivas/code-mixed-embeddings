# import pandas as pd
import unicodedata

""" Normalise (normalize) unicode data in Python to remove umlauts, accents etc. """
# df = pd.read_csv("frequent_hindi.csv")
# words = list(df['Roman Words'])

words = open("frequent_useful.txt").read().split('\n')

words = list(sorted(set(words)))

with open('frequent_set_words.txt', 'wb',) as f:
	for word in words:
		normal = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore')
		f.write(normal+b'\n')