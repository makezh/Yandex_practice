n,k,m = map(int, input().split())

ost = n
k1,k2,k22= 0, 0, 0

# 13 5 3
# n  k m
while ost//k > 0:
	k1 = ost//k
	ost -=  k1*k

	k22 = k//m * k1
	k2 += k22
	ost += (k%m)*k22

print(k2)
