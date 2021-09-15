n, a = input(), [input() for i in range(3)]
s = ''.join([n[i] for i in range(len(n)) if n[i].isdigit()])
for i in range(len(a)):
    a[i] = ''.join([a[i][j] for j in range(len(a[i])) if a[i][j].isdigit()])
    if (len(a[i]) == 11 and a[i][1:] == s[1:]) or ('495' + a[i]) == s[1:]\
            or a[i][1:] == ('495' + s[:]) or a[i] == s:
        print('YES')
    else:
        print('NO')
				