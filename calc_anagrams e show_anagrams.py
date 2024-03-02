import random
from math import factorial
def calc_anagrams(n):
	lista2=[]
	global c
	c=factorial(len(n))
	i=0
	while i<len(n)-1:
		if n[i] not in lista2:
			if n.count(n[i])>0:
				lista2.append(n[i])
				c=c/factorial(n.count(n[i]))
		i=i+1
	return c
		
def show_anagrams(n):
	lista3=[]
	for k in n:
		lista3.append(k)
	lista=[]
	while len(lista)<c:
		a2=""
		random.shuffle(lista3)
		for k in lista3:
			a2=a2+k
		if a2 not in lista:
			lista.append(a2)
	lista=sorted(lista)
	for k in lista:
		if k==n:
			lista.remove(k)
	for k in lista:
		print(k)

calc_anagrams("ara")
show_anagrams("ara")