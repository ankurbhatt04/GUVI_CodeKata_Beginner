try:
	n,q=list(map(int,input('Enter the value of n and q: ').strip().split(' ')))
	if(n>q):
		q,n=n,q
	for i in range(n+1,q):
		temp=i
		sum=0
		while(temp!=0):
			sum+=(temp%10)**3
			temp=temp//10
		if(i==sum):
			print(i,end=' ')
except:
	print('invalid')