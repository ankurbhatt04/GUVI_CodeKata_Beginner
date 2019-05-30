try:
	n=int(input('Enter a number: ').strip())
	temp=n
	rev=0
	while(temp!=0):
		rev=rev*10+temp%10
		temp=temp//10
	if(rev==n):
		print('Yes')
	else:
		print('No')
except:
	print('invalid')