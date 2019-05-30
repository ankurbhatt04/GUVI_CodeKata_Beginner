try:
	n=int(input('Enter a number: ').strip())
	fact=1
	while(n>1):
		fact*=n
		n=n-1
	print(fact)
except:
	print('invalid')