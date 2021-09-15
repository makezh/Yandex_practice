n,k,m = map(int, input().split())

k1,k2 = 0, 0


while n >= k:
	k1 = n//k
	k2+= k1*(k//m)
	n -= k1*(k//m)*m

print(k2)

