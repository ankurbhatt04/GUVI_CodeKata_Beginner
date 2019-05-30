try:
	n,q=list(map(int,input('Enter the value of n and q: ').strip().split(' ')))
	if(n>q):
		q,n=n,q
	if(n%2==0):
		for i in range(n+2,q,2):
			print(i,end=' ')
	else:
		for i in range(n+1,q,2):
			print(i,end=' ')
except:
	print('invalid')