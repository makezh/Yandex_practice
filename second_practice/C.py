n = int(input())
a = list(map(int,input().split()))
x = int(input())
imin = 0
diff = abs(x-a[imin])
for i in range (1, n):
	if abs(a[i] - x) < diff:
		imin = i
		diff = abs(a[i] - x)
print(a[imin])