var = raw_input("Please enter path: ")
file = open(var, 'r')
out = []
output = []
result = []
temp = file.read().splitlines()
lista = sorted(temp, key=len, reverse=True)
def toString(s):
	return ''.join(str(e) for e in s)
c = 0
for l in lista:
	first = lista[c]
	c +=1
	result.append(first)
	for w in lista:
		pal = list(first)
		count = 0
		word = toString(w)
		for p in pal:
			letra = pal[count]
			pal[count] = ""
			data2 = toString(pal)
			if data2 == word:
				result.append(word)
				first = data2
				break
			else:
				pal[count] = letra
				count +=1	
	lista[:] = [x for x in lista if x not in result]
	out.append(','.join(result).split(','))
	del result[:]
maxlen = max(len(x) for x in out)
for o in out:
	if len(o)==maxlen:
		print ' => '.join(o)