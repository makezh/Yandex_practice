a,b,c = int(input()), int(input()), int(input())
if a ==0:
	if b**0.5 == c:
		print('MANY SOLUTIONS')
	else:
		print('NO SOLUTION')
else:
	x = (c**2 - b)/a
	if c < 0 or x != int(x):
		print('NO SOLUTION')
	else:
		print(int(x))