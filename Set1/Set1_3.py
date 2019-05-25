chr=input('Enter any character: ')
vowel=['a','e','i','o','u']
try:
	if(chr in vowel):
		print('Vowel')
	elif(chr.isalpha()):
		print('Consonant')
	else:
		print('invalid')
except:
	print('invalid')