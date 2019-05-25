n=input('Enter a number: ')
try:
	num=int(n)
	if(not(num%2)):
		print('Even')
	else:
		print('Odd')
except:
	print('invalid')