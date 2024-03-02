def isanagram(n1, n2):
	lista=[]
	c=0
	lista2=[]
	for n in n1:
		lista.append(n)
	for n in n2:
		lista2.append(n)
	for n in range(0, len(lista)):
		try:
			if lista[c] in n2:
				c2=lista2.index(lista[c])
				del lista[c]
				del lista2[c2]
		except:
		 	return False
	if len(lista)==0 and len(lista2)==0:
		return True
	else:
		return False