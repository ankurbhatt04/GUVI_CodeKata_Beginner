try:
	n,q=list(map(int,input('Enter the value of n and q: ').strip().split(' ')))
	if(n>q):
		q,n=n,q
	for i in range(n+1,q):
		f=0
		for j in range(2,int(i**0.5)+1):
			if(i%j==0):
				f=1
		if(f==0):
			print(i,end=' ')
except:
	print('invalid')