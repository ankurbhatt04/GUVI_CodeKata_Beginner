try:
	year=input('Enter any year:')
	yr_int=int(year)
	if(yr_int%400==0 or (yr_int%100!=0 and yr_int%4==0)):
		print('Yes')
	else:
		print('No')
except:
	print('invalid')