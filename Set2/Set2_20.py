try:
	n=int(input('Enter a number: ').strip())
	for i in range(1,6):
		print(i*n,end=' ')
except:
	print('invalid')