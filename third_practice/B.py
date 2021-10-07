a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(*sorted(b.intersection(a)))