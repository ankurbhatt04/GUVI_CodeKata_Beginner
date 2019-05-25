try:
	n=int(input('Enter a number: '))
	l=['Hello']*n
	for i in l:
		print(i)
except:
	print('invalid')