a = list(map(int,input().split()))
maxi = pmax = a.index(min(a))
mini = pmin = a.index(max(a))
if len(a) == 2:
	print(min(a), max(a))
else:
	for i in range(0, len(a)):
		if a[i] >= a[maxi] and i != maxi:
			pmax = maxi
			maxi = i
		elif a[i] > a[pmax]:
			pmax = i
		if a[i] <= a[mini] and i != mini:
			pmin = mini
			mini = i
		elif a[i] < a[pmin]:
			pmin = i
	#print(a[maxi], a[pmax])
	#print(a[mini], a[pmin])

	MAX = max(a[maxi]*a[pmax], a[mini]*a[pmin], a[maxi]*a[pmin], a[pmax]*a[mini])

	if a[maxi]*a[pmax] == MAX:
		print(a[pmax], a[maxi])
	elif a[mini]*a[pmin] == MAX:
		print(a[mini],a[pmin])
	elif a[maxi]*a[pmin] == MAX:
		print(a[pmin],a[maxi])
	elif a[pmax]*a[mini] == MAX:
		print(a[mini],a[pmax])