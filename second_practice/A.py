x= list(map(int, input().split()))
i=0
fl = True
while i+1<len(x):
	if x[i+1]<=x[i]:
		fl = False
		print('NO')
		break
	i+=1
if fl:
	print('YES')