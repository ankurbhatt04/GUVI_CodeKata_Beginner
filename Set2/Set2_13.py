try:
	n=int(input('Enter a number: ').strip())
	flag=0
	if(n==0 or n==1):
		print('No')
	else:
		for i in range(2,int(n**0.5)+1):
			if(n%i==0):
				flag=1
		if(flag==0):
			print('Yes')
		else:
			print('No')
except:
	print('invalid')