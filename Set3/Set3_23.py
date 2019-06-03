try:
	n=int(input('Enter  N: ').strip())
	arr=list(map(int,input('Enter  N: ').strip().split()))
	minm=min(arr)
	print(minm)
except:
	print('invalid')