try:
	n=int(input('Enter  N: ').strip())
	arr=list(map(int,input('Enter  N: ').strip().split()))
	maxm=max(arr)
	print(maxm)
except:
	print('invalid')