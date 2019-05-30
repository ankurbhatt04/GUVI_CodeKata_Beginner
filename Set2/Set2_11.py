try:
	n,k=list(map(int,input('Enter value of n and k: ').strip().split()))
	result=n**k
	print(result)
except:
	print('invalid')