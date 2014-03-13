from collections import OrderedDict

toVector = lambda x: map(int, x)

vectors1 = []
vectors2 = []
l = 1

with open("A-large-practice.in") as i:
	n = int(i.readline())
	for j in xrange(n):
		_ = i.readline()
		v1 = toVector(i.readline().split())
		v2 = toVector(i.readline().split())
		v1.sort()
		v2.sort()
		v2.reverse()
		vectors1.append(v1)
		vectors2.append(v2)
		print l
		l +=1

scalars = []
for k,v in zip(vectors1, vectors2):
	scalar = sum([k[i]*v[i] for i in xrange(len(k))])
	scalars.append(scalar)


with open("output", "r+") as out:
	for i,k in zip(xrange(len(scalars)), scalars):
		out.write("Case #%d: %d\n"%(i+1, k))


