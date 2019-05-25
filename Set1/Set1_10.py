try:
	n=input('Enter a number: ')
	leng=len(n)
	n=int(n)
	if((n//(10**leng))==(-1)):
		print(leng-1)
	else:	
		print(leng)
except:
	print('invalid')