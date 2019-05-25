try:
	a,b,c=list(map(int,input("Enter three numbers: ").strip().split(' ')))
	print(max([a,b,c]))
except:
	print('invalid')