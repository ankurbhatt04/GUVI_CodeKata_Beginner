chr=input('Enter a charcter: ')
try:
	if(chr.isalpha()):
		prnit('Alphabet')
	else:
		print('No')
except:
	print('invalid')