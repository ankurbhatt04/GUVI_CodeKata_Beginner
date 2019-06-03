try:
	n,a,d=list(map(int,input('Enter  N, A and D: ').strip().split()))
	last=a+(n-1)*d
	sum=(n*(a+last))//2
	print(sum)
except:
	print('invalid')