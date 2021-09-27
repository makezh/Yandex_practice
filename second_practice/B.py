x1 = int(input())
ans = ''
x2 = 0
while x1 != (-2 * 10**9):
		x2 = int(input())
		if x2 != (-2 * 10**9):
			if x1 == x2:
				if ans == '' or ans == 'CONSTANT':
					ans = 'CONSTANT'
				elif ans == 'ASCENDING' or ans == 'WEAKLY ASCENDING':
					ans = 'WEAKLY ASCENDING'
				elif ans == 'DESCENDING' or ans == 'WEAKLY DESCENDING':
					ans = 'WEAKLY DESCENDING'
			elif x2 >= x1 and (ans == '' or ans == 'ASCENDING' or ans == 'WEAKLY ASCENDING' or ans == 'CONSTANT'):
				if x2>x1 and ans != 'WEAKLY ASCENDING' and ans != 'CONSTANT':
					ans = 'ASCENDING'
				else:
					ans = 'WEAKLY ASCENDING'
			elif x2 <= x1 and (ans == '' or ans == 'DESCENDING' or ans == 'WEAKLY DESCENDING' or ans == 'CONSTANT'):
				if x2 < x1 and ans != 'WEAKLY DESCENDING' and ans != 'CONSTANT':
					ans = 'DESCENDING'
				else:
					ans = 'WEAKLY DESCENDING'
			else:
				ans = 'RANDOM'
		#print(x1, x2, ans)
		x1 = x2
print(ans)