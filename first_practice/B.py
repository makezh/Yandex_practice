a, b, c = int(input()), int(input()), int(input())
if a + b > c and a+c > b and b+c > a:
	print('YES')
else:
	print('NO')