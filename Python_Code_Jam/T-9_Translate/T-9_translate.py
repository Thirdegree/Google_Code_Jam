

codes = {'a':'2','b':'22','c':'222','d':'3','e':'33','f':'333','g':'4',
		'h':'44','i':'444','j':'5','k':'55','l':'555','m':'6','n':'66',
		'o':'666','p':'7','q':'77','r':'777','s':'7777','t':'8','u':'88',
		'v':'888','w':'9','x':'99','y':'999','z':'9999', ' ':'0', '\n': ''}


strings = []
with open("C-large-practice.in") as i:
	n = int(i.readline())
	for j in xrange(n):
		strings.append(i.readline())

translated_strings = []
for i in strings:
	temp = ""
	i = i.replace("\n","")
	for j in xrange(len(i)):
		if j == len(i)-1:
			temp += codes[i[j]]
			print temp
			continue
		else:
			if codes[i[j]][0] == codes[i[j+1]][0]:
				temp += codes[i[j]]+ ' '
			else:
				temp += codes[i[j]]


	translated_strings.append(temp)

with open("output","r+") as out:
	for i, k in zip(xrange(len(translated_strings)), translated_strings):
		out.write("Case #%d: %s\n"%(i+1,k))