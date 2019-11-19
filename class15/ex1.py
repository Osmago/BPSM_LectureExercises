#!bin/usr/python3

import re

accs = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

searchfor = [r'5', r'[de]', r'de', r'd.e', r'^[xy]' , r'^[xy].*e$', r'\d{3,}', r'd[arp]']

for acc in accs:
	print (acc)
	for what in searchfor:
		if re.search(what, acc):
			print("\tfound ", what)
	if re.search('d', acc) and re.search('e', acc):
		print ("\tfound d and e")
	print()
