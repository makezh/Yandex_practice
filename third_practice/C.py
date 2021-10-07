n, m = map(int, input().split())
a = {int(input()) for _ in range(n)}
b = {int(input()) for _ in range(m)}

print(len(a.intersection(b)))
print(*sorted(a.intersection(b)))

print(len(a-b))
print(*sorted(a-b))

print(len(b-a))
print(*sorted(b-a))