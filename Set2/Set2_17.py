try:
	n=int(input('Enter a number: ').strip())
	temp=n
	sum=0
	while(temp!=0):
		sum+=(temp%10)**3
		temp=temp//10
	if(n==sum):
		print('Yes')
	else:
		print('No')
except:
	print('invalid')