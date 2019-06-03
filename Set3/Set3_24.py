try:
	n=int(input('Enter  N: ').strip())
	arr=list(map(int,input('Enter array elements: ').strip().split()))
	arr.sort()
	for i in arr:
		print(i,end=' ')
except:
	print('invalid')