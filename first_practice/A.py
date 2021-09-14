t1, t2 = map(int, input().split())
#в комнате и желаемая
mode = input()
#freeze heat auto fan
if mode == 'fan':
	print(t1)
elif mode == 'auto':
	print(t2)
elif mode == 'heat':
	if t1 >= t2:
		print(t1)
	else:
		print(t2)
elif mode == 'freeze':
	if t1 <= t2:
		print(t1)
	else:
		print(t2)