try:
	n=int(input('Enter  N: ').strip())
	arr=list(map(int,input('Enter array elements: ').strip().split()))
	arr.sort()
	print(arr[n//2])
except:
	print('invalid')