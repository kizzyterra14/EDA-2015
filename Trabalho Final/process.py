lst = [1201,1308,1308,1201,1403,1308]

aux = []
dif = []

while lst != None:
	head = lst.pop(0)
	flag = 0
	for i in range(len(lst)):
		if(head == lst[i]):
			aux.append((head, lst[i])
			lst.pop(i)
			flag = 1
	if flag == 0:
			dif.append(head)


