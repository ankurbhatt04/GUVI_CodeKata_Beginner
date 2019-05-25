n=input('Enter a number: ')
try:
	n=int(n)
	if(n==0):
		print('Zero')
	elif(n>0):
		print('Positive')
	else:
		print('Negative')
except:
	print('Invalid Input')