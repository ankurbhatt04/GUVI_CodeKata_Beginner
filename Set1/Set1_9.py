try:
	n,k=list(map(int,input('Enter  the value of N and K: ').strip().split()))
	if(n<0 or k<0):
		print('invalid')
		
	ar=list(map(int,input('Enter  the value of aray elements: ').strip().split()))
	sum=0
	for i in range(0,k):
		sum+=ar[i]
	print(sum)
except:
	print('invalid')